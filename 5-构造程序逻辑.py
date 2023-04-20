'''
寻找水仙花数

Version:0.1
Author:coloes
'''

for num in range(100, 1000):
    low = num % 10
    mid = num // 10 % 10
    high = num // 100

    if low ** 3 + mid ** 3 + high ** 3 == num:
        print(num)

'''
正数反转

Version:0.1
Author:coloes
'''

num = int(input("输入你的数字："))

reversed_num = 0
while num > 0:
    reversed_num = reversed_num * 10 + num % 10
    num //= 10
print(reversed_num)

'''
百钱百鸡
公鸡5块一只
母鸡3块一只
小鸡1块三只
一百块买100只鸡
公鸡，母鸡，小鸡共多少个

Version:0.1
Author:coloes
'''



for x in range(21):
    for y in range(34):
        z = 100 - x -y
        if x * 5 + y * 3 + z / 3 == 100:
            print(x,y,z) 