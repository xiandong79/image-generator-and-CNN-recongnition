# BNP

代码已经搞定。也写成了 APP 的形式。

1. 在命令行输入： `python app.py`
2. 然后在另一个命令行输入 `curl --data input_word="bad" http://localhost:5000/predict`

就可以看到 predict 的结果。

问题：目前，在打包成 docker image 过程中失败。

## 背景介绍

代码是 image_ocr.py `python image_ocr.py` 就可运行。

官方原文档：
https://github.com/keras-team/keras/blob/master/examples/image_ocr.py

参考的 blog 是：
https://www.dlology.com/blog/how-to-train-a-keras-model-to-recognize-variable-length-text/

source code is available both on his GitHub as well as a runnable Google Colab notebook.
但是这个的特点是，word-image-generator 是 on the fly 并不会保存下来。那么，如何封装展示给 BNP 呢？

# bonus 如何 docker 化。

参考链接： https://medium.com/analytics-vidhya/deploy-your-first-deep-learning-model-on-kubernetes-with-python-keras-flask-and-docker-575dc07d9e76

## To build our Docker container, run:

在目标文件夹：

```
sudo docker build -t bnp-app:latest .
```

## Run the Docker container

Now let’s run our Docker container to test our app:

```
sudo docker run -d -p 5000:5000 bnp-app
```

## Check the status of your container by running

```
sudo docker ps -a
```

## how to debug docker image

```
docker logs <CONTAINER ID> i.e., f2672b5aff0a
```

## Test our model

在另一个命令行：

```
curl  --data input_word="good" http://localhost:5000/predict
curl  --data input_word="am" http://localhost:5000/predict
curl  --data input_word="bad" http://localhost:5000/predict
```

## Create a Docker Hub

```
sudo docker images
sudo docker tag d03fcc88da88 xiandong/bnp-app
sudo docker push xiandong/bnp-app
```

## you can pull

`docker pull xiandong/bnp-app`

# Create a Kubernetes Cluster

```
kubectl run bnp-app --image=xiandong/bnp-app --port 5000
# We can verify that our pod is running by typing
kubectl get pods
# anyone visiting the IP address of our deployment can access our API.
kubectl expose deployment keras-app --type=LoadBalancer --port 80 --target-port 5000
# running
kubectl get service
```

## test

```
curl  --data input_word="bad" http://<EXTERNAL-IP  of k8s>/predict
```

# reference

1. https://github.com/tensorflow/tensorflow/issues/14356
2. https://medium.com/analytics-vidhya/deploy-your-first-deep-learning-model-on-kubernetes-with-python-keras-flask-and-docker-575dc07d9e76
3. https://github.com/Tony607/keras-image-ocr
4. https://www.dlology.com/blog/how-to-train-a-keras-model-to-recognize-variable-length-text/
5. https://stackoverflow.com/questions/24808043/importerror-no-module-named-scipy
6.
