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
#    d=int(input(c))
#    e=f[d]
#    if [e,a] in b:
#        print('胜')
#        j+=1
#    i+=1

# import random
# all_choices = ['石头', '剪刀', '布']
# win_list = [['石头', '剪刀'], ['剪刀', '布'], ['布', '石头']]
# prompt = """(0) 石头
# (1) 剪刀
# (2) 布
# 请选择(0/1/2): """
# cwin = 0
# pwin = 0
# while cwin < 2 and pwin < 2:
#     computer = random.choice(all_choices)
#     ind = int(input(prompt))
#     player = all_choices[ind]
#     print("Your choice: %s, Computer's choice: %s" % (player, computer))
#     if player == computer:
#         print('\033[32;1m平局\033[0m')
#     elif [player, computer] in win_list:
#         pwin += 1
#         print('\033[31;1mYou WIN!!!\033[0m')
#     else:
#         cwin += 1
#         print('\033[31;1mYou LOSE!!!\033[0m')

# py_str='Python'
# alist=['杜场所','说的话','长孙']
# atuple=('徐三年','撒谎')
# adict={'张第':'上海','里斯':'南京'}
# for ch in py_str:
#     print(ch)
# for name in alist:
#     print(name)
# for name in atuple:
#     print(name)
# for key in adict:
#     print(key,adict[key])

# print(list(range(10)))
# print(list(range(6,11)))
# print(list(range(1,11,2)))
# print(list(range(10,0,-1)))
#
# sum100=0
# for i in range(0,101):
#     sum100+=i
# print(sum100)

#fib=[0,1]
#for i in range(8):
#    fib.append(fib[-1]+fib[-2])
#print(fib)

#fid=[0,1]
#for i in range(11):
#    fid.append(fid[-1]+fid[-2])
#print(fid)
#
# fib=[0,1]
# for i in range(13):
#     fib.append(fib[-1]+fib[-2])
# print(fib)

#for i in range(1,10):
#    for j in range(1,i+1):
#        print('%sx%s=%s'%(j,i,i*j),end=' ')
#    print()

#for i in range(1,10):
#    for j in range(1,i+1):
#        print('%sx%s=%s'%(j,i,j*i),end=' ')
#    print()

#print([10 for i in range(11)])
#print([10+5 for j in range(12)])
#print(['192.168.1.'+str(k) for k in range(1,255)])

#f=open('/tmp/zhuji')
#data=f.readline()
#data=f.readline()
#data=f.readline()
#f.close()
#data=f.readlines()
#data=f.close()
#data=f.readline()
#data=f.read(22)
#data=f.readline()
#data=f.readlines()
#print(data)

#f=open('/bin/ls','rb')
#data=f.read(10)
#f.close()
#print(data)

#f=open('/tmp/zhuji','w')
#data=f.write('hello world1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111\n')
#f.flush()
#print(data)

#f=open('/tmp/zhuji','a')
#for i in range(8):
#    f.write('new line\n')
#f.close

#f=open('/tmp/zhuji','r+')    #读写方式打开
#f.write('abcde')             #abcde将会在开头把源文件的前5个字符覆盖    
#f.flush()                    
#f.tell()                     #获取文件指针位置
#f.read(8)                    #从文件指针开始的位置向后读8个字节
#f.seek(3,0)                  #将文件指针移动到开头偏移3个字节
#f.read(2)                    #度文件第4.5个字符
#f.seek(0,2)                  #移动指针到文件结尾   
#f.write('my test\n')
#f.flush()
#f.read()
#f.seek(0,0)
#f.readline()
#f.close()

#with open('/tmp/zhuji') as f:
#line=f.readline()
#print(line)

#with open('/tmp/zhuji') as f:
#for line in f:
#    print(line,end='')

#f1=open('/bin/ls','rb')
#f2=open('/root/ls','wb')
#data=f1.read()
#f2.write(data)
#f1.close()
#f2.close()

#f1=open('/bin/ls','rb')
#f2=open('/root/ls','wb')
#data=f1.read()
#f2.write(data)
#f1.close
#f2.close

#src_fname='/bin/ls'
#dst_fname='/tmp/list'
#src_fobj=open(src_fname,'rb')
#dst_fobj=open(dst_fname,'wb')
#while True:
#    data=src_fobj.read(4096)
#    if not data:
#        break
#    dst_fobj.write(data)
#src_fobj.close()
#dst_fobj.close()

#src_fname='/bin/ls'
#dst_fname='/tmp/list'
#with open(src_fname,'rb') as src_fobj:
#    with open(dst_fname,'wb') as dst_fobj:
#        while True:
#            data=src_fobj.read(4096)
#            if not data:
#                break
#            dst_fobj.write(data)

#def sc_fib():
#    fib=[0,1]
#    for i in range(8):
#        fib.append(fib[-1]+fib[-2])
#    print(fib)
#sc_fib()
#sc_fib()
#sc_fib()
#sc_fib()
#sc_fib()
#sc_fib()
#sc_fib()
#sc_fib()
#sc_fib()
#sc_fib()
#sc_fib()
#sc_fib()
#sc_fib()
#sc_fib()

#a=sc_fib()
#print(a)    #函数没有return,默认返回none

#def sc_fib():
#    fib=[0,1]
#    for i in range(8):
#        fib.append(fib[-1]+fib[-2])
#    return(fib)
#a=sc_fib()
#print(a)
#b=[i * 2 for i in a]
#c=[a for i in a]
#print(b)
#print(c)

#def sc_fib(n):
#    fib=[0,1]
#    for i in range(n-2):
#        fib.append(fib[-1]+fib[-2])
#    return fib
#a=sc_fib(10)
#print(a)
#b=sc_fib(20)
#print(b)
#x=int(input('length:'))
#c=sc_fib(x)
#print(c)

#def sc_fib(n):
#    fib=[0,1]
#    for i in range(n-2):
#        fib.append(fib[-1]+fib[-2])
#    return fib
#print(sc_fib(10))
#a=sc_fib(4)
#print(a)
#b=sc_fib(20)
#print(b)
#x=int(input('length:'))
#c=sc_fib(x)
#print(c)

#import sys
#def copy(src_fname,dst_fname):
#    src_fobj=open(src_fname,'rb')
#    dst_fobj=open(dst_fname,'wb')
#    while True:
#        data=src_fobj.read(4096)
#        if not data:
#            break
#        dst_fobj.write(data)
#copy(sys.argv[1],sys.argv[2])

#open('/tmp/zhuji','r+')    #读写方式打开
#f.write('abcde')             #abcde将会在开头把源文件的前5个字符覆盖    
#f.flush()                    
#f.tell()                     #获取文件指针位置
#f.read(8)                    #从文件指针开始的位置向后读8个字节
#f.seek(3,0)                  #将文件指针移动到开头偏移3个字节
#f.read(2)                    #度文件第4.5个字符
#f.seek(0,2)                  #移动指针到文件结尾   
#f.write('my test\n')
#f.flush()
#f.read()
#f.seek(0,0)
#f.readline()
#f.close()

#with open('/tmp/zhuji') as f:
#line=f.readline()
#print(line)

#with open('/tmp/zhuji') as f:
#for line in f:
#    print(line,end='')

#f1=open('/bin/ls','rb')
#f2=open('/root/ls','wb')
#data=f1.read()
#f2.write(data)
#f1.close()
#f2.close()

#f1=open('/bin/ls','rb')
#f2=open('/root/ls','wb')
#data=f1.read()
#f2.write(data)
#f1.close
#f2.close

#def pstar(n=30):
#    print('*' * n)
#pstar()
#pstar(50)

import random
import string
all_chs = string.digits + string.ascii_letters
def gen_pass(n=8):
    result = ''
    for i in range(n):
        ch = random.choice(all_chs)
        result += ch
    return result
if __name__ == '__main__':
    print(gen_pass())
    print(gen_pass(4)) 
























