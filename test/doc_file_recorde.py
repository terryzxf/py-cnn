import arrow as arw
T = input('  times(>0): ')
st = input('  start date(workday) :')
# test tail
# T = '29'
# st = '2018-02-01'
weekend_judge = arw.get(st).isoweekday() in (6, 7)
T_judge = eval(T) < 0 or not (isinstance(eval(T), int))
# test tail
# print(type(weekend_judge))
# print ('  weekend_judge:',weekend_judge)
# print('  T_judge:',T_judge)
# print('  eval(T):',eval(T))
# print('  not(isinstance(eval(T),int)):',not(isinstance(eval(T),int)))
while T_judge or weekend_judge:
    if weekend_judge:
        print('  ', 'it`s weekend! please input a workday!')
        st = input('  start date: ')

    if eval(T) < 0:
        print("  times must above zero and must be 'int':")
        T = input('  times(>0): ')

    if not (isinstance(eval(T), int)):
        print("  times must above zero and must be 'int':")
        T = input("  times(>0,'int'): ")
    T_judge = eval(T) < 0 or not (isinstance(eval(T), int))
    weekend_judge = arw.get(st).isoweekday() in (6, 7)

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
out_end_date = end_date.format('YYYY-MM-DD')
# 'out_end_date' and 'end_date' is the day end oncology without interrupt
# print('  ', out_end_date)
