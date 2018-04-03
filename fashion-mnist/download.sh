#!/bin/bash

mkdir -p data
curl -o data/train-images-idx3-ubyte.gz https://s3.amazonaws.com/anaconda-public-datasets/fashion-mnist/train-images-idx3-ubyte.gz
curl -o data/train-labels-idx1-ubyte.gz https://s3.amazonaws.com/anaconda-public-datasets/fashion-mnist/train-labels-idx1-ubyte.gz
curl -o data/t10k-images-idx3-ubyte.gz https://s3.amazonaws.com/anaconda-public-datasets/fashion-mnist/t10k-images-idx3-ubyte.gz
curl -o data/t10k-labels-idx1-ubyte.gz https://s3.amazonaws.com/anaconda-public-datasets/fashion-mnist/t10k-labels-idx1-ubyte.gz
