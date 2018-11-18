 - by jiguo@20181118
#### how to run
1. go to current folder 
2. run 
```shell
pythoh bnp_app.py
```

#### test to recognize a word
1. open another terminal and input (use "small" as an example)
```shell
curl --data input_word="small" http://localhost:5000/predict
```