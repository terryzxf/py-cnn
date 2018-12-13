# 将多个输入样例组织成一个batch可以提高模型的训练效率
# 所以在得到单个样例的预处理结果后还需要将他们组成一个batch
# 然后在提供给神经网络的输入层。tensorflow提供了tf.train.batch和tf.train.shuffle_batch函数
# 来将单个样例组织成batch的形式输出。这两个函数都会生成一个队列，队列的入队操作是生成单个样例的方法，
# 而每次出队得到的是一个batch的样例。他们唯一的区别是否会将数据循序打乱。一下代码展示这两函数用法。
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

# 使用7.3.2中方法读取解析得到的样例。这里假设Example结构中i表示一个样例的特征向量，
# 比如一张图像的像素矩阵。而J表示该样例对应的标签。
example, label= features['i'],features['j']

#一个batch中的样例个数。
batch_size = 3
# 组合样例的队列中最多可以存储的样例个数。这个队列如果太大，那么需要占用很多内存资源；
# 如果太小，那么出队操作可能会因为没有数据而被阻碍（block),从而导致训练效率降低。
# 一般来说这个队列的大小回合每一个batch的大小相关，下面一行代码给出了设置队列大小的一种方式。
capacity = 1000 + 3 * batch_size

example_batch, label_batch = tf.train.batch([example, label], batch_size =batch_size, capacity=capacity)

with tf.Session() as sess:
    tf.local_variables_initializer().run()
    tf.global_variables_initializer().run()
    coord = tf.train.Coordinator()
    treads = tf.train.start_queue_runners(sess=sess, coord=coord)

    for i in range(2):
        cur_example_batch, cur_label_batch = sess.run([example_batch,label_batch])

        print( cur_example_batch, cur_label_batch)
    coord.request_stop()
    coord.join(threads)
