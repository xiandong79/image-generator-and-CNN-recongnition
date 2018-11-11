
#%%
import numpy as np
import string
from PIL import Image, ImageFont, ImageDraw
import os
import json
import requests
# cwd = os.getcwd()
# if not os.path.exists(str(cwd + "/data/")):
#     os.makedirs(str(cwd + "/data/"))


#%%

def WordImageGenerator(words, word_font, image_name, image_size = (320, 80), offest = (40, 10)):
    '''
    Generate an image of text
    word:      The text to display in the image
    word_font:      The font to use
    image_name:     The file name
    image_size:      The image size
    offest:      The offest of the text in the image
    '''
    img = Image.new('RGB', image_size, "black")
    draw = ImageDraw.Draw(img)
    # Draw.text(xy, text, color_fill=None, font=None, anchor=None)
    draw.text(offest, words, (255, 255, 255), font = word_font)
    # img.save('/absolute/path/to/myphoto.jpg', 'JPEG')
    img.save(image_name, 'JPEG')


#%%
# The possible words to add in the image
url = 'https://www.randomlists.com/data/words.json'
response = requests.get(url).json()
canditate_words_list = response["data"]
print(canditate_words_list[:10])
print(len(canditate_words_list))


#%%
num_image = 8
num_words_per_image = list(np.random.randint(1, 3, size = num_image))
words_list = [' '.join(np.random.choice(canditate_words_list, num)) for num in num_words_per_image]
print(words_list)


#%%
#Get the font of word
# Linux
# font = ImageFont.truetype("LiberationMono-Regular.ttf", 16)
# font = ImageFont.truetype("arial.ttf", 16)
# Mac 
font = ImageFont.truetype("/Library/Fonts/Arial.ttf", 26)

#The largest size of word needed
max_font_size = max(font.getsize(words) for words in words_list)
print(max_font_size)
#Computed offset
offset = ((320 - max_font_size[0]) // 2, (80 - max_font_size[1]) // 2)
print(offset)
#Image size
image_size = (320, 80)
record = []


#%%
for image_id, words in enumerate(words_list):
    WordImageGenerator(words, font, str(image_id) + '.png', image_size, offset)
    record.append(str(image_id) + '.png,' + words)
    
#Write CSV file
with open('Train.csv', 'w') as file:
    file.write('\n'.join(record))


#%%
# Until, the 'traing image' i.e., An English word image generators, is achieved.


#%%
import numpy as np
import os
import string
import sys
from skimage.io import imread
from sklearn.model_selection import ShuffleSplit
from TFANN import ANNC
# TFANN.py needs module named 'tensorflow'


#%%
def LoadData(file_path = '.'):
    '''
    Loads the OCR dataset. A is matrix of images (NIMG, Height, Width, Channel).
    Y is matrix of characters (NIMG, MAX_CHAR)
    file_path:     Path to OCR data folder
    return: Data Matrix, Target Matrix, Target Strings
    '''
    train_file_path = os.path.join(file_path, 'Train.csv')
    A, Y, T, FN = [], [], [], []
    with open(train_file_path) as file:
        for Li in file:
            FNi, Yi = Li.strip().split(',')                     #filename,string
            T.append(Yi)
            A.append(imread(os.path.join(file_path, 'Out', FNi)))
            Y.append(list(Yi) + [' '] * (MAX_CHAR - len(Yi)))   #Pad strings with spaces
            FN.append(FNi)
    return np.stack(A), np.stack(Y), np.stack(T), np.stack(FN)

#%% [markdown]
# Next the neural network is constructed using the artificial neural network classifier (ANNC) class from TFANN. The architecture described above is represented in the following lines of code using ANNC.

#%%
#Architecture of the neural network
NC = len(string.ascii_letters + string.digits + ' ')
MAX_CHAR = 64
IS = (14, 640, 3)       #Image size for CNN
ws = [('C', [4, 4,  3, NC // 2], [1, 2, 2, 1]), ('AF', 'relu'), 
      ('C', [4, 4, NC // 2, NC], [1, 2, 1, 1]), ('AF', 'relu'), 
      ('C', [8, 5, NC, NC], [1, 8, 5, 1]), ('AF', 'relu'),
      ('R', [-1, 64, NC])]
#Create the neural network in TensorFlow
cnnc = ANNC(IS, ws, batchSize = 64, learnRate = 5e-5, maxIter = 32, reg = 1e-5, tol = 1e-2, verbose = True)
if not cnnc.RestoreModel('TFModel/', 'ocrnet'):
    #Fit the network
    cnnc.fit(A, Y)
    #The predictions as sequences of character indices
    YH = np.zeros((Y.shape[0], Y.shape[1]), dtype = np.int)
    for i in np.array_split(np.arange(A.shape[0]), 32): 
        YH[i] = np.argmax(cnnc.predict(A[i]), axis = 2)
    #Convert from sequence of char indices to strings
    PS = [''.join(CS[j] for j in YHi) for YHi in YH]
    for PSi, Ti in zip(PS, T):
        print(Ti + '\t->\t' + PSi)


