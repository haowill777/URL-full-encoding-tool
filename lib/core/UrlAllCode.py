class UrlAllCode:
	try:
		def encode(self, string): #加密
			encode_string = ""
			for char in string:
				encode_char = hex(ord(char)).replace("0x","%")	#加密核心代码
				encode_string += encode_char
			return encode_string
	except:
		print("加密函数中断(Aborts the encode program)")
		exit()

	try:
		def decode(self, string): #解密
			decode_string = ""
			string_arr = string.split("%")	#输入数据变成列表
			string_arr.pop(0)	#删除第一个空元素
			for char in string_arr:
				decode_char = chr(eval("0x" + char))	#解密核心代码
				decode_string += decode_char
			return decode_string
	except:
		print("解密函数中断(Aborts the decode program)")
		exit()
