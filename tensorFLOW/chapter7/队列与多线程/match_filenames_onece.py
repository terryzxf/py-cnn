import tensorflow as tf
import sys
# 使用tf.train.match_filenames_once 函数获取文件列表。

files = tf.train.match_filenames_once(sys.path[0]+'/path/to/data.tfrecords-*',name=None)

# 通过tf.train.string_input_producer函数创建输入队列，输入队列中文件列表为
# tf.train.match_filenames_once函数获取的文件列表，这里将shuffle参数设为False
# 来避免随机打乱读文件的顺序，但一般在解决真是问题时，会将shuffle参数设置为True。
filename_queue = tf.train.string_input_producer(files, shuffle=False)

# 如7.1节中所示读取并解析一个样本。
reader = tf.TFRecordReader()
_, serialized_example = reader.read(filename_queue)
features = tf.parse_single_example(serialized_example,features= {'i': tf.FixedLenFeature([], tf.int64),
                                                                 'j': tf.FixedLenFeature([], tf.int64)})

with tf.Session() as sess:
    # 虽然在本段程序中没有声明任何变变量，但使用tf,train.match_filenames_once函数时需要
    # 初始化一些变量
    sess.run(tf.local_variables_initializer())
    '''
    打印文件列表将得到下面结果
    
    '''
    sess.run(files)
    print(files)

    coord = tf.train.Coordinator()
    threads = tf.train.start_queue_runners(sess=sess,coord=coord)

    for i in range(6):
        print( sess.run([features['i'],features['j']]))
    coord.request_stop()
    coord.join(threads)
