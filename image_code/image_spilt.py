#!/usr/bin/python
#ecoding: utf-8
''' 图片验证码分割 '''

# import pillow lib

from PIL import Image

# 问题部分图片的宽度和高度
width_question = 300
height_question = 30


# 分割问题部分的图片
def img_split_4_question(original_img):

    img = original_img.crop((120,0,width_question,height_question))

    # save new img
    img.save("./tmp2.jpg")
    return img


#分割验证码部分的图片
def img_split_4_code(original_img):


    width = original_img.size[0]
    height = original_img.size[1]

    img = original_img.crop((0,height_question,width,height))

    # save new img
    img.save("./tmp3.jpg")

    return img


# 对问题部分的图片进行8等分割，获取每张小图片
def img_split_code(original_img):

    img = vertical_split(original_img)

    img_code = []

    for temp_img in img:
        img_code = img_code + horizontal_split(temp_img)

    eight_img_code = []
    for tep_img in img_code:
        eight_img_code = eight_img_code + horizontal_split(tep_img)

    return eight_img_code


#水平对等分割
def horizontal_split(original_img):

    width = original_img.size[0]
    height = original_img.size[1]


    img = []
    img.append(original_img.crop((0,0,width / 2,height)))
    img.append(original_img.crop((width / 2,0,width,height)))


    return img


#垂直对等分割
def vertical_split(original_img):
    width = original_img.size[0]
    height = original_img.size[1]

    img = []
    img.append(original_img.crop((0,0,width,height / 2)))
    img.append(original_img.crop((0,height / 2,width,height)))

    return img

    # orignal image


img = Image.open("./tmp.jpg")
img_split_4_question(img)
img_split_4_code(img)

img3 = Image.open("./tmp3.jpg")
image3 = img_split_code(img3)

for i in range(len(image3)):
    image3[i].save("./temp" + str(i) + ".jpg")
