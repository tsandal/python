import tarfile
import zipfile
import os
import shutil
import yaml
pwd1=os.getcwd()
if os.path.exists(pwd1+'/tar'):
    shutil.rmtree(pwd1+'/tar')
os.mkdir(pwd1+'/tar')
tar=tarfile.open("nginx-1.12.2.tar.gz","r")
tar.extractall(pwd1+'/tar/')
tar.close()
zip=zipfile.ZipFile("RHCE-1806.zip","r")
zip.extractall(pwd1+'/tar/')
tar.close()