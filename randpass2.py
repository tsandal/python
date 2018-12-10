import random
import string
all_cha=string.ascii_letters+string.digits
def randpass(n=8):
    result=''
    for i in range(n):
        ch=random.choice(all_cha)
        result+=ch
    return result
if __name__=='__main__':
    a=randpass()
    print(a)

