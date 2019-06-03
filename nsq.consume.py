# -*- coding: utf-8 -*-
# @Time    : 2019/6/3 14:54
# @Author  : wcl
# @File    : nsq.consume.py
# @Software: PyCharm
import nsq


def handler(message):
    print(message)
    print(message.body)
    return True


r = nsq.Reader(message_handler=handler, nsqd_tcp_addresses=['192.168.1.171:4150'], topic='test_topic', channel='asdfxx',
               lookupd_poll_interval=15)
nsq.run()

"""
#启动lookup
nsqlookupd
#启动一个nsqd , 并指定lookup的地址
nsqd --lookupd-tcp-address=127.0.0.1:4160
#打开一个监控网址
nsqadmin --lookupd-http-address=127.0.0.1:4161
"""
