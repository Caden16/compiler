#-*- coding:utf-8 -*-
from containChinese import containChinese
global width
global subWidth 
global div
width = 80

'''
Due      : 2017-3-13
Author   : Adaxry
Vertion  : 1.0
Usage  	 : draw the tabel use 3 parameter
Parameter: header (string)   table title
		 : subHeader(list)
		 : component(list(list)) 
update   ： 
2017-5-18 增添是否居中的选项，添加至最后一个参数			
增添一个新的绘制表格内容的函数，其中取出居中部分		 

'''

def drawTable(header,subHeader,component,p_width = 80,ifCenter = 1): 
	global width
	global subWidth
	global div
	width = p_width
	# width = input("请输入表格长度(建议 40)  ")
	# width = int(width)
	div = len(subHeader)
	subWidth = int(width / div)
	width = div * subWidth
	drawHeader(header)
	drawSubHeader(subHeader)
	# drawAllContent(component)
	for i in range(len(component)):  # 打印所有表格内容
		# drawLine(len(component[0]))
		if(ifCenter):
			drawContent(component[i])
		else:
			drawNoCenter(component[i])
	drawLine(len(component[0]))	

def drawHeader(header):
	global div 
	drawLine(1)
	headerList = []
	headerList.append(header)# 作为列表
	drawContent(headerList)
	
	
def drawSubHeader(subHeader):
	drawLine(len(subHeader))
	global subWidth 
	global div 
	drawContent(subHeader)

	
def drawContent(content): # content 是列表  drawNoCenter
	global width
	localsDiv = len(content)
	localsWidth = int(width/localsDiv) - 1 
	for i in range(localsDiv):
		drawSymbol('|',1)
		print(str(content[i]).center(localsWidth - containChinese(content[i]),' '),end = "")
	drawSymbol('|',1)
	print()	 #输完一个表项后换行

	
def drawNoCenter(content): # 左对齐
	global width
	localsDiv = len(content)
	localsWidth = int(width/localsDiv) - 1 
	for i in range(localsDiv):
		drawSymbol('|',1)
		print(str(content[i]).ljust(localsWidth),end = "")
	drawSymbol('|',1)
	print()	 #输完一个表项后换行	



	
def drawLine(div):	 
	global width
	localsWidth = int(width/div)
	for i in range(div):
		drawShortLine(localsWidth)
	print('+')	
	
	

def drawShortLine(shortWidth):	
	drawSymbol('+',1)
	drawSymbol('-',shortWidth-1)	

	
	
def drawSymbol(symbol,times):	
	print(symbol * times ,end = "")   # Print多次输出 * 的用法
		
		
def main(header,subHeader,component):
	drawTable(header,subHeader,component,59)
		
if __name__=='__main__':
	header = "表格标题"
	subHeader = ["第一列","第二列","第三列"]
	component = [[1,2,3],[11,22,33],[111,222,333],[1111,2222,3333],[11111,22222,33333]]
	main(header,subHeader,component)
    		
			