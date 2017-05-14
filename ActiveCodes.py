#!/usr/bin/python
# coding: utf-8
import random
import string
# 生成激活码
def codes(num,length):
    # length: length of each code
    # num: total number of codes
    store = string.uppercase + string.lowercase + string.digits
    #print store
    count = 0
    ret = []
    while count < num:
        one_code = ""
        for i in range(length):
            c = random.choice(store)
            one_code += c
        # print one_code
        if not one_code in ret:
            ret.append(one_code)
            count += 1
    return ret
if __name__ == "__main__":
    codes =  codes(200,15)
    for i in range(200):
        print "%d: %s" % (i+1, codes[i])
