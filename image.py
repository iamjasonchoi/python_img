import requests
import config
from db_mysql import DB_operating
from lxml import html
import uuid
from AipOcr import aip
from file import makidir
from PIL import Image
DB = DB_operating()
makidir=makidir()
aip=aip()
class spiderclass(object):
    def __init__(self):
        super().__init__()

    # 爬取网页
    def spider(self, url):
        try:
            html = requests.get(url, headers=config.headers)
            html.encoding = 'utf-8'
            return html.text
        except Exception as e:
            print(e, '该URL抓取失败',url)
            html.close()
            return ''
    def spider_xpath(self, htmls, xpath,url,imgtype):
        tree = html.fromstring(htmls)
        contexts = tree.xpath(xpath)
        context = ''
        for item in contexts:
            self.download_image(item,url,imgtype)
    def download_image(self, imgurl,url,imgtype):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36',
                   'Referer': url,
                   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                   'Accept-Encoding': 'gzip, deflate, sdch',
                   'Accept-Language': 'zh-CN,zh;q=0.8',
                   'Cache-Control': 'max-age=0',
                   'Connection': 'keep-alive',
                   }
        if 'http:' in imgurl:
            img = requests.get(imgurl, stream=True, headers=headers)
            filename = imgurl.split('/')[-1]
            # D:\python_download_img
            with open(config.filepath+"/" + filename, 'wb') as f:
                for chunk in img.iter_content(chunk_size=1024):
                    if chunk:  # filter out keep-alive new chunks
                        f.write(chunk)
                        f.flush()
                f.close()
            path=config.filepath.split("/")[-1]+'/'+filename
            #PIL模块改变图片大小 哈哈
            filepath=config.filepath+'/'+filename
            try:
                makidir.UpdateImageSize(filepath)
                # 图像识别
                res = aip.aipOcrGeneral(filepath)
                words=''
                for dome in res['words_result']:
                    words+=dome['words']
                DB.INSERT_imgpath(filename, path, imgtype,words)
            except Exception as e:
                print(e)
            print('爬取图片:', filename)
