import gevent

from gevent import monkey
monkey.patch_all()

import requests     # urllib 进行封装 爬虫 80-90

# 并行  并发
# 协程  并发

def download(url):
    print("get: %s" % url)
    res = requests.get(url)
    data = res.text
    print(len(data), url)


# g1 = gevent.spawn(download, 'https://www.baidu.com/')
# g2 = gevent.spawn(download, 'https://www.python.org/')        # 时间久一点
# g3 = gevent.spawn(download, 'https://www.baidu.com/')
# g1.join()
# g2.join()
# g3.join()

gevent.joinall([
    gevent.spawn(download, 'https://www.baidu.com/'),
    gevent.spawn(download, 'https://www.python.org/'),
    gevent.spawn(download, 'https://www.baidu.com/')
])
