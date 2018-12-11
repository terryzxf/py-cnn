# tf.QueueRunner 主要用于启动多个线程来操作同一个队列,启动的这些线程可以通过上面介绍的tf.Coordinator类来统一管理.
#
# tf.QueueRunner 和 tf.Coordinator来管理多线程队列操作.

import tensorflow as tf

# 声明一个先进先出的队列 队列中最多一百个元素,类型为实数.
queue = tf.FIFOQueue(100,"float")

# 定义队列的入队操作
enqueue_op = queue.enqueue([tf.random_normal([1])])

# 使用tf.train.QueueRunner 来创建多个线程运行队列的入队操作.
# tf.train.QueueRunner 的第一个参数给出了被操作的队列,
# [enqueue_op]*5 表示了需要启动五个线程,每个线程中运行的是enqueue_op操作.
qr = tf.train.QueueRunner(queue, [enqueue_op]*5)

# 将定义过的QueueRunner加入到tensorflow计算图上指定的集合.
# tf.train.add_queue_runner函数没有指定集合
# 则加入默认的tf.GraphKeys.QUEUE_RUNNERS. 下面的函数就是将刚刚定义的qr加入默认的tf.GraphKeys.QUEUE_RUNNERS集合

tf.train.add_queue_runner(qr)
# 定义出队操作
out_tensor = queue.dequeue()

with tf.Session() as sess:

    # 使用tf.train.Coordinator来协同启动的线程.
    coord = tf.train.Coordinator()
    # 使用tf.train.QueueRunner时,需要明确调用tf.train.start_queue_runners来启动所有线程.否则因为没有线程运行入队操作.
    # 当调用出对操作时,程序会一致等待入队操作被运行. tf.train.start_queue_runners函数会默认启动
    # tf.GraphKeys.QUEUE_RUNNERS集合中所有的QueueRunner. 因为这个函数只支持启动指定集合中的QueueRunner,
    # 所以一般来说tf.train.add_queue_runner 函数和 tf.train.start_queue_runners函数会指定同一个集合.
    threads = tf.train.start_queue_runners(sess=sess,coord=coord)

    # 获取队列中的数值.
    for _ in range(30): print(sess.run(out_tensor)[0])

    # 使用tf.train.Coordinator来停止所有的线程.
    coord.request_stop()
    coord.join(threads)