# 主程序文件
from image import spiderclass
import threading
import config
import time
from db_mysql import DB_operating
from file import makidir
db = DB_operating()
makidir=makidir()

class imgage_spider(threading.Thread):
    def __init__(self):
        super().__init__()

    def run(self):
        sp = spiderclass()
        config.filepath = db.find_filepath()[0].replace("\\", "/")
        makidir.maki_dir(config.filepath)
        while True:
            resul = db.selectUrl()
            num=1
            if resul:
                for dome in resul:
                    # 读取首页所有类别URL
                    html = sp.spider(dome[1])
                    sp.spider_xpath(html,dome[2],dome[1],dome[5])
                    db.updateUrl(dome[0])
                    time.sleep(config.sleep_time)
            else:
                time.sleep(config.sleep_time)
if __name__ == '__main__':
    s = imgage_spider()
    s.start()
