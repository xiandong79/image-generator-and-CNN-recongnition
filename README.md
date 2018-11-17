# BNP

下载后，copy `ocr_xiandong.ipynb` 或 `ocr_ken.ipynb`  并重命名为自己名字的文件，如`ocr_XXX.ipynb`. 然后，play and enjoy。 希望你能推进一些进度。


## 4. 深度学习模型。

我决定采用 [SimpleHTR-master](https://github.com/githubharald/SimpleHTR ) 这个 model ，那么我们接下来要做的将 data_generator 生成的 /data/train, data/test 这些路径，接进去 model / src 代码中就行 （代码已经放到 /src 文件夹）。 

1. 修改data_generator 的产出。
2. 修改SimpleHTR-master src/ model 的输入数据接口 （怎么修改，可参考 https://towardsdatascience.com/faq-build-a-handwritten-text-recognition-system-using-tensorflow-27648fb18519 ）。


```
我觉得我们 copy  github 代码 ，链接入自己的 dataset 是可以的。时间来得及。
```

## 1. 从题目s中选择了这个题目
An English word image generators, then feed it to machine learning model [preferably neural network] to recognize the word from the image

## 2. [Bonus]

	o CreatethesimpleHTML+Javascripttoruntheprogram 
	o Deliver an API to call the program
	o Push the program as a Docker Image to Docker Hub
	o Demonstrate the use of Cloud Computing for the solution

## 3. 训练数据的生成 English word image generators

在 BNP/utils/image_generator.py 是训练数据的生成脚本。然后这个 class WordImageGenerator 的实例化调用（生成数据）在 ocr_ken.ipnb. 你可以修改参数（如，图片的像素大小，图片数量，存储路径。）
