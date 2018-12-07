# print("tom's pet is a cat")
# print('tom said"hello world"')
# words='hello\nworld'
# print(words)
# lines='''haha
# xixi
# hehe'''
# print(lines)
# line='1\n2\n3'
# print(line)
# py_str='python'
# print(len(py_str))
# a='hisauhfus'
# print(a)
# print(a[2:5])
# print(a[3])
# print(a[3:])
# print(a[:4])
# print(a[1:200])
# print(a+' is cool')
# print('*'*50)
# print(a*3)
# print('t'in a)
# print('h'in a)
# print('h' not in a)
# print(a[::2])
# print(a[1::2])
# # print(a[-4:-1])
# # print(a[::-1])
# alist=[10,20,30,'niu','haha',[1,2]]
# print(len(alist))
# print(alist[2])
# print(alist[3:4])
# print(alist[4:])
# print(alist*3)
# print(20 in alist)
# print(10 not in alist)
# print(alist[::2])
# print(alist[1::2])
# alist[-1]=100
# print(alist)
# alist.append(200)
# print(alist)
#atuple=(11,22,33,44)
#print(atuple[-1])
#print(atuple[2:])
# adict={'name':'haha','age':13}
# print(adict)
# print(adict['name'])
# print(adict['age'])
# print(len(adict))
# print(13 in adict)
# print('name' in adict)
# adict['sex']='nan'
# adict['age']=19
# print(adict)
# words=['tom','haha','xixi']
# if 'tom' in words:
#     print('yes')
# if 'tom' not in words:
#     print('not in')
# else:
#     print('tom in words')
# if -0.0:
#     print('ok')
# if -0.01:
#     print('0.01 is ok')
# if ' ':
#     print('space is ok')
# if '':
#     print('is false')
# if 1>2:
#     print('haha')
# else:
#     print('xixi')
# if 1<2:
#     print('haha')
# else:
#     print('xixi')
# if not None:
#     print('hehoe')
# import getpass
# a=input('请输入用户名：')
# b=getpass.getpass('请输入密码：')
# if a=='bob' and b=='123456':
#     print('Login successful')
# else:
#     print('Login incorrect')
# import random
# a=random.randint(1,100)
# print(a)
# b=int(input('猜数1～100：'))
# if a>b:
#     print('xiaole')
# elif a<b:
#     print('dale')
# else:
#     print('duile')
# a=100
# b=80
# if a<b:
#     smaller=a
#     print(smaller)
# else:
#     smaller=b
#     print(smaller)
# smaller=a if a<b else b
# print(smaller)
# a=int(input('请输入成绩：'))
# if a>=90:
#     print('优秀')
# elif 80<=a<90:
#     print('好')
# elif 70<=a<80:
#     print('良')
# elif 60<=a<70:
#     print('及格')
# else:
#     print('你要努力了')
# a=int(input('请输入成绩：'))
# if a>=90:
#     print('优秀')
# elif 80<=a:
#     print('好')
# elif 70<=a:
#     print('良')
# elif 60<=a:
#     print('及格')
# else:
#     print('你要努力了')
# import random
# a=input('请输入：')
# b=random.choice(['剪刀','石头','布'])
# if a=='剪刀':
#     if b=='剪刀':
#         print('平局')
#     elif b=='石头':
#         print('机器赢')
#     else:
#         print('你赢了')
# elif a=='石头':
#     if b=='剪刀':
#         print('你赢了')
#     elif b=='石头':
#         print('平局')
#     else:
#         print('机器赢')
# else:
#     if b=='剪刀':
#         print('机器赢')
#     elif b=='石头':
#         print('你赢了')
#     else:
#         print('平局')
# import random
# all_choice=['石头','剪刀','布']
# win_list=[['石头','剪刀'],['剪刀','布'],['布','石头']]
# computer=random.choice(all_choice)
# player=input('请出拳:')
# print(computer)
# if player==computer:
#     print('pingju')
# elif [player,computer] in win_list:
#     print('niyingle')
# else:
#     print('diannaoying')
# import random
# all_choice=['石头','剪刀','布']
# win_list=[['石头','剪刀'],['剪刀','布'],['布','石头']]
# prompt='''(0)石头
# (1)剪刀
# (2)布
# 请出拳(0/1/2)：'''
# computer=random.choice(all_choice)
# index=int(input(prompt))
# player=all_choice[index]
# if player==computer:
#     print('pingju')
# elif [player,computer] in win_list:
#     print('niyingle')
# else:
#     print('diannaoying')
# sum100=0
# counter=1
# while counter<=100:
#     sum100=sum100+counter
#     counter=counter+1
# print(sum100)
# import random
# a=random.randint(1,100)
# running=True
# while running:
#     b=int(input('请输入1~100：'))
#     if a>b:
#         print('小了')
#     elif a<b:
#         print('大了')
#     else:
#         print('对了')
#         running=False
# import random
# a=random.randint(1,100)
# while True:
#     b=int(input('请输入1~100：'))
#     if a>b:
#         print('小了')
#     elif a<b:
#         print('大了')
#     else:
#         print('对了')
#         break
# sum100=0
# counter=0
# while counter<100:
#     counter+=1
#     if counter%2:
#         continue
#     sum100+=counter
# print(sum100)
#a=input('请输入名字：')
#b=input('请输入密码：')
#if a=='bob' and b=='123456':
#    print('Login successful')
#else:
#    print('Login incorrect')

#import getpass
#a=input('请输入用户名：')
#b=getpass.getpass('请输入密码：')
#if a=='bob' and b=='123456':
#    print('Login successful')
#else:
#    print('Login incorrect')

#a=3
#b=4
#smaller=a if a>b else b
#print(smaller)

#a=int(input('请输入成绩：'))
#if a>=90:
#    print('优秀')
#elif a>=80:
#    print('好')
#elif a>=70:
#    print('良')
#elif a>=60:
#    print('及格')
#else:
#    print('你要努力了')

#import random
#jiqi=random.choice(['石头','剪刀','布'])
#a=input('请输入：')
#print(jiqi)
#if a=='石头': 
#    if jiqi=='石头':
#        print('平')
#    elif jiqi=='剪刀':
#        print('胜')
#    else:
#        print('输')
#if a=='剪刀':
#    if jiqi=='剪刀':
#        print('平')
#    elif jiqi=='布':
#        print('胜')
#    else:
#        print('输')
#if a=='布':
#    if jiqi=='布':
#        print('平')
#    elif jiqi=='石头':
#        print('胜')
#    else:
#        print('输')

#import random
#qb=['剪刀','石头','布']
#sqb=[['剪刀','布'],['石头','剪刀'],['布','石头']]
#jq=random.choice(qb)
#a='''0剪刀
#1石头
#2布
#请输入0/1/2：'''
#b=int(input(a))
#c=qb[b]
#print(jq)
#if c==jq:
#    print('平')
#elif [c,jq] in sqb:
#    print('胜')
#else:
#    print('败')

#import random 
#a=random.randint(1,100)
#print(a)
#c=True
#while c:
#    b=int(input('请输入1～100数：'))
#    if a>b:
#        print('小了')
#    elif a<b:
#        print('大了')
#    else:
#        print('对了')
#        c=False

#import random
#a=random.randint(1,100)
#print(a)
#i=0
#while i<5:
#    b=int(input('请输入1～100的数：'))
#    if a<b:
#        print('大了')
#    elif a>b:
#        print('小了')
#    else:
#        print('对了')
#        break
#    i+=1
#else:
#    print(a)

#a=int(input('请输入成绩：'))
#if a>=90:
#    print('优秀')
#elif a>=80:
#    print('好')
#elif a>=70:
#    print('良')
#elif a>=60:
#    print('及格')
#else:
#    print('你要努力了')

#import random
#jiqi=random.choice(['石头','剪刀','布'])
#a=input('请输入：')
#print(jiqi)
#if a=='石头': 
#    if jiqi=='石头':
#        print('平')
#    elif jiqi=='剪刀':
#        print('胜')
#    else:
#        print('输')
#if a=='剪刀':
#    if jiqi=='剪刀':
#        print('平')
#    elif jiqi=='布':
#        print('胜')
#    else:
#        print('输')
#if a=='布':
#    if jiqi=='布':
#        print('平')
#    elif jiqi=='石头':
#        print('胜')
#    else:
#        print('输')

#import random
#qb=['剪刀','石头','布']
#sqb=[['剪刀','布'],['石头','剪刀'],['布','石头']]
#jq=random.choice(qb)
#a='''0剪刀
#1石头
#2布
#请输入0/1/2：'''
#b=int(input(a))
#c=qb[b]
#print(jq)
#if c==jq:
#    print('平')
#elif [c,jq] in sqb:
#    print('胜')
#else:
#    print('败')

#import random 
#a=random.randint(1,100)
#print(a)
#c=True
#while c:
#    b=int(input('请输入1～100数：'))
#    if a>b:
#        print('小了')
#    elif a<b:
#        print('大了')
#    else:
#        print('对了')
#        c=False

#import random
#a=random.randint(1,100)
#print(a)
#i=0
#while i<5:
#    b=int(input('请输入1～100的数：'))
#    if a<b:
#        print('大了')
#    elif a>b:
#        print('小了')
#    else:
#        print('对了')
#        break
#    i+=1
#else:
#    print(a)

#import random
#f=['剪刀','石头','布']
#b=[['剪刀','布'],['石头','剪刀'],['布','石头']]
#c='''0剪刀
#1石头
#2布
#请输入0/1/2:'''
#i=0
#j=0
#while i<3:
#    a=random.choice(['剪刀','石头','布'])
#    print(a)
#    d=int(input(c))
#   e=f[d]
#    if [e,a] in b:
#        print('胜')
#        j+=1
#    i+=1
#if j<2:
#    print('失败')
#else:
#    print('成功')

#import random
#all_choices = ['石头', '剪刀', '布']
#win_list = [['石头', '剪刀'], ['剪刀', '布'], ['布', '石头']]
#prompt = """(0) 石头
#(1) 剪刀
#(2) 布
#请选择(0/1/2): """
#cwin = 0
#pwin = 0
#while cwin < 2 and pwin < 2:
#    computer = random.choice(all_choices)
#    ind = int(input(prompt))
#    player = all_choices[ind]
#    print("Your choice: %s, Computer's choice: %s" % (player, computer))
#    if player == computer:
#        print('\033[32;1m平局\033[0m')
#    elif [player, computer] in win_list:
#        pwin += 1
#        print('\033[31;1mYou WIN!!!\033[0m')
#    else:
#        cwin += 1
#        print('\033[31;1mYou LOSE!!!\033[0m')

import random
f=['剪刀','石头','布']
b=[['剪刀','布'],['石头','剪刀'],['布','石头']]
c='''0剪刀
1石头
2布
请输入0/1/2:'''
i=0
j=0
while i<3:
    a=random.choice(['剪刀','石头','布'])
    print(a)
    d=int(input(c))
    e=f[d]
    if [e,a] in b:
        print('胜')
        j+=1
    i+=1
if j<2:
    print('失败')
else:
    print('成功')





























































