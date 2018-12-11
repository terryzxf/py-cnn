# 如何使用tensorflow中的队列管理输入文件列表.假设所有的输入数据都已经整理成了TFRecord格式.
# 虽然一个TFRecord文件中可以存储多个训练样例,但是当训练数据量较大时,可以将数据分成多个TFRecord文件来提供处理效率
# tensorflow提供了tf.train.match_filenames_once函数来获取符合一个正则表达式的所有文件,
# 得到文件列表可以通过tf.train.string_input_producer函数进行有效的管理.
# tf.train.string_input_producer函数会使用初始化时提供的文件列表创建一个输入队列,
# 输入队列中原始的元素为文件列表中的所有文件.如7.1节中的样例代码所示,创建好的输入队列可以作为文件读取函数的参数.
# 每次调用文件读取函数时,该函数会先判断当前是否已有打开的文件可读,如果没有或者打开的文件已经读完,这个函数会从输入队列中出队
# 一个文件并从这个文件中读取数据.
# 通过设置shuffle参数, tf.train.string_input_producer函数支持随机打乱文件列表中文件出队的顺序.
# 当shuffle参数为True时,文件在加入队列之前会被打乱顺序,所以出队的顺序也是随机的.随机打乱文件顺序以及加入输入队列的过程会跑在一个单独的线程上,
# 这样不会影响获取文件的速度. tf.train.string_input_producer生成的输入队列可以同时被多个文件读取线程操作,
# 而且输入队列中的文件均匀地分给不同的线程,不出现有些文件被处理过多次而有些维恩间还没有被处理过的情况.
#    当一个输入队列中的所有文件都被处理完后,它会将初始化时提供的文件列表中的文件全部重新加入队列.
# tf.train.string_input_producer函数可以设置num_epochs参数来限制加载初始文件列表的最大轮数.
# 当所有文件都已经被使用了设定的轮数后,如果继续尝试读取新文件,输入队列会报错OutOfRange的错误.在测试神经网络模型时,
# 因为所有测试数据只需要使用一次,所以可以将num_epochs参数设置为1, 这样在计算完一轮之后程序将自动停止.
# 在展示tf.train.match_filenames_once 和 tf.train.string_input_producer函数的使用方法之前,
# 下面先给出一个简单的程序来生产样例数据.
#
#
import tensorflow as tf

# 创建TFRecord文件的帮助函数.
def _int64_feature(value):
    return tf.train.Feature(int64_list=tf.train.int64List(value=[value]))

# 模拟海量数据情况下将数据写入不同的文件.num_shards定义了总共写入多少文件
# instance_per_shard 定义了每个文件有多少个数据.

num_shards = 2

instances_per_shard = 2

for i in range(num_shards):

    #
    #
    #
    filename = ('/path/to/data.tfrecords-%.5d-of-%.5d' % (i, num_shards))
    writer= tf.python_io.TFRecordWriter(filename)
    # 将数据封装成Example结构并写入TFRecord文件.
    for j in range(instances_per_shard):
        #
        example = tf.train.Exmple(features=tf.train.Features(feature={
            'i': _int64_feature(i),
            'j': _int64_feature(j),
        writer.write(example.SerializeToString())
        }))
    writer.close()