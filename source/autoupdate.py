import os
import urllib.request as request

baseurl = 'https://english-terminal.vercel.app/'
filelist = ['teste.py', 'outroteste.py']

def get_files():
    try:
        for filename in filelist:
            request.urlretrieve(baseurl, os.path.dirname(os.path.abspath(__name__))+'\\teste\\'+filename)
    except Exception as e:
        print(str(e))

if __name__ == '__main__':
    get_files()