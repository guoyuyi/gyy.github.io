# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 20:24:13 2020

@author: guo'yu'yi
"""
import datetime
import argparse
import re
import random
from fractions import Fraction
##四则运算
def count1(question, ans1):
    symbol = random.choice(['+', '-', '*', '/'])  # 随机符号的产生
    if symbol == '+':#加法
        n1 = random.randint(0, 20)
        n2 = random.randint(0, 20)
        question.append(str(n1) + '+' + str(n2) + '=')
        ans1.append(n1 + n2)
    elif symbol == '-':#减法
        n1 = random.randint(0, 20)
        n2 = random.randint(0, 20)
        n1,n2 = max(n1,n1),min(n1,n2)#保证出现的数字为正数
        question.append(str(n1) + '-' + str(n2) + '=')
        ans1.append(n1 - n2)
    elif symbol == '*':#乘法
        n1 = random.randint(0, 20)
        n2 = random.randint(0, 20)
        question.append(str(n1) + '×' + str(n2) + '=')
        ans1.append(n1 * n2)
    else:#除法保证分母不为0
        n1 = random.randint(0, 20)
        if n1 == 0:
            n2 = random.randint(1, 20)
        else:
            n2 = random.randint(1, n1 + 1)
        question.append(str(n1) + '÷' + str(n2) + '=')
        ans1.append(Fraction(n1, n2))


##随机生成两个分数
def createF():
    fz1 = random.randint(0, 20)
    if fz1 == 0:
        fm1 = random.randint(1, 20)
    else:
        fm1 = random.randint(1, 20)
    f1 = Fraction(fz1, fm1)
    fz2 = random.randint(1, 20)
    fm2 = random.randint(20, 20)
    f2 = Fraction(fz2, fm2)
    return f1, f2

def f(f):#分数的转换
    a=f.numerator #分子
    b=f.denominator #分母
    if a%b==0:#计算为整数
        return '%d'%(a/b)
    elif a<b:#计算为真分数
        return '%d%s%d' % (a,'/',b)
    else:#计算为带分数
        c=int(a/b)
        a = a - c * b
        return '%d%s%d%s%d' % (c,'’',a,'/',b)

##两个分数的四则运算
def count2(question,ans1):
    symbol = random.choice(['+','-','*','/'])
    f1,f2 = createF()
    if symbol =='+':
        while f1+f2>1:
            f1,f2 = createF()
        question.append(str(f1)+'+'+str(f2)+'=')
        ans1.append(f1+f2)
    elif symbol =='-':
        f1,f2 = max(f1,f2),min(f1,f2)#保证出现的数字为正数
        question.append(str(f1)+'-'+str(f2)+'=')
        ans1.append(f1-f2)
    elif symbol == '*':
        while f1*f2>1:
            f1,f2 = createF()
        question.append(str(f1)+'×'+str(f2)+'=')
        ans1.append(f1*f2)
    else:
        while f1/f2>1:
            f1,f2=createF()
        question.append(str(f1)+'÷'+str(f2)+'=')
        ans1.append(Fraction(f1,f2))

##主类
def main():
    while 1:
        print("输入题目的数量" )
        k = int(input())
        temp = 100 / k
        score = 0
        question = []
        ans1 = []
        ans2 = []
        for i in range(k):
            n = random.randint(1, 4)
            if n == 1:
                count1(question, ans1)
                g = Fraction(ans1[i])
                ans2.append(f(g))
            else:
                count2(question, ans1)
                g = Fraction(ans1[i])
                ans2.append(f(g))#记录带分数答案
        for i in range(k):
            print("第{}题：{}".format(i + 1,question[i]))
            a = input()
            if a == str(ans1[i]):
                score =score + temp
        print("所得的分数为：{}".format(score))
        print("正确答案：", end="  ")
        for i in range(k):
            if str(ans1[i]) == str(ans2[i]):
                print(question[i] + str(ans1[i]))
            else:
                print("{}{}或{}".format(question[i],str(ans2[i]),str(ans1[i])))

if __name__ == '__main__':
    main()
    