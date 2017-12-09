#!/usr/bin/python
#ecoding:utf-8

from pytesser import *
import ImageEnhance

image = Image.open("./tmp2.jpg")

enhancer = ImageEnhance.Contrast(image)
image_enhancer = enhancer.enhance(4)
print(image_to_string(image_enhancer))

