def main():
	print("进入程序")
	result = ''
	string = input("请输入字符串:")
	request = input("加密输入1，解密输入2：")
	if request != '1' and request != '2':
		request = input("输入有误加密输入1，解密输入2")
	if request == '1':
		result = encode(string)	#进入加密函数
		print(string + ":加密结果是：" +result)
	if request == '2':
		result = decode(string) #进入解密函数
		print(string + ':解密结果:' + result)
	
def encode(string): #加密
	encode_string = ""
	for char in string:
		encode_char = hex(ord(char)).replace("0x","%")	#加密核心代码
		encode_string += encode_char
	return encode_string

def decode(string): #解密
	decode_string = ""
	string_arr = string.split("%")	#输入数据变成列表
	string_arr.pop(0)	#删除第一个空元素
	for char in string_arr:
		decode_char = chr(eval("0x" + char))	#解密核心代码
		decode_string += decode_char
	return decode_string

main()
	