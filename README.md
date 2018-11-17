# BNP


## 5. accuracy = 0!!!

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



