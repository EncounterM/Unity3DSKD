# -*- coding: utf-8 -*-
# @Time    : 2022/3/6 5:37 下午
# @Author  : 杨从利
# @Contact : sdtcycl@163.com 
# @Site    : 
# @File    : test2.py
# @Software: PyCharm
# @Program function : 整合某个多级目录文件夹下面的图片到一个新的文件夹下,并实现修改名字（可以自行修改代码使其使用原始名字）
"""
Such as:
root_path:
    - folder1
        - img1.jpg
        - img2.jpg
    - folder2
        - img1.jpg
    - folder3

save_path:
    - img1.jpg
    - img2.jpg
    - img3.jpg
"""

import os
import shutil
from glob import glob
from PIL import Image


# 创建文件夹
def CreateDir(path):
    isExists=os.path.exists(path)
    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        os.makedirs(path)
        print(path+' 目录创建成功')
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print(path+' 目录已存在')

# 复制多目录文件夹下的文件到同一个目录下
def CopyFile(filepath, newPath, resize_width, resize_hight):
    # 获取当前路径下的文件名，返回List
    # print(newPath)
    fileNames = os.listdir(filepath)
    for file in fileNames:
        # 将文件名加入到当前文件路径后面
        newDir = filepath + '/' + file
        # 如果是文件
        if os.path.isfile(newDir):
            # print("newDir:", newDir)
            global count_img
            count_img = count_img + 1
            name = os.path.join(newPath, "%d.jpg" % count_img)

            im = Image.open(newDir)
            # im.thumbnail((720,1280))
            reim = im.resize((resize_width, resize_hight))

            print(im.format, reim.size, reim.mode, name)
            reim.save(name, im.format)
        # 如果不是文件，递归这个文件夹的路径
        else:
            CopyFile(filepath=newDir,newPath=newPath,resize_width=resize_width,resize_hight=resize_hight)

if __name__ == "__main__":
    count_img = 0
    path = "./testFolder"
    # 存放总文件的目录文件， 结尾必须有"/"
    result_path = "./result/"
    CopyFile(filepath=path, newPath=result_path, resize_width=680, resize_hight=512)


    # # 创建目标文件夹
    # mkPath = path + "/总文件/"
    # CreateDir(mkPath)
