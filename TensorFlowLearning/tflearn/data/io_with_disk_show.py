__author__ = 'kaiyao.dai'

import tensorflow as tf
import numpy as np

'''
将数据保存在磁盘并读取
tf.train.Example
tf.train.Message
tf.train.Example 相当于一个tf.train.Message组成的map,可以通过转为二进制串来读写

tfRecord
tf.data.Dataset
'''

data1 = np.arange(20)
# 将numpy转为Dataset
features_dataset = tf.data.Dataset.from_tensor_slices([data1, data1])
# 可以迭代，返回Tensor
for f0, f1 in features_dataset.take(1):
    # Tensor
    (f0, f1)



