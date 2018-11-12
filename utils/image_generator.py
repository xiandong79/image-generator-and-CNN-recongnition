# -*- coding:utf-8 -*-
'''
File: image_generator.py
File Created: Monday, 12th November 2018
Author: Hongzoeng Ng (kenecho@hku.hk)
-----
Last Modified: Monday, 12th November 2018
Modified By: Hongzoeng Ng (kenecho@hku.hk>)
-----
Copyright @ 2018 KenEcho
'''
import numpy as np
from PIL import Image, ImageFont, ImageDraw
import os
import json
import requests

FONT = ImageFont.truetype("arial.ttf", 26)


class WordImageGenerator(object):
    def __init__(self, train_num=1000, test_num=300):
        self.image_num = {'train': train_num, 'test': test_num}
        self.dataset = {'train': [], 'test': []}
        self.offset = ()

    def _request_words(self):
        url = 'https://www.randomlists.com/data/words.json'
        response = requests.get(url).json()
        canditate_words_list = response["data"]
        return canditate_words_list

    def _word_image(
            self, words, word_font, image_name, dataset,
            image_size=(320, 80), offset=(40, 10)):
        """
        dataset: 'train' or 'test'
        """
        img = Image.new('RGB', image_size, "black")
        draw = ImageDraw.Draw(img)
        draw.text(offset, words, (255, 255, 255), font=word_font)
        img.save('./data/{}/{}.jpg'.format(dataset, image_name), 'JPEG')

    def generate_dataset(self):
        canditate_words_list = self._request_words()
        for k in self.dataset:
            num_words_per_image = list(
                np.random.randint(
                    1, 3, self.image_num[k]
                )
            )
            self.dataset[k] = [
                ' '.join(
                    np.random.choice(canditate_words_list, num)
                )
                for num in num_words_per_image
            ]
        words_list = self.dataset['train'] + self.dataset['test']
        max_font_size = max(FONT.getsize(words) for words in words_list)
        self.offset = (
            (320 - max_font_size[0]) // 2,
            (80 - max_font_size[1]) // 2
        )

    def save_image(self):
        for k in self.dataset:
            record = []
            for image_id, words in enumerate(self.dataset[k]):
                self._word_image(
                    words, FONT, str(image_id), k,
                    offset=self.offset
                )
                record.append(str(image_id) + ',' + words)
            with open("./data/{}.csv".format(k), 'w') as fw:
                fw.write("\n".join(record))
    
    def clear_dataset(self):
        for k in self.dataset:
            dir_list = os.listdir("./data/{}/".format(k))
            for f in dir_list:
                try:
                    os.remove('./data/{}/{}'.format(k, f))
                except:
                    pass
            try:
                os.remove('./data/{}.csv'.format(k))
            except:
                pass
        self.dataset = {'train': [], 'test': []}
