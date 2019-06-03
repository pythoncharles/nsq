# -*- coding: utf-8 -*-
# @Time    : 2019/6/3 14:50
# @Author  : wcl
# @File    : nsq.create.py
# @Software: PyCharm

import nsq
import tornado.ioloop
import time


def pub_message():
    write.pub('test_topic', time.strftime('%H:%M:%S'), finish_pub)


def finish_pub(conn, data):
    print(data)


write = nsq.Writer(['127.0.0.1:4150'])
tornado.ioloop.PeriodicCallback(pub_message, 1000).start()
nsq.run()
