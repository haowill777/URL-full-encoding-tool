#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
2022由haowill开发[2022 haowill developers (http://www.haowill.top)]
加解密工具,如何使用请阅读readme.md(This program is Encryption and decryption tool. How to use it?Pelase see readme.md)
不好意程序需要python3(Sorry,program require Python3)
"""

import sys
from lib.core.UrlAllCode import UrlAllCode 	#URL全编码(URL All code)

if sys.version_info.major < (2):	#检查python版本(Check version of python)
    sys.stdout.write("抱歉,需要python3(Sorry, dirsearch requires Python 3.7 or higher)\n")
    sys.exit(1)

if __name__ == "__main__":
	try:
		# opt = getopt.getopt(sys.argv[1:],"hu:")
		# print(opt)
		print("进入程序(Inter program)")		# main函数
		result = ''
		string = input("请输入字符串:")
		request = input("加密输入1，解密输入2：")
		if request != '1' and request != '2':
			request = input("输入有误加密输入1，解密输入2")
		if request == '1':
			UrlAll =  UrlAllCode()
			result = UrlAll.encode(string)	#进入加密函数
			print(string + "=>加密结果是：" + result)
		if request == '2':
			UrlAll =  UrlAllCode()
			result = UrlAll.decode(string) #进入解密函数
			print(string + '=>解密结果:' + result)
	except:
		print("主要程序异常中断(Aborts the main program)")
		exit(1)
else:
	exit()

	