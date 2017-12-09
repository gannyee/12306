#!/usr/bin/python
#coding: utf-8

# œ¬‘ÿ12306Õº∆¨—È÷§¬Î


import urllib

import urllib.request

import json

from PIL import ImageFilter

from PIL import Image

pic_url = "https://kyfw.12306.cn/passport/captcha/captcha-image?login_site=E&module=login&rand=sjrand&0.7401238870112408"


def get_img():

    """ send get image code request and get the response """

    """ data process""" 
    with urllib.request.urlopen(pic_url) as url:
        raw = url.read()
   
    #print(raw)

    """" save got imgae into located file """
    """ write out in binary form """
    with open("./tmp.jpg",'wb') as fp:
        fp.write(raw)

    return Image.open("./tmp.jpg")

get_img()
