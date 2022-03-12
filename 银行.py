import random
import time
import os


def Miao_time():
    for i in range(10):
        print('\r即将退出，还剩%s秒' % (10 - i), end='')  # \r 表示去除上一行接着下一行    end=" " 表示不换行
        time.sleep(1)
    print()# 引用time模块
    print('安全退出')


# 这个是匿名函数
a = lambda a: a * a  # lambda 后加参数 再加式子
a(8)


def money():
    b = 1
    with open('账密123', 'r+') as f:
        for i in f:
            a = i.split('--')
            print('请先登入账户')
            name = input('请输入姓名:')
            id_cord = input('请输入卡号:')
            if int(id_cord) == int(a[3]) and name == a[1]:
                while b <= 3:
                    code = input('请输入密码:')
                    if int(code) == int(a[5]):
                        print('密码正确')
                        print(a[:8])
                        link = input("输入你要的操作:")
                        if link == '取款':
                            z = 0
                            while 1:
                                money = input('请输入您操作的金额:')
                                if int(money) <= int(a[7]):
                                    # 取款的金额
                                    message = '姓名--' + name + '--卡号--' + id_cord \
                                              + '--密码--' + code + '--余额--' + a[7] + '--'
                                    data = ''
                                    with open('账密123', 'r+') as f:
                                        for i in f:
                                            if (i.find(message) == 0):
                                                c = int(a[7]) - int(money)
                                                i = '姓名--' + name + '--卡号--' + id_cord + '--密码--' \
                                                    + code + '--余额--' + str(c) + '--'
                                            data += i
                                    with open('账密123', 'r+') as f:
                                        f.writelines(data)
                                        f.close()
                                    with open('账密123', 'r+') as f:
                                        for i in f:
                                            a = i.split('--')
                                            print(a[:8])
                                            user = input('是否继续:')
                                            if user == '是':
                                                print('请继续操作.')
                                                # break
                                            else:
                                                return print('退出')
                                else:
                                    print('余额不足')
                        elif link == '存款':
                            while 1:
                                money = input('请输入你操作的金额!')
                                # 存款的金额
                                message = '姓名--' + name + '--卡号--' + id_cord \
                                          + '--密码--' + code + '--余额--' + a[7] + '--'
                                data = ''
                                with open('账密123', 'r+') as f:
                                    for i in f:
                                        if i.find(message) == 0:
                                            c = int(a[7]) + int(money)
                                            i = '姓名--' + name + '--卡号--' + id_cord + '--密码--' \
                                                + code + '--余额--' + str(
                                                c) + '--'
                                        data += i
                                with open('账密123', 'r+') as f:
                                    f.writelines(data)
                                    f.close()
                                with open('账密123', 'r+') as f:
                                    for i in f:
                                        a = i.split('--')
                                        print(a[:8])
                                        user = input('是否继续:')
                                        if user == '是':
                                            print('准备')
                                            break
                                        else:
                                            return print('退出')
                        elif link == '转账':
                            fopen = open('账密123', 'r')
                            w_str = ""
                            other = input('请输入对方户主名:')
                            other_id = input('请输入对方账户:')
                            money = input('请输入你要转的金额')
                            w_str = ""
                            try:
                                with open('账密123', 'r+') as f:
                                    for i in f:
                                        a = i.split('--')
                                        a = str(a)
                                        b = a.replace('3039', '80')
                                        print(a)
                                        print('-----')
                                        print(b)
                            except Exception as e:
                                print(e)

                                # c=int(a[7])+50
                                # print(a)

                                # else:3
                                #     print('没有找到用户')
                                # message = '姓名--' + name + '--卡号--' + id_cord + '--密码--'
                                # + code + '--余额--' + a[7] + '--'
                                # data = ''
                                # with open('账密123', 'r+') as f:
                                #     for i in f:
                                #         if i.find(message) == 0:
                                #             c = int(a[7]) + int(money)
                                #             i = '姓名--' + name + '--卡号--' + id_cord + '--密码--' \
                                #                             + code + '--余额--' + str(c) + '--'
                                #         data += i
                                # with open('账密123', 'r+') as f:
                                #     f.writelines(data)
                                #     f.close()
                                # print(a[0:8])
                    else:
                        print('密码不正确还剩机会%s次' % (3 - b))
                        b = b + 1
                        if b == 4:
                            return print('账户冻结'), Miao_time()
            else:
                print('没有此账户！')
                user = input('是否需要创建')
                if user == '是':
                    return Bank_sys(chose)
                else:
                    Miao_time()


def find(chose):
    b = 1
    id_cord = (input('请输入卡号:'))
    with open('账密123', 'r') as f:  # 以读的方式打开文件账密123
        for i in f:
            a = i.split('--')  # 以‘--’切割
            if int(id_cord) == int(a[3]):
                while b <= 3:
                    code = int(input('请输入密码:'))
                    if code == int(a[5]):
                        print(a[:8])
                        break
                    else:
                        print('密码错误,还剩机会%s次' % (3 - b))
                    b = b + 1
                break
            elif int(id_cord) != int(a[3]):
                print('没有此账户')
                id = input('是否创建用户')
                if id == '是':
                    return Bank_sys(chose)
                else:
                    Miao_time()


def Z_M(name, id_cord, code, save):
    message = '\n姓名--' + name + '--卡号--' + \
              id_cord + '--密码--' + code + '--余额--' + save + '--'
    with open('账密123', 'r+') as f:
        f.write(message)
        for i in f:
            a = i.split(str('--'))


def Bank_sys(chose):
    n = 0
    global code, name, id_cord
    while n < 1:
        name = input("请输入姓名：")
        id = input("请输入身份证：")
        phone = int(input("请输入手机号:"))
        if len(id) != 18 and phone != 11:
            print('重新输入格式不对！')
        else:
            n, a = 0, 0
            while n < 3:
                yzm = random.randint(9999, 100000)
                print('您的验证码为：', yzm)
                yzm1 = int(input('请输入验证码:'))
                if yzm1 == yzm:
                    id_cord = random.randint(1, 1000000)
                    print('卡号为:', id_cord)
                    while a <= 3:
                        code = input("设置您的密码:")
                        if len(code) == 6:
                            code1 = input("请再次确认您的密码：")
                            if code1 == code:
                                save = 10
                                Z_M(str(name), str(id_cord), str(code), str(save))
                                return print('开户成功！')
                            else:
                                print("密码不匹配\请再次输入")
                        else:
                            print('密码过短')
                else:
                    print('验证码错误!')
                    a = a + 1
                n = n + 1


# def frozen_account():
#     username=input('请输入您要锁定的账户名:')
#     identify=input('请输入身份证:')


func = {1: ':开户', 2: ':查询', 3: ':取款/存款/转帐',
        4: ':锁定/解锁', 5: ':退出'}
for m, n in func.items():
    print(m, n, end="\t")
print()
print('需要在本目录建立一个txt文档名为:账密123')
chose = input("请输入你要选择的功能编号：")
if chose == '1':
    Bank_sys(chose)
elif chose == '2':
    find(chose)
elif chose == '3':
    money()
elif chose == '4':
    pass
else:
    Miao_time()


# 学习1
# 斐波那契数列
n = 0
i = 0
# 1,1,2,3,5,
lst = []
# def func(n):
#     if len(lst)<900:
#         lst.append(n)
#         return func(n)
#     else:
#         print(len(lst))
# func(n)
# while i<5:
#     a, b= 1, 1
#     lst.append(a)
#     lst.append(b)
#     b=lst[n]+lst[n+1]
#     n=n+1
#     lst.append(b)
#
#     print(lst)
#     i+=1


# 2
# 正则表达式
# 字符组:[]写在中括号的内容,都出现在下面的某个字符的位置上符合规则的
# [a-z]匹配字母
# [0-9]匹配数字
# [A-Z]匹配字母
# [A-z]或[a-zA-Z]匹配大小写字母
# [a-zA-Z0-9]匹配数字大小字母
# [a-zA-Z0-9_]==\W匹配数字大小写字母下划线


# 转义符
# print('\\r44')#让后面那个转义符失去转义


# 元字符
# \w 匹配数字字母下划线
# \d{9} 匹配[0,9]数字    {9}只约束前面的表示乘9
# \s 匹配所有的空白符
# ^\d\d\d\d$  表示匹配固定的东西(这个表示匹配4位数的东西)^开始符 $结束符
# []表示只要出现在[]里面的全匹配
# [^]表示只要出现在[^]里面的全 不 匹配
# a|b 或 符合a或b的匹配
# 量词
# {n}表示出现的n次数
# {,n}表示至少出现n次
# {n,m}表示n到m次
