# def get_age(name,age):
#     print('%s is %s years old'% (name,age))
# get_age()       #error
# get_age('bob',23,22)    #error
# get_age('tom',22)       #正确
# get_age(25,'bob')       #语法没有错误，语义不对
# get_age(age=25,name='tom')    #对的
# get_age(age=23,'bob')      #语法错误，key=val形式必须在后
# get_age(23,name='bob')      #error name得到多个值
# get_age('bob',age=23)      #对的

# def myfunc(*args):       # *标示args是个元祖
#     print(args)
# def myfunc2(**kwargs):   # **标示kwargs是字典
#     print(kwargs)
# if __name__ == '__main__':
#     myfunc()
#     myfunc(10)
#     myfunc(10,23)
#     myfunc(12,11,22,33)          #(12, 11, 22, 33)
#     myfunc2(name='tom')          #{'name': 'tom'}
#     myfunc2(name='bob',age=22)    #{'name': 'bob', 'age': 22}

# def add(x,y):
#     print(x+y)
# if __name__ == '__main__':
#     alist=[11,22]
#     add(*alist)          #调用函数时，参数加上*表示将序列对象拆开   33
#     add(*'ab')        #ab

#myadd(123)

# import tkinter
# from functools import partial
# root=tkinter.Tk()
# lb=tkinter.Label(root,text="hello world",font="Arial 20")
# b1=tkinter.Button(root,bg="blue",fg='while',text='Button 1')
# MyButton=partia

# def func1(n):
#     if n==1:
#         return  1
#     return n * func1(n-1)
# if __name__ == '__main__':
#     print(func1(5))

# ips=['192.168.1.%s'% i for i in range(1,255)]
# print(ips)
# hosts=('192.168.1.%s'% i for i in range(1,255))   #生成器
# for host in hosts:
#     print(host)

# def mygen():
#     yield 100
#     print('----------')
#     yield 200
#     print('##########')
#     yield 300
# a=mygen()

def file_block(fobj):































































































































