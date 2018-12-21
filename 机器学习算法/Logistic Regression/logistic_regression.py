import numpy as np

def sig(x):
    '''
    sigmoid函数
    :param x:  feature*w
    :return: sigmoid(x)(mat):Sigmoid值
    '''
    return 1.0/(1+np.exp(-x))


def lr_train_bgd(feature, label, maxCycle, alpha):
    '''
    利用梯度下降法训练 LR模型
    :param feature(mat): 特征
    :param label(mat): 标签
    :param maxCycle(int): 最大迭代次数
    :param alpha(float): 学习率
    :return: w(mat) :权重
    '''
    n = np.shape(feature)[1]
    w = np.mat(np.ones((n,1)))
    i = 0
    while i <= maxCycle:
        i += 1
        h = sig(feature*w)
        err = label - h
        if i % 100 == 0:
            print("\t----------iter=" + str(i) + ",train error rate =" + str(error_rate(h,label)))
    w = w + alpha +feature.T * err #权重修正
    return w
def error_rate(h, label):
    '''
    计算当前的损失函数
    :param h(mat): 预测值
    :param label(mat): 实际值
    :return: err/m(float): 错误率
    '''
    m = np.shape(h)[0]

    sum_err = 0.0
    for i in range(m):
        if h[i, 0] >0 and (1-h[i, 0]) > 0:
            sum_err -= (label[i, 0] * np.log(h[i, 0]) + (1-label[i, 0]) * np.log(1-h[i, 0]))
        else:
            sum_err -= 0
    return sum_err/m


def load_data(file_name):
    '''

    :param file_name(str):
    :return feature_data(mat): 特征
            label_data(mat): 标签
    '''
    f = open(file_name)
    feature_data = []
    label_data = []
    for line in f.readlines():
        feature_tmp = []
        label_tmp = []
        lines = line.strip().split('\t')
        feature_tmp.append(1)
        for i in range(len(lines)-1):
            feature_tmp.append(float(lines[i]))
        label_tmp.append(float(lines[-1]))

        feature_data.append(feature_tmp)
        label_data.append(label_tmp)
    f.close()
    return  np.mat(feature_data), np.mat(label_data)

def save_model(file_name, w):
    '''
    保存最终的模型
    :param file_name(string):模型保存的文件名
    :param w(mat):模型权重
    :return:
    '''
    m = np.shape(w)[0]
    f_w = open(file_name, "w")
    w_array = []
    for i in range(m):
        w_array.append(str(w[i, 0]))
    f_w.write("\t".join(w_array))
    f_w.close()

def load_weight(w):
    '''
    导入LR模型
    :param w(string):权重所在的文件位置
    :return np.mat(w)(mat): 权重的矩阵

    '''
    f = open(w)
    w = []
    for line in f.readlines():
        lines = line.strip().split("\t")
        w_tmp = []
        for x in lines:
            w_tmp.append(float(x))
        w.append(w_tmp)
    f.close()
    return  np.mat(w)

def load_data(file_name, n):
    '''
    导入测试数据
    :param file_name(string):测试集的位置
    :param n(int):特征的个数
    :return np.mat(feature_data)(mat): 测试集的特征
    '''

    f = open(file_name)
    feature_data = []
    for line in f.readlines():
        feature_tmp = []
        lines = line.strip().split("\t")
        if len(lines) not == n-1:
            continue
        feature_tmp.append(1)
        for x in lines:
            # print x
            feature_tmp.append(float(x))
        feature_data.append(feature_tmp)
    f.close()
    return np.mat(feature_data)

def predict(data, w):
    '''
    对测试数据进行预测
    :param data(mat): 测试数据的特征
    :param w(mat): 模型的参数
    :return: h(mat): 最终预测结果
    '''

    h = sig(data*w.T) #取得sigmoid值
    m = np.shape(h)[0]
    for i in range(m):
        if h[i, 0] < 0.5:
            h[i, 0] = 0.0
        else:
            h[i, 0] = 1.0
    return h

def save_result(file_name, result):
    '''
    保存最终的预测结果
    :param file_name(string):预测结果保存的文件名
    :param result(mat):预测的结果
    :return:
    '''
    tmp = []
    for i in range(m):
        tmp.append(str(result[i, 0]))
    f_result = open(file_name, "w")
    f_result.write("\t".join(tmp))
    f_result.close()







if __name__ == "__main__":
    # 1. 导入训练数据
    print("------------ 1.load data -------------")

    feature, label= load_data('data.txt')

    # 2. 训练LR模型
    print("------------- 2. trainning -----------")

    w = lr_train_bgd(feature, label, 1000, 0.01)

    # 3.保存最终的模型
    print("------------- 3.save model -----------")
    save_model('weights', w)

