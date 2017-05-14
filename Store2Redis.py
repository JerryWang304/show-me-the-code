#!/usr/bin/python
# coding: utf-8

#将200个字符串存入Redis中
import redis
from ActiveCodes import codes


if __name__ == '__main__':
    active_codes = codes(200,15)
    r = redis.StrictRedis(host='localhost', port=6379, db=0)
    for i in range(len(active_codes)):
        r.set(i,active_codes[i])
    