# 九九乘法表
for list1 in range(1, 10):  # list1取值为1-9
    list3 = []
    for list2 in range(1, list1 + 1):  # list2取值范围为1-9
        list3.append('%d * %d = %d' % (list2, list1, list1 * list2))  # list3记录循环的值
    print('\t'.join(list3))  # 将list3中的str间隔的'，'取消并变成格式\t。
    '''运用\t的时候要从行那里找规律'''

# 斐波那数列设计
x = 7
i = 1
n = 1
sum1 = 1
while i <= x:
    star = '*' * i
    print(star.center(7, ' '))
    i += 2
p = i - 2
while p > x or p > 1:
    p -= 2
    star = '*' * p
    print(star.center(7, ' '), end='\n')

num = int(input('斐波那数列'))
if num == 1:
    print(1)
elif num == 2:
    print(1)
else:
    while num > 2:
        sum1, n, y = sum1 + n, sum1, n
        num -= 1
        print(sum1)

# 求10W以内的所有质数
number = 100000
list1 = [2, 3, 5, 7]
list2 = []
list3 = []
for x in range(3, number, 2):
    if x % 3 == 0:
        pass
    elif x % 5 == 0:
        pass
    elif x % 7 == 0:
        pass
    else:
        if x not in list3:
            list2.append(x)
            for y in list2:
                sum = x * y
                if sum > 100000:
                    break
                else:
                    list3.append(sum)

list1 += list2
print(list1)
print(list3)

# 用list方法求质数：
import datetime

PRIMENUMBER = 100000
count = 1
print(2)
list1 = []
judge = True
start = datetime.datetime.now()
for x in range(3, PRIMENUMBER, 2):
    root = x ** 0.5
    for y in list1:
        if y > root:
            judge = True
            break
        if x % y == 0:
            judge = False
            break
    if judge:
        count += 1
        list1.append(x)
print((datetime.datetime.now() - start).total_seconds())
print(count)
