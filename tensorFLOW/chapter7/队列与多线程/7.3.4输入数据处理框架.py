# 在前面的小节中已经介绍了图7-14中展示的流程图中的所有步骤。在这一小节将把这些步骤穿成一个完整的
# tensorflow来处理输入数据。一下代码给出了这个完成的程序。
import tensorflow as tf


# 创建文件列表，通过文件列表创建文件输入队列。在调研输入数据处理流程，需要同意所以原始数据的格式并将它们存储到
# TFRecord文件中，下面给出了文件列表应该包含所有提供训练数据的TFRecord。
files = tf.train.match_filenames_once('/path/to/file_pattern-*')
filename_queue = tf.train.string_input_producer(files, shyffle=False)

reader = tf.TFRecordReader()
_, serilized_example = reader.read(filename_queue)
features = tf.parse_single_example(
    serialized_example,
    features={
        'image':tf.FixedLenFeature([], tf.string),
        'label':tf.FixedLenFeature([], tf.int64),
        'height':tf.FixedLenFeature([], tf.int64),
        'width':tf.FixedLenFeature([], tf.int64),
        'channels':tf.FixedLenFeature([], tf.int64)
    }
)

image, label = features['image'],features['label']
height, width = features['height'],features['width']
channels = features['channels']

decoded_image = tf.decode_raw(image,tf.uint8)
decoded_image.set_shape([height,width,channels])

image_size =299

distortde_imge = preprocess_for_train(
    decoded_image, image_size, image_size, None))

