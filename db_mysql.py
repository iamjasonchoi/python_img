import pymysql
import config
import time
class DB_operating(object):
    def __init__(self):
        super().__init__()
    #更新爬取状态
    def updateUrl(self, urlid):
        conn = pymysql.connect(host=config.host, port=config.port, user=config.user, passwd=config.passwd, db=config.db,
                               charset=config.charset)
        cursor = conn.cursor()
        sql = 'UPDATE url SET operating=1 WHERE id=%s'
        try:
            cursor.execute(sql, urlid)
            conn.commit()
        except Exception as e:
            conn.rollback()
            print(e)
        finally:
            cursor.close()
            conn.close()
    #查询等待爬取的URL
    def selectUrl(self):
        conn = pymysql.connect(host=config.host, port=config.port, user=config.user, passwd=config.passwd, db=config.db,
                               charset=config.charset)
        cursor = conn.cursor()
        sql = 'SELECT * FROM url WHERE operating=0'
        try:
            cursor.execute(sql)
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()
        result = cursor.fetchall()
        return result
    #爬取完成的图片路径入库
    def INSERT_imgpath(self,filename,path,imgtype,words):
        conn = pymysql.connect(host=config.host, port=config.port, user=config.user, passwd=config.passwd, db=config.db,
                               charset=config.charset)
        cursor = conn.cursor()
        path=path.replace("\\",'/')
        print(path)
        sql="INSERT INTO t_img(filename,filepath,updata,upuser,type,`key`) VALUES('%s','%s','%s','%d','%d','%s')"%(filename,path,time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) ,2,imgtype,words)
        print('sql:',sql)
        try:
            cursor.execute(sql)
            conn.commit()
        except Exception as e:
            print(e)
            conn.rollback()
        finally:
            cursor.close()
            conn.close()
    #取得保存路径
    def find_filepath(self):
        conn = pymysql.connect(host=config.host, port=config.port, user=config.user, passwd=config.passwd, db=config.db,
                               charset=config.charset)
        cursor = conn.cursor()
        sql='SELECT `value` FROM config WHERE type=\'filepath\''
        cursor.execute(sql)
        filepath=cursor.fetchone()
        cursor.close()
        conn.close()
        return filepath