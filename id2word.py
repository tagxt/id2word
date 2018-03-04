#!usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@Created by sublime_text at home on  2018/3/4—14:59！
@Gnome:   Live and learn!
@Author: 葛绪涛
@Nickname:  wordGe
@QQ:  690815818
@Filename: id2word.py 
@Blog: http://higexutao.blog.163.com  
"""
from aip import AipOcr

# 定义常量
APP_ID = '10379743'
API_KEY = 'QGGvDG2yYiVFvujo6rlX4SvD'
SECRET_KEY = 'PcEAUvFO0z0TyiCdhwrbG97iVBdyb3Pk'


def getWordFromImage(image):
    img = AipOcr(APP_ID, API_KEY, SECRET_KEY)
    options = {
        'detect_direction': 'true',
        'language_type': 'CHN_ENG',
        'probability': 'true',
    }
    result = img.webImage(image, options)
    return result
