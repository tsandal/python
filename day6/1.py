# adict={'name':'bob','age':22}
# bdict=dict(['ab','bc',('name','niu')])
# print(bdict)
# c={}.fromkeys(('boo','haha'),22)
# print(c)
# for key in adict:
#     print('%s:%s'%(key,adict[key]))
# d='%(name)s is %(age)s years old'%adict
# print(d)
# adict.keys()
# for key in adict.keys():
#     print(key)
# for key in adict:
#     print(key)
# list(adict.values())
# for key,val in adict.items():
#     print('%s:%s'%(key,val))
# print(adict.get('phone'))      #获取KEY为phone的值
# adict.get('phone','110')       #没有返回110
# e=adict.popitem()              #随机弹出一项
# #adict.pop('email')           #弹出KEY是email的项
# adict.update({'aaa':11,'bbb':22})
# print(e)

# aset=set('hello')
# print(aset)
# print(len(aset))
# for ch in aset:
#     print(ch)
# bset=set('how')
# print(aset | bset)
# print(aset & bset)
# print(aset - bset)
# print(aset.add('new'))
# print(aset.update(['hello','ll']))
# cset=set('ho')
# print(cset.issubset(aset))           #cset是aset的子集吗
# print(aset.issuperset(cset))         #aset是cset的超集吗
# print(aset.intersection(bset))       #aset & bset
# print(aset.union(bset))              #aset | bset
# print(aset.difference(bset))         #aset - bset
#
#
# ###过滤公司网站访问相同的url
# cp /etc/passwd /tmp
# cp /etc/passwd /tmp/mima
# with open('/tmp/mima') as f:
#     aset=set(f)
# with open('/tmp/passwd') as f:
#     bset=set(f)
# with open('/tmp/result.txt','w') as f:
#     f.writelines(aset - bset)


#######time模块
# import time
# print(time.time())      #时间戳
# print(time.ctime())     #当前时间
# print(time.localtime()) #返回九元祖格式时间
# time.sleep(2)
# print(time.strftime('%Y-%m-%d %H:%M:%S'))
#
# time.time()
# time.ctime()
# time.localtime()
# time.sleep(3)
# time.strftime('%Y-%m-%d %H:%M:%S')
#
# #######datetime模块
# from datetime import datetime,timedelta
# t1=datetime.now()
# print(t1.year)
# print(t1.month)
# print(t1.day)
# print(t1.hour)
# print(t1.minute)
# print(t1.second)
# print(t1.microsecond)
# t2=datetime(2018,10,10)
# t1=datetime.strptime('Dec 12 2018','%b %d %Y')  #转换字符串为datetime对象
# t=datetime(2018,12,10)
# print(t1>t)
#
# t1=datetime.now()
# days=timedelta(days=100)
# t3=t1-days      #100天前的时间
# t4=t1+days      #100天后的时间
# print(t3)
# print(t4)

# ########异常
# try:
#     num=int(input('number:'))
#     result=100/num
# except (ZeroDivisionError,ValueError):
#     print('无效输入,必须输入非0数字')
# except (KeyboardInterrupt,EOFError):
#     print('\nbye-bye')
# else:
#     print(result)
# finally:
#     print('DONE')

#########自定义主动抛出异常
#def set_age(name,age):
    # if not 0<age<150:
    #     raise ValueError('年龄超过范围了(1-150)')
    # print('%s现在是%s岁了'%(name,age))
# def set_age2(name,age):
#     assert 0<age<150,'年龄超过范围了(1-150)'
#     print('%s现在是%s岁了' % (name, age))
# if __name__ == '__main__':
#  #   set_age('haha',31)
#     set_age2('xix',211)

##########os模块
# import os
# print(os.getcwd())        #pwd
# os.mkdir('/tmp/kk')       #mkdir /tmp/kk
# os.chdir('/tmp/kk')       #cd /tmp/kk
# os.listdir()              #ls
# os.listdir('/home')       #ls /home
# os.mknod('mytest.txt')    #touch mytest.txt
# os.symlink('/etc/hosts','zhuji')   #ln -s /etc/hosts zhuji
# os.chmod('mytest.txt',0o644)       #chmod 644 mytest.txt
# os.rename('mytest.txt','test.doc')  #mv mytest.txt test.doc
# os.listdir()      #ls
# os.remove('zhuji')     #rm -f zhuji
# os.rmdir('/tmp/devop')    #删除空目录
# os.path.split('/etc/sysconfig/network')
# os.path.basename('/etc/sysconfig/network')
# os.path.dirname('/etc/sysconfig/network')
# os.path.join('/etc/sysconfig','network')
# os.path.isfile('/etc/hosts')
# os.path.isdir('/etc/hosts')
# os.path.exists('/etc/hosts')     #是否存在
# os.path.islink('/etc/hosts')     #是链接吗

# ##########pickle模块
# f=open('/tmp/mydata','w')
# f.write('hello world\n')
# f.write(1000)    #不允许写入数字
# f.write({'name':'tom'})    #不允许写入字典
#
# import pickle as p      #导入模版时取别名
# f=open('/tmp/data','wb')
# adict={'name':'bob','age':22}
# p.dump(adict,f)
# f.close()
#
# import pickle as p
# f=open('/tmp/data','rb')
# mydict=p.load(f)
# f.close()
# print(mydict)
# print(mydict['age'])

adict={'name':'tom','age':22}
bdict=dict((['name','bob'],['age',23]))
print(bdict)
cdict={}.fromkeys(('bob','alice'),23)
print(cdict)

for each_key in adict:
    print'key=%s,value=%s'%(each_key,adict[each_key])
    print('%(name)s'%adict)
print adict
adict['age']=22
print(adict)
adict['email']='bob@tarena.com.cn'
print adict

del adict['email']
print(adict)
adict.pop('age')
print(adict)
adict.clear()
print(aDict)


























































































