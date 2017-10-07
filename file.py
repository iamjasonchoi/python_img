import os
from PIL import Image
class makidir(object):
    def __init__(self):
        super().__init__()
    def maki_dir(self,filepath):
        filepath.strip()
        isExists = os.path.exists(filepath)
        if not isExists:
            os.makedirs(filepath)
            print("创建路径:",filepath)
        else:
            print(filepath,'路径已存在')

    def get_file_content(self,filePath):
        try:
            with open(filePath, 'rb') as fp:
                return fp.read()
        except Exception as e:
            print(e)
            return ''
    #改变图片大小
    def UpdateImageSize(self,filepath):
        try:
            images = Image.open(filepath)
            out = images.resize((300, 300), Image.ANTIALIAS)
            out.save(filepath)
            return True
        except Exception as e:
            print(e)
            return False