# import tkinter
# from functools import partial
# def pstar():
#     print('*'*20)
# def hello():
#     lb.config(text='hello world')
# def welcome():
#     lb.config(text='hello haha')
# root = tkinter.Tk()  # 相当于创建一个窗体
# lb = tkinter.Label(root, text="Hello World!", font="Arial 20")  # 创建label
# b1 = tkinter.Button(root, bg='blue', fg='white', text='Button 1')
# MyButton = partial(tkinter.Button, root, bg='blue', fg='white')
# b2 = MyButton(text='Button 2',command=hello)
# b3 = MyButton(text='Button 3',commond=welcome)
# b4 = MyButton(text='QUIT', command=root.quit)
# for item in [lb, b1, b2, b3, b4]:
#     item.pack()
#
# root.mainloop()


# def counter(start=0):
#     count=start
#     def incr():
#         nonlocal count
#         count+=1
#         return count
#     return incr
# a=counter()
# b=counter(10)
# print(a())        #1
# print(b())        #11

# def set_color(func):
#     def set_red():
#         return '\033[31;1m%s\033[0m' % func()
#     return set_red
#
# def hello():
#     return 'Hello World'
#
# @set_color
# def welcome():
#     return 'Hello China'
#
# @set_color
# def mytest():
#     a = 10 + 10
#     return a
#
# if __name__ == '__main__':
#     # print(hello())
#     # print(welcome())
#     hello = set_color(hello)
#     print(hello())
#     print(welcome())
#     print(mytest())

#import os
#import pickle
#import time

#time.time()
#os.path.isfile('/etc')

#hi='hello world'

# import hashlib
# with open('/etc/passwd','rb') as fobj:
#     data=fobj.read()
# m=hashlib.md5(data)
# a=m.hexdigest()
# print(a)

#import sys
#import hashlib
#def check_md5(fname):
#    m=hashlib.md5()
#    with open(fname,'rb') as fobj:
#        while True:
#            data=fobj.read(4096)
#            if not data:
#                break
#            m.update(data)
#    return m.hexdigest()
#if __name__ == '__main__':
#    print(check_md5(sys.argv[1]))

#walk的使用
#递归列出所有的文件
#list(os.walk('/tmp/demo/security'))
#for path,folders,files in os.walk('/tmp/demo/security'):
#    for file in files:
#        os.path.join(path,file)



























