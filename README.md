# BNP


## 5. accuracy = 0!!!

注意，训练前需要把 `/model` 文件夹中的 `checkpoint` 和 `snapshot`文件删掉，否则 训练将基于这些历史的`checkpoint` 。

在 `/src` 文件夹中, `python main.py --train` 就可以训练模型，可是训练结果糟糕。



## 1. 从题目s中选择了这个题目
An English word image generators, then feed it to machine learning model [preferably neural network] to recognize the word from the image

## 2. [Bonus]

	o CreatethesimpleHTML+Javascripttoruntheprogram 
	o Deliver an API to call the program
	o Push the program as a Docker Image to Docker Hub
	o Demonstrate the use of Cloud Computing for the solution

## 3. 训练数据的生成 English word image generators

在 /data 文件夹，执行 `python generate_image_and_label_2_IAM_format` 就可以生成训练5000个图像数据 和它对应的 label。

（备用方案）在 `BNP/utils/image_generator.py` 是训练数据的生成脚本。然后这个 `class WordImageGenerator` 的实例化调用（生成数据）在 `ocr_ken.ipnb`. 你可以修改参数（如，图片的像素大小，图片数量，存储路径。）


## 4. 选择深度学习模型。

我决定采用 [SimpleHTR-master](https://github.com/githubharald/SimpleHTR ) 这个 model。其说明文档blog 在这里 [build-a-handwritten-text-recognition-system-using-tensorflow](https://towardsdatascience.com/build-a-handwritten-text-recognition-system-using-tensorflow-2326a3487cd5)，

我修改了 训练数据的生成 的输出，使得它生成的文件的路径 可以直接嵌入 model 使用。

 （怎么修改，可参考 https://towardsdatascience.com/faq-build-a-handwritten-text-recognition-system-using-tensorflow-27648fb18519 ）。
 
### Implementation using TF

The implementation in `/src` consists of 4 modules:

	1. SamplePreprocessor.py: prepares the images from the IAM dataset for the NN
	2. DataLoader.py: reads samples, puts them into batches and provides an iterator-interface to go through the data
	3. Model.py: creates the model as described above, loads and saves models, manages the TF sessions and provides an interface for training and inference
	4. main.py: puts all previously mentioned modules together




# Notice （另一个方案）：
先在 Ken 也在走另一个路（参考下面的blog），自己生成训练数据 `/utils/image_generator.py` 数据会自动保存在 `/data`
 文件夹下。
 
https://nicholastsmith.wordpress.com/2017/10/14/deep-learning-ocr-using-tensorflow-and-python/

接下来是 构建训练模型。@HongzoengNg

# bonus 如何docker化。
参考链接： https://medium.com/analytics-vidhya/deploy-your-first-deep-learning-model-on-kubernetes-with-python-keras-flask-and-docker-575dc07d9e76
