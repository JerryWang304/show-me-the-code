#!usr/bin/python
#coding: utf-8

import Image
import os
legal_max_height = 1136
legal_max_width = 640

def is_legal_image(im):
    w,h = im.size
    if w > legal_max_width or h > legal_max_height:
        return False
    return True

def change_image_size(im,filename):
    new_image = im.resize((legal_max_width, legal_max_height),Image.ANTIALIAS)
    new_image.save(str(filename)+'.jpeg')

if __name__ == '__main__':
    count = 10
    files = os.listdir(os.curdir)
    for el in files:
        # 获取文件后缀判断是否是图片
        file_type = os.path.splitext(el)[1]
        print file_type
        if file_type == '.png':
            im = Image.open(el)
            if not is_legal_image(im):
                change_image_size(im,count)
                count += 1
