# -*- coding: utf-8 -*-
# Date: 2019/1/31


class Ftp_client(object):



    def register(self):
        '''注册方法'''
        print(222222222)

    def initialize(self):
        '''初始化方法，让用户选择登录或是注册'''
        while True:
            choose = input('register\nlogin\nEnter your choice: ').strip()
            if hasattr(self, choose):
                getattr(self, choose)()
            else:
                print('输入有误，请重新输入')
