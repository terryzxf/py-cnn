import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
import numpy as np
import sys

# TFRecord格式介绍
"""
TFRecord文件中的数据都是通过tf.train.Example Protocol Buffer 格式存储的。 以下代码给出了tf.train.Example的定义。
    message Example{
        Features features =1;
    };

    message Featrures{
        map<string, Feature> feature =1;
    }

    message Example{
        oneof kind{
            BytesList bytes_list = 1;
            FloatList float_list = 2;
            Int64List int64_list = 3;
        }
    };
"""


# 7.1.2

# 将MNIST输入数据转换为TFRecord的格式。


# 生成整数型的属性


def _int64_feature(value):
    return tf.train.Feature(int64_list=tf.train.Int64List(value=[value]))


# 生成字符串型的属性


def _bytes_feature(value):
    return tf.train.Feature(bytes_list=tf.train.BytesList(value=[value]))


# 读取数据


mnist = input_data.read_data_sets(sys.path[0] + "/MNIST_data/", dtype=tf.uint8, one_hot=True)

images = mnist.train.images

# 训练数据所对应的正确答案，可以作为一个属性保存在TFRecord中，

labels = mnist.train.labels

# 训练数据的图像分辨率，这可以作为Exmaple中的一个属性。
pixels = images.shape[1]
num_examples = mnist.train.num_examples

# 输出TFRecord文件的地址。
filename = sys.path[0] + "/TFRecord/output.tfrecords"
# 创建一个writer来写TFRecord文件。
writer = tf.python_io.TFRecordWriter(filename)

for index in range(num_examples):
    # 将图像矩阵转换成一个字符串。
    image_raw = images[index].tostring()
    # 讲一个样例转化为Example Protocol Buffer， 并将所有的信息写入这个数据结构。

    example = tf.train.Example(features=tf.train.Features(feature={
        'pixels': _int64_feature(pixels),
        'label': _int64_feature(np.argmax(labels[index])),
        'image_raw': _bytes_feature(image_raw)
    }))

    writer.write(example.SerializeToString())

writer.close()
