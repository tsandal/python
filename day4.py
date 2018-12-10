#import random
#all_cha='!@#$%^&*?0123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
#result=''
#for i in range(8):
#    ch=random.choice(all_cha)
#    result+=ch
#print(result)

# import random
# import string
# all_cha=string.ascii_letters+string.digits
# def randpass(n=8):
#     result=''
#     for i in range(n):
#         ch=random.choice(all_cha)
#         result+=ch
#     return result
# if __name__=='__main__':
#     a=randpass()
#     print(a)
#     print(randpass(4))
# import shutil
# f1=open('/etc/hosts')
# f2=open('/tmp/zj.txt','w')
# shutil.copy('/etc/hosts','/tmp/aa.txt')
# shutil.copyfile('/etc/hosts','/tmp/ab.txt')
# shutil.copy2('/etc/hosts','/tmp/ac.txt')
# shutil.copytree('/etc/hosts','/tmp/ad.txt')
# shutil.move('/tmp/aa.txt','/var/tmp/')
# shutil.rmtree('/tmp/aa.txt')
# shutil.chown('/tmp/passwd',user='student',group='student')
# help(shutil.rmtree)

# x=y=10
# print(id(x))
# print(id(y))
# x=20
# print(id(x))
# a=b=[10,20]
# print(id(a))
# print(id(b))
# a=[100,20]
# print(id(a))
# print(id(b))

# import keyword
# print(keyword.kwlist)
# print(keyword.iskwlist('len'))
# print('for' in keyword.kwlist)
# print('len' in keyword.kwlist)
# while True:
#     filename=input('请输入文件名：')
#     if not
# import os
# def get_fname():
#     while True:
#         filename=input('请输入文件名：')
#         if not os.path.exists(filename):
#             break
#         print('已存在%s'%filename)
#     return filename
# def get_content():
#     contents=[]
#     while True:
#         line=input('("end" to quit)>')
#         if line == 'end':
#             break
#         contents.append(line)
#     return contents
# def wfile(filename,contents):
#     with open(filename,'w') as fobj:
#         fobj.writelines(contents)
# if __name__ == '__main__':
#     fname=get_fname()
#     content=get_content()
#     wfile(fname,contents)
# import os
# def get_fname():
#     while True:
#         filename = input('请输入文件名：')
#         if not os.path.exists(filename):
#             break
#         print('%s 已存在，请重试。' % filename)
#     return filename
# def get_contents():
#     contents = []
#     print('请输入内容，结束请输入end。')
#     while True:
#         line = input('> ')
#         if line == 'end':
#             break
#         contents.append(line)
#     return contents
# def wfile(fname, contents):
#     with open(fname, 'w') as fobj:
#         fobj.writelines(contents)
# if __name__ == '__main__':
#     fname = get_fname()
#     contents = get_contents()
#     contents = ['%s\n' % line for line in contents]
#     wfile(fname, contents)

# import random
# import string
# a=string.ascii_letters+string.digits
# b=''
# for i in range(8):
#     c=random.choice(a)
#     b+=c
# print(b)

# import os
# def get_fname():
#     while True:
#         filename = input('请输入文件名：')
#         if not os.path.exists(filename):
#             break
#         print('%s 已存在，请重试。' % filename)
#     return filename
# def get_contents():
#     contents = []
#     print('请输入内容，结束请输入end。')
#     while True:
#         line = input('> ')
#         if line == 'end':
#             break
#         contents.append(line)
#     return contents
# def wfile(fname, contents):
#     with open(fname, 'w') as fobj:
#         fobj.writelines(contents)
# if __name__ == '__main__':
#     fname = get_fname()
#     contents = get_contents()
#     contents = ['%s\n' % line for line in contents]
#     wfile(fname, contents)

# alist=[10,20,30,40]
# print(max(alist))
# names=['tom','lisi','hahhaha']
# print(max(names))
# print(min(names))
#
# hi='hello'
# alist=[10,20,30]
# for i in range(len(hi)):
#     print(i,hi[i])
# for a,b in enumerate(alist):
#     print(a,b)

# hi='hello'
# alist=[10,20,30,40]
# for i in range(len(hi)):
#     print(i,hi[i])
# for a,b in enumerate(alist):
#     print(a,b)

# alist=[12,55,234,2,54,87,43,24,745,21]
# for i in reversed(alist):
#     print(i)
# print(sorted(alist))
# for a in sorted(alist):
#     print(a)
# print(list(reversed(alist)))
# print(sorted(alist))
#
# for i in reversed(alist):
#     print(i)

# import string
# import keyword
# first_chs=string.ascii_letters+'_'
# all_chs=first_chs+string.digits
# def check_id(idt):
#     if keyword.iskeyword(idt):
#         return '%s是关键字'%idt
#     if idt[0] not in first_chs:
#         return '首字符不合法'
#     for ind,ch in enumerate(idt[1:]):
#         if ch not in all_chs:
#             return '第%s个字符不合法'%(ind+2)
#     return '%s是合法的标示符'%idt
# if __name__ == '__main__':
#     idt=input('请输入字符串:')
#     print(check_id(idt))

# import string
# import keyword
# first_chs = string.ascii_letters + '_'
# all_chs = first_chs + string.digits
# def check_id(idt):   # abc@123
#     if idt[0] not in first_chs:
#         return '第一个字符不合法'
#     for ind, ch in enumerate(idt[1:]):  # bc@123 [(0, b), (1, c)...]
#         if ch not in all_chs:
#             return '第%s个字符%s非法' % (ind+2, ch)
#     if keyword.iskeyword(idt):
#         return '%s是关键字，不能作为自定义的标识符' % idt
#     return '%s是合法的标识符' % idt
# if __name__ == '__main__':
#     idt = input('请输入待检查的标识符：')
#     print(check_id(idt))

# print('%s:%s'%('bob',22))
# print('%sx%s=%s'%(2,3,6))
# print('%5sx%5s=%5s'%(3,4,12))
# print('%s:%d'%('bob',21))
# print('%-5s%-5s'%('bob',22))
# print('%5s%5s'%('bob',22))
# print('%s:%d'%('bob',0000))

# print('{}:{}'.format('bob',22))
# print('{}:{}'.format(22,'bob'))
# print('{1}:{0}'.format(22,'bob'))
# print('{0[1]}:{0[0]}'.format([22,'bob']))

# import sys
# import subprocess
# import randpass2
# def adduser(username,fname):
#     info="""用户信息：
# 用户名：%s
# 密码：%s
# """%(username,password)
#     subprocess.call('useradd%s'%username,shell=True)
#     subprocess.call(
#         'echo %s | passwd --stdin %s'%(password,username),
#         shell=True
#     )
#     with open(fname,'a') as fobj:
#         fobj.write(info)
# if __name__ == '__main__':
#     password=randpass2.randpass()
#     fname='/tmp/mima.txt'
#     adduser(sys.argv[1],password,fname)

# hi='    hello    '
# print(hi.upper())
# h='HELLO'
# print(h.lower())
# print(hi.strip())
# print(hi.lstrip())
# print(hi.rstrip())
# print(hi.replace('l','m'))
# print(hi.center(50))
# print(hi.center(50,'*'))
# print(hi.ljust(50,'*'))
# print(hi.rjust(50,'*'))
# print(hi.startswith(' '))
# print(hi.endswith('abc'))

# import sys
# import subprocess
# import randpass2
# def adduser(username,fname):
#     info="""用户信息：
# 用户名：%s
# 密码：%s
# """%(username,password)
#     subprocess.call('useradd%s'%username,shell=True)
#     subprocess.call(
#         'echo %s | passwd --stdin %s'%(password,username),
#         shell=True
#     )
#     with open(fname,'a') as fobj:
#         fobj.write(info)
# if __name__ == '__main__':
#     password=randpass2.randpass()
#     fname='/tmp/mima.txt'
#     adduser(sys.argv[1],password,fname)
#完美
# import sys
# import subprocess
# from randpass2 import randpass
# def add_user(username, password, fname):
#     info = """user information:
# username: %s
# password: %s
# """
#     subprocess.call('useradd %s' % username, shell=True)
#     subprocess.call(
#         'echo %s | passwd --stdin %s' % (password, username),
#         shell=True
#     )
#     with open(fname, 'a') as fobj:
#         fobj.write(info % (username, password))
# if __name__ == '__main__':
#     username = sys.argv[1]
#     password = randpass()
#     fname = '/tmp/users.txt'
#     add_user(username, password, fname)

# atuple=(10,20,30,[1,2,3])
# print(atuple.count(20))    #统计有几个20
# print(atuple.count(200))
# print(atuple.index(20))    #第一个20的下标
# atuple[-1].append(4)
# print(atuple)
# atuple[-1][0]=100

# a=(10,)
# print(a)
# print(len(a))
# b=(10)       #不代表元祖
# print(b)
# print(len(b))   #报错

# import os
# def get_fname():
#     while True:
#         filename=input('请输入文件名：')
#         if os.path.exists(filename):
#             print('已存在,请重试')
#         else:
#             break
#     return filename
# def get_contents():
#     contents=[]
#     print('请输入内容，结束请输入end')
#     while True:
#         line=input('>')
#         if line=='end':
#             break
#         contents.append(line)
#     return contents
# def wfile(fname,contents):
#     with open(fname,'w') as fobj:
#         fobj.writelines(contents)
# if __name__ == '__main__':
#     fname=get_fname()
#     contents=get_contents()
#     contents = ['%s\n' % line for line in contents]
#     wfile(fname,contents)

#print([i**i for i in range(3)])

# import sys
# import subprocess
# import randpass2
# def add_user(username,password,fname):
#     info="""user information
# username%s
# password%s"""%(username,password)
#     subprocess.call('useradd %s'%username,shell=True)
#     subprocess.call('echo %s | passwd --stdin %s'%(password,username),shell=True)
#     with open(fname,'a') as fobj:
#         fobj.write(info % (username,password))
# if __name__ == '__main__':
#     username=sys.argv[1]
#     password=randpass2.randpass()
#     fname='/tmp/users.txt'
#     add_user(username,password,fname)

# import sys
# import subprocess
# from randpass2 import randpass
# def add_user(username, password, fname):
#     info = """user information:
# username: %s
# password: %s
# """
#     subprocess.call('useradd %s' % username, shell=True)
#     subprocess.call(
#         'echo %s | passwd --stdin %s' % (password, username),
#         shell=True
#     )
#     with open(fname, 'a') as fobj:
#         fobj.write(info % (username, password))
# if __name__ == '__main__':
#     username = sys.argv[1]
#     password = randpass()
#     fname = '/tmp/users.txt'
#     add_user(username, password, fname)

# import sys
# import subprocess
# import randpass2
# def add_user(username,password,fname):
#     info="""user information:
# username:%s
# password:%s
# """
#     subprocess.call('useradd %s'%username,shell=True)
#     subprocess.call('echo %s | passwd --stdin %s'%(password,username),shell=True)
#     with open(fname,'a') as fobj:
#         fobj.write(info % (username,password))
# if __name__ == '__main__':
#     username=sys.argv[1]
#     password=randpass2.randpass()
#     fname='/tmp/users.txt'
#     add_user(username,password,fname)

# from mktxtfile import get_contents
# width = 48
# contents = get_contents()
# print('+%s+' % ('*' * 48))
# for line in contents:
#     print('+{:^48}+'.format(line))
# print('+%s+' % ('*' * 48))

# >>> import shutil
# >>> f1 = open('/etc/hosts')
# >>> f2 = open('/tmp/zj.txt', 'w')
# >>> shutil.copyfileobj(f1, f2)    # copy文件对象
# >>> f1.close()
# >>> f2.close()
# >>> shutil.copyfile('/etc/hosts', '/tmp/abcd.txt')   # copy文件名
# >>> shutil.copy('/etc/hosts', '/tmp/aaaa.txt')   # 目标可能是目录
# >>> shutil.copy('/etc/passwd', '/tmp/')
# >>> shutil.copy2('/etc/passwd', '/tmp/')   # 相当于cp -p
# >>> shutil.copytree('/etc/security', '/tmp/anquan')  # cp -r
# >>> shutil.move('/tmp/zj.txt', '/var/tmp/')  # mv
# >>> shutil.rmtree('/tmp/anquan')   # rm -rf
# >>> shutil.rmtree('/var/tmp/zj.txt')   # 不能删除单个文件
# >>> import os
# >>> os.remove('/var/tmp/zj.txt')
# >>> shutil.chown('/tmp/passwd', user='bob', group='bob')
# >>> help(shutil.rmtree)
#
# >>> x = y = 10
# >>> id(x)
# 9348224    # 显示变量在内存的地址
# >>> id(y)
# 9348224
# >>> x = 20
# >>> id(x)
# 9348544
# >>> y       # y的值不变
# >>> a = b = [10, 20]
# >>> id(a)
# 140225192670152
# >>> id(b)
# 140225192670152
# >>> a[0] = 100
# >>> a
# [100, 20]
# >>> b
# [100, 20]
#
# >>> a, b = 10, 20   # 相当于是a=10; b=20
# >>> a
# 10
# >>> b
# 20
# >>> a, b = b, a     # a和b的值互换
#
# 标识符：就是个名字，包括变量、模块、类、函数
#
# 关键字
# >>> import keyword
# >>> keyword.kwlist
# >>> keyword.iskeyword('len')
# >>> 'for' in keyword.kwlist
#
# http://yiyibooks.cn/ -> python352文档 -> 库参考
#
#
# 编写程序的流程、步骤：
# 1、发呆、思考：在脑海里像过电影一样，想想程序是怎么运行的（交互的？非交互的？）
# 交互的：考虑屏幕上提示什么，用户回答什么
# 2、思考程序有哪些功能。将这些功能创建函数，编写程序框架
# def get_fname():
#
#
# def get_content():
#
#
# def wfile(fname, content):
#
#
# if __name__ == '__main__':
#     fname = get_fname()
#     content = get_content()
#     wfile(fname, content)
# 3、完成函数代码
#
# >>> names = ['bob', 'alice', 'tom']
# >>> max(names)
# >>> min(names)
#
#
#
# 字符串格式化
# '' % ()
# >>> '%s: %s' % ('bob', 22)   # %s / %d 常用
# >>> '%s: %d' % ('bob', 22)
# >>> '97 is %c' % 97   # %c转换数字成为对应的ascii码，了解
# >>> '97 is %#o' % 97  # 不常用
# >>> '97 is %#x' % 97  # 不常用
# >>> '10000 is %e' % 10000  # 不常用
# >>> '10/3 is %f' % (10 / 3)  # 不常用
# >>> '10/3 is %d' % (10 / 3)
# >>> '%10s%10s' % ('name', 'age')   # 常用，定义字段宽度为10个字节
# >>> '%-10s%-10s' % ('name', 'age')   # 常用，左对齐
#
# >>> '{}: {}'.format('bob', 22)
# 'bob: 22'
# >>> '{}: {}'.format(22, 'bob')
# '22: bob'
# >>> '{1}: {0}'.format(22, 'bob')
# 'bob: 22'
# >>> '{0[1]}: {0[0]}'.format([22, 'bob'])

import string
import keyword
first_chs = string.ascii_letters + '_'
all_chs = first_chs + string.digits
def check_id(idt):   # abc@123
    if idt[0] not in first_chs:
        return '第一个字符不合法'
    for ind, ch in enumerate(idt[1:]):  # bc@123 [(0, b), (1, c)...]
        if ch not in all_chs:
            return '第%s个字符%s非法' % (ind+2, ch)
    if keyword.iskeyword(idt):
        return '%s是关键字，不能作为自定义的标识符' % idt
    return '%s是合法的标识符' % idt
if __name__ == '__main__':
    idt = input('请输入待检查的标识符：')
    print(check_id(idt))








































