from genericpath import isfile
import requests
import os
import sys
BASE_DIR = os.path.dirname(os.path.dirname(__file__)) #项目目录
sys.path.append(BASE_DIR)
import GlobalValue
UPLOAD_URL = GlobalValue.BACKEND_URL + "/acg/upload/" #上传目录
LOCAL_DIR = os.path.join(os.path.dirname(__file__),r'to_upload') #图片目录
ext=['jpg','bmp','png'] #只接受图片

to_uploads = []
for name in os.listdir(LOCAL_DIR):
    if (name.endswith('.jpg') or name.endswith('.PNG') or name.endswith('.png') or name.endswith('.jpeg')):
        to_uploads.append(os.path.join(LOCAL_DIR,name))
 
for name in to_uploads:
    files = {'img':open(name,'rb')}
    r = requests.post(url=UPLOAD_URL,data=None,files=files)
    files['img'].close()
    os.remove(name)
    


