from urllib.request import urlopen
html=urlopen('http://www.qq.com')
html.read(20)
#html=urlopen('http://www.qq.com')
with open('/tmp/qq.html','wb') as fobj:
    fobj.write(html.read())
