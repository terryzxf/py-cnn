import numpy as np

def sig(x):
    '''
    sigmoid函数
    :param x:  feature*w
    :return: sigmoid(x)(mat):Sigmoid值
    '''
    return 1.0/(1+np.exp(-x))


