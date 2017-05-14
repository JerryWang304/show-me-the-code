#!/usr/bin/python
# coding: utf-8

# 在图右上角添加数字
from PIL import Image, ImageDraw, ImageFont
def add_number(picture):
    image = Image.open(picture)
    print image.format
    #image.show()
    width, height = image.size
    print "width = %d, height = %d" % (width, height)
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("Roboto-Light.ttf",90)
    draw.text((width-100,0),"10",font=font, fill='#FF0000' )
    #image.save('result.jpg')
    image.show()
if __name__ == "__main__":
    add_number("avatar.jpeg")
