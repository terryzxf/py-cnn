import arrow as arw


# 计算并返回 开始日期间隔次数后的结束日期
def calculate_end_date(startday, dosesplit):

    st = startday   # 开始日期
    T = dosesplit   # 次数
    # test tail
    # T = '29'
    # st = '2018-02-01'

    # test tail
    # print(type(weekend_judge))
    # print ('  weekend_judge:',weekend_judge)
    # print('  T_judge:',T_judge)
    # print('  eval(T):',eval(T))
    # print('  not(isinstance(eval(T),int)):',not(isinstance(eval(T),int)))


    st_date = arw.get(st)
    a = int(T) // 5
    b = int(T) % 5
    # test tail
    # print('   ', st_date.isoweekday())
    if b == 0:
        if st_date.isoweekday() == 1:
            day_shift = (a - 1) * 7 + 5
        else:
            day_shift = (a - 1) * 7 + 5 + 2

    elif b == 1:
        day_shift = a * 7 + b

    elif b == 2:
        if st_date.isoweekday() == 5:
            day_shift = a * 7 + b + 2
        else:
            day_shift = a * 7 + b

    elif b == 3:
        if st_date.isoweekday() == 4 or st_date.isoweekday() == 5:
            day_shift = a * 7 + b + 2
        else:
            day_shift = a * 7 + b

    elif b == 4:
        if st_date.isoweekday() == 1 or st_date.isoweekday() == 2:
            day_shift = a * 7 + b
        else:
            day_shift = a * 7 + b + 2
    end_date = st_date.shift(days=day_shift)
    out_enddate = end_date.format('YYYY-MM-DD')
    return out_enddate


    # 'out_enddate' and 'end_date' is the day end oncology without interrupt
    # print('  ', out_enddate)


# # backup
"""
##
# 计算并返回 开始日期间隔次数后的结束日期
def calculate_end_date(startday, dosesplit):
    import arrow as arw
    st = startday   # 开始日期
    T = dosesplit   # 次数
    # test tail
    # T = '29'
    # st = '2018-02-01'

    # test tail
    # print(type(weekend_judge))
    # print ('  weekend_judge:',weekend_judge)
    # print('  T_judge:',T_judge)
    # print('  eval(T):',eval(T))
    # print('  not(isinstance(eval(T),int)):',not(isinstance(eval(T),int)))


    st_date = arw.get(st)
    a = int(T) // 5
    b = int(T) % 5
    # test tail
    # print('   ', st_date.isoweekday())
    if b == 0:
        if st_date.isoweekday() == 1:
            day_shift = (a - 1) * 7 + 5 - 1
        else:
            day_shift = (a - 1) * 7 + 5 + 2 - 1

    elif b == 1:
        day_shift = a * 7 + b - 1

    elif b == 2:
        if st_date.isoweekday() == 5:
            day_shift = a * 7 + b + 2 - 1
        else:
            day_shift = a * 7 + b - 1

    elif b == 3:
        if st_date.isoweekday() == 4 or st_date.isoweekday() == 5:
            day_shift = a * 7 + b + 2 - 1
        else:
            day_shift = a * 7 + b - 1

    elif b == 4:
        if st_date.isoweekday() == 1 or st_date.isoweekday() == 2:
            day_shift = a * 7 + b - 1
        else:
            day_shift = a * 7 + b + 2 - 1
    end_date = st_date.shift(days=day_shift)
    out_enddate = end_date.format('YYYY-MM-DD')
    return out_enddate
    """

st_date = input('  start date(date(YYYY-MM-DD),workdatimes) :')
times = input('  times(number>0,int): ')

weekend_judge = arw.get(st_date).isoweekday() in (6, 7)
T_judge = eval(times) < 0 or not (isinstance(eval(times), int))
while T_judge or weekend_judge:
    if weekend_judge:
        print('   it`s weekend! please input a workdatimes!')
        st_date = input('  start date: ')

    if eval(times) < 0:
        print("  times must above zero and must be 'int':")
        times = input('  times(>0): ')

    if not (isinstance(eval(times), int)):
        print("  times must above zero and must be 'int':")
        times = input("  times(>0,'int'): ")
    T_judge = eval(times) < 0 or not (isinstance(eval(times), int))
    weekend_judge = arw.get(st_date).isoweekday() in (6, 7)
end_date  = calculate_end_date(st_date,times)
print(end_date)