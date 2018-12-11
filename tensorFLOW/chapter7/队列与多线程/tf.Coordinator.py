# 在tensorflow中,队列不仅仅时一种数据结果,还是异步计算张量取值的一个重要机制.比如多个线程可以同时想一个队列中写入元素,
# 或者同时读取一个队列中的元素
#
#
#
# tensorflow 提供了tf.Coordinator 和 tf.QueueRunner 两个类来完成多线程协同的功能.
# tf.Coordinator 主要用于协同多个线程一起停止,并提供了should_stop, request_stop,和join三个函数.
# 在启动线程之前,需要先声明一个tf.Coordinator类,并将这个类传入每一个创建的线程中.启动的线程需要一致查询tf.Coordinator类中提供的
# should_stop函数,当这个函数的返回值为True时,则当前线程也需要退出. 没一个启动线程都可以通过调用request_stop函数来通知其他线程退出.
# 当某一线程调用request_stop函数之后,should_stop函数的返回值江北设置为True,这样其他线程就可以同时被终止了.
#
# tf.Coordinator使用

import tensorflow as tf
import numpy as np
import threading
import time

# 线程中运行的程序, 这个程序每隔1秒判断是否需要停止并打印自己的Id
def MyLoop(coord, worker_id):
    # 使用tf.Coordinator类提供的协调工具判断当前线程是否需要停止.
    while not coord.should_stop():
        # 随机停止所有线程
        a= np.random.rand()
        if a < 0.1:
            print("停止于 id:  %d \n" % worker_id)
            # 调用coord.reuquest_stop()函数来通知其他线程停止.
            coord.request_stop()
        else:
            # 打印当前线程的ID.
            print("运行于 id:  %d\n" % worker_id)
        # 暂停1秒
        time.sleep(1)


# 声明一个tf.train.Coordinator类来协同多个线程.

coord = tf.train.Coordinator()

# 声明创建五个线程.
threads = [
    threading.Thread(target=MyLoop,args=(coord,i)) for i in range(5)
]

# 启动所有的线程
for t in threads: t.start()

# 等待所有线程退出
coord.join(threads)
