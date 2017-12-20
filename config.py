import pymysql.cursors
import time
# 需要爬取的网页
url = 'http://www.lubiaoqing.com'
# 休眠时间
sleep_time = 10
# 数据库链接属性
host = '127.0.0.1'
port = 3306
user = 'root'
passwd = ''
db = 'singdog'
charset = 'utf8'
#获取时间
getDate=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
#请求头
headers = {
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                'Accept-Language': 'zh-CN,zh;q=0.8',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
                'Accept-Encoding': 'gzipdeflate'}
filepath=''
