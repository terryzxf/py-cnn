class info_get():

    """
    该文档用以实现病例登记系统的所有模块化功能:
    查找(基于放疗号的病人信息查找)
    创建图形 (放疗设野示意图)
    保存示意图
    生成放疗小结文档
    ! 生成讨论记录 (实现中...)
    ! 生成模式化的病历记录模版
    
    """
    import sys
    gerpath = str(sys.path[0])

    #data_path = '/home/zxf/病人登记/Data.xlsx'


    def erro_return(a):  # 错误提示 待完善>>>>

        labels = {'RTid': '放疗号', 'Names': '名字'}
        print('  {0:s}错误,未找到输入的{0:s}'.format(labels[a]))

    def info_get(signNum, excel_path=gerpath+'/模板doc/登记表.xlsx'):  # 基于[放疗号] [excel路径]的信息查询  返回[病人信息(Series)] ,[病人信息(str)]
        import pandas as pd
        from numpy import array as na
        error_mes = 'the input rtid is NUll, something wrong,check it '  # str(Df_data['RTid'])
        # def signNum_judge():    #判断输入的放疗号是否合法是否有效
        #if signNum == '':
            #return None,'the input rtid is NUll, something wrong,check it'
        if signNum == '' or int(signNum) not in range(0, 9999):
            return None, error_mes, '①'
        # signNum_judge()
        else:
            Df_data = pd.read_excel(excel_path)  # 读入登记表EXCEL文件

            # 替换中文属性名为英文属性名方便直接引用
            Df_data.columns = ['id', 'RTid','Curesta', 'Names', 'sex', 'age', 'Department', 'bedNum',
                           'dignose', 'phoneNum', 'bodyPart', 'startDate']
            #  'id',  住院号    'RTid', 放疗号   'Names',姓名    'sex',性别
            #  'age', 年龄   'Department',科别   'bedNum',床号  'dignose',诊断
            #  'phoneNum',电话  'bodyPart',治疗部位   'startDate'开始日期

            jug = str(signNum) in na(Df_data['RTid'])

            if not jug:

                return None, error_mes, Df_data['RTid'][431]
            else:
                Df_data.set_index('RTid', inplace=True)  # 设置放疗号为索引便于根据放疗号查询信息
                pt_S = Df_data.loc[str(signNum)]  # 获取查询的病人全部登记信息
                table_tail = Df_data.tail(40)  #获得最末四十条记录 提供UI_infoTbl接口
                # 将获取的信息显示转变为到窗体的字符串格式  为UI显示预留
                patient_info = ' '.join(['姓名:', pt_S.Names, '性别:', pt_S.sex, '年龄:', str(pt_S.age),
                                 '科室:', pt_S.Department, '床号:', str(pt_S.bedNum),
                                 '\n', '诊断:', pt_S.dignose, '电话:', str(pt_S.phoneNum), '\n',
                                 '治疗部位:', str(pt_S.bodyPart), '开始日期:', str(pt_S.startDate)])
                return pt_S, patient_info, table_tail

