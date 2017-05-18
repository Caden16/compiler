#-*- coding:utf-8 -*-
'''
Due: 	2017-3-14
Author: Adaxry
Usage:	count the number of chinese and return the number
'''

def containChinese(string):
	string = str(string) # 转为字符串
	numOChinese = int((len(string.encode('utf-8')) - len(string))/2)
	return numOChinese

	
def main():
	print(containChinese("这句话里有8个汉语"))
	
if __name__=='__main__':
	main()