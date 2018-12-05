# import os

import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

# 定义神经网络结构相关的参数
INPUT_NODE = 784
OUTPUT_NODE = 10
LAYER1_NODE = 500

# 配置神经网络的参数。
BATCH_SIZE = 100
LEARNING_RATE_BASE = 0.8
LEARNING_RATE_DECAY = 0.99
REGULARIZATION_RATE = 0.0001
TRAINING_STEPS = 4000
MOVING_AVERAGE_DECAY = 0.99

# 模型保存的路径和文件名
MODEL_SAVE_PATH = "./model/"
MODEL_NAME = "model.ckpt"


def inference(input_tensor, avg_class, weights1, biases1, weights2, biases2):
    # 当没有提供滑动平均类时,直接使用参数当前的取值.
    if avg_class == None:
        layer1 = tf.nn.relu(tf.matmul(input_tensor, weights1) + biases1)

        # 计算输出层的前向传播结果.因为在计算损失函数时会一并计算softmax函数.
        # 所以这里不需要加入激活函数.而且不加入softmax不会影响预测结果.因为预测使用的是
        # 不同类别对应节点输出值的相对大小,有没有softmax层对最后分类结果计算没有影响.于是
        # 在计算整个神经网络的前向传播时可以不加入最后的softmax层.
        return tf.matmul(layer1, weights2) + biases2
    else:
        # 首先使用avg_class.average函数来计算得出变量的滑动平均值,
        # 然后再计算相应的神经网络的前向传播结果.
        layer1 = tf.nn.relu(
            tf.matmul(input_tensor, avg_class.average(weights1)) +
            avg_class.average(biases1)
        )
        return tf.matmul(layer1, avg_class.average(weights2) +
                         avg_class.average(biases2))


# 训练模型的过程.
def train(mnist):


    x = tf.placeholder(tf.float32, [None, INPUT_NODE], name='x-input')
    y_ = tf.placeholder(tf.float32, [None, OUTPUT_NODE], name='y-input')

    # 生成隐藏层的参数.
    weights1 = tf.Variable(
        tf.truncated_normal([INPUT_NODE, LAYER1_NODE], stddev=0.1)
    )

    biases1 = tf.Variable(
        tf.constant(0.1, shape=[LAYER1_NODE]))
    # 生成输出层参数
    weights2 = tf.Variable(
        tf.truncated_normal([LAYER1_NODE, OUTPUT_NODE], stddev=0.1))
    biases2 = tf.Variable(
        tf.constant(0.1, shape=[OUTPUT_NODE]))

    # 计算在当前参数下神经网络前向传播结果. 这里给出的用于计算滑动平均的类为None,
    # 所以函数不会使用参数的滑动平均值.

    y = inference(x, None, weights1, biases1, weights2, biases2)

    # 定义存储训练轮数的变量, 这个变量不需要计算滑动平均值,所以这里指定的这个变量为不可训练
    # 的变量(trainable= Flase).  在使用TensorFLOW训练神经网络时,
    # 以便会将代表训练论述的变量指定为不可训练的参数.
    global_step = tf.Variable(0, trainable=False)

    # 给定滑动平均衰减率和训练轮数的变量,初始化滑动平均类.
    # 第四章中介绍过给定训练轮数的变量可以加快训练早期变量的更新速度.
    variable_averages = tf.train.ExponentialMovingAverage(
        MOVING_AVERAGE_DECAY, global_step)

    # 在所有代表神经网络参数的变量上使用滑动平均. 其他辅助变量(比如global_step)
    # 就不需要了. tf.trainable_variables返回的就是图上集合
    # GraphKeys.TRAINABLE_VARIABLES中的元素. 这个集合的元素就是所有没有指定
    # trainable=False的参数.
    variables_averages_op = variable_averages.apply(
        tf.trainable_variables())

    # 计算使用了滑动平均之后的前向传播结果. 第四章中介绍过滑动平均不会改变变量本身的取值,
    # 而是会维护一个影子变量来记录其滑动平均值.所以当需要使用这个滑动平均值时,
    # 需要明确调用average函数.
    average_y = inference(
        x, variable_averages, weights1, biases1, weights2, biases2)

    # 计算交叉熵作为刻画预测值和真实值之间差距的的损失函数.这里使用了TensorFlow中提供
    # 的 sparse_softmax_cross_entropy_with_logits函数来计算交叉熵.
    # 当分类问题只有一个正确答案时,可以使用这个函数来加速交叉熵的计算. MNIST问题的图片中
    # 只包含了0-9中的一个数字,所以可以使用这个函数来计算交叉熵损失.
    # 这个函数的第一个参数是神经网络不包括softmax层的前向传播结果,第二个时训练数据的正确答案,
    # 因为标准答案是一个长度为10的一位数组,而该函数需要提供的是一个正确答案的数字,所以需要
    # 使用tf.argmax函数来得到正确答案对应的类别编号.
    cross_entropy = tf.nn.sparse_softmax_cross_entropy_with_logits(
        logits=y, labels=tf.argmax(y_, 1)
    )
    cross_entropy_mean = tf.reduce_mean(cross_entropy)

    # 计算L2正则化损失函数.
    regularizer = tf.contrib.layers.l2_regularizer(REGULARIZATION_RATE)
    # 计算模型的正则化损失.一般只计算神经网络边上权重的正则化损失,而不使用偏置项.
    regularization = regularizer(weights1) + regularizer(weights2)

    # 总损失等于交叉熵损失上和正则化损失之和.
    loss = cross_entropy_mean + regularization
    # 设置学习率
    learning_rate = tf.train.exponential_decay(
        LEARNING_RATE_BASE,  # 基础学习率随着迭代的进行,更新变量时使用的
        global_step,  # 学习率在这个基础上递减
        mnist.train.num_examples / BATCH_SIZE,  # 过完所有的训练数据需要的迭代次数
        LEARNING_RATE_DECAY  # 学习率衰减速度
    )

    # 使用tf.train.GradientDescentOptimizer优化算法来优化损失函数.
    # 注意这里损失函数包含了交叉熵损失和L2正则化损失.
    train_step = tf.train.GradientDescentOptimizer(learning_rate).minimize(loss,
                                                                           global_step=global_step
                                                                           )
    # 在训练神经网络模型时,每过一遍数据既需要通过反向传播来更新神经网络中的参数,
    # 又要更新每一个参数的滑动平均值.累了以此完成多个操作,Tensorflow提供了tf.control_dependengcies
    # 和tf.group两种机制. 下面两行程序和
    # train.op = tf.group(train_step, variables_averages_op)是等价的
    with tf.control_dependencies([train_step, variables_averages_op]):
        train_op = tf.no_op(name='train')

    # 检验使用了滑动平均模型的神经网络的前向传播结果是否正确.
    # tf.argmax(average_y, 1)计算每一个样例的预测答案.其中average_y 是一个batch_size*10
    # 的二维数组,每一行表示一个靓丽的前向传播结果.tf.argmax的第二个参数'1'表示选取最大值的操作
    # 仅在第一个维度中进行,也就是说,只在每一行选取最大值对应的下标.于是得到的结果时一个长度为batch
    # 的一位数组,这个一位数组中的值就表示了每一个样例对应的数字识别结果.
    # tf.equal判断两个张量的每一维是否相等,如果相等则返回TRUE ,否则返回False

    correct_prediction = tf.equal(tf.argmax(average_y, 1), tf.argmax(y_, 1))
    # 这个运算首先讲一个布尔型的数值转换为实数值,
    # 然后计算平均值.这个平均值就是模型在这个一位数组上的正确率.
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

    # 初始化会话并开始训练过程.
    with tf.Session() as sess:
        tf.global_variables_initializer().run()
        # 准备验证数据. 一般在神经网络的训练过程中会通过验证数据来大致判断停止的
        # 条件和评判训练的效果.
        validate_feed = {x: mnist.validation.images,
                         y_: mnist.validation.labels}

        # 准备测试数据.在真实应用中,这部分数据在训练时是不可见的,这个数据至少是作为
        # 模型优劣的最后评价标准.
        test_feed = {x: mnist.test.images, y_: mnist.test.labels}

        # 迭代地训练神经网络.
        for i in range(TRAINING_STEPS):
            # 每1000 轮输出一次在验证数据集上的测试结果.
            if i % 1000 == 0:
                #
                #
                #
                #
                validate_acc = sess.run(accuracy, feed_dict=validate_feed)
                print('Arfter %d training steps, validation accuracy'
                      "using average model is %g " % (i, validate_acc))
            xs, ys = mnist.train.next_batch(BATCH_SIZE)
            sess.run(train_op, feed_dict={x: xs, y_: ys})

        # 在训练结束之后,在测试机上检测神经网络模型的最终正确率.
        test_acc = sess.run(accuracy, feed_dict=test_feed)
        print("After %d training steps, test accuracy using average"
              "model is %g" % (TRAINING_STEPS, test_acc))


# 主程序入口
def main(argv=None):
    # 声明处理MNIST数据集的类,这个类在初始化时会自动下载数据.
    mnist = input_data.read_data_sets('/home/zxf/zxf/TensorFlow/data/', one_hot=True)
    train(mnist)


# TensorFlow 提供的一个主程序入口,tf.app.run会调用上面定义的main函数.

if __name__ == '__main__':
    tf.app.run()


