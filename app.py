#!usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@Created by sublime_text at home on  2018/3/4—14:04！
@Gnome:   Live and learn!
@Author: 葛绪涛
@Nickname:  wordGe
@QQ:  690815818
@Filename: web.py 
@Blog: http://higexutao.blog.163.com  
"""
# 此程序是利用百度的 baidu-aip 模块进行身份证识别（文字识别）
# 引入库
import sys
from tornado import web, httpserver, ioloop
from id2word import getWordFromImage


class MainPageHandler(web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render('index.html')

    def post(self, *args, **kwargs):
        # 得到文件的 包含 filename body content-Type
        file = self.request.files.get('myImage')
        if file:
            for img in file:
                fn = img['filename']
                fn_ext = fn.split('.')[1]
                fn_ext = fn_ext.lower()
                if fn_ext == 'png' or fn_ext == 'jpg':
                    # print(fn_ext)
                    # 得到网页index.html 上传的文件，注<input type='file' name='myImage'
                    xlImg = self.request.files.get('myImage')[0]
                    res = getWordFromImage(xlImg['body'])
                    self.render('result.html', content=res['words_result'])
                else:
                    self.render('error_ext.html', ext_name=fn_ext)
                    # sys.exit()
            else:
                pass
                # self.render('error_ext.html', ext_name='空')
                # self.render('http://127.0.0.1:8888')


# 设置参数（tornad 的两个路径参数 template_path  (放网页）    static_path （放js 和css）
settings = {
    'template_path': 'templates',
    'static_path': 'static',
}
application = web.Application([
    (r"/", MainPageHandler),
], **settings)

if __name__ == '__main__':
    http_server = httpserver.HTTPServer(application)
    http_server.listen(8888)
    ioloop.IOLoop.current().start()
