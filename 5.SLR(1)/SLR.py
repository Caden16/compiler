from drawTable import drawTable
global component # 表格内容
global newTempNum  #新建变量的个数，从T1开始
global fourTuple
global place
global entry
global flag   #成功标志
global inputString
global stateStack 
global operStack
global current
global inputString 
global top		#字符栈的栈顶元素
global index    #字符栈的栈顶指针
global gotoTable
global actionTable

entry = {'i': ''}
newTempNum = 1
fourTuple = [[' ']]
place = {'A':'', 'V':'', 'E':'', 'T':'', 'F':'' }
gotoTable = {
0:{'A':1, 'V':2},
4:{'E':5, 'T':6, 'F':7},
8:{'E':14, 'T':6, 'F':7},
10:{'T':15, 'F':7},
11:{'T':16, 'F':7 },
12:{'F':17},
13:{'F':18}
}

actionTable = {
0:{ '=':' ','+':' ',  '-':'　','*':' ',  '/':' ', '(':' ',  ')':' ',  'i':'S(3)',  '#':' '},
1:{ '=':' ','+':' ',  '-':'　','*':' ',  '/':' ', '(':' ',  ')':' ',  'i':' ',  '#':'S(20)'},
2:{ '=':'S(4)','+':' ',  '-':'　','*':' ',  '/':' ', '(':' ',  ')':' ',  'i':' ',  '#':' '},
3:{ '=':'R(11)','+':' ',  '-':'　','*':' ',  '/':' ', '(':' ',  ')':' ',  'i':' ',  '#':' '},
4:{ '=':' ','+':' ',  '-':'　','*':' ',  '/':' ', '(':' S(8)',  ')':' ',  'i':'S(9) ',  '#':' '},
5:{ '=':' ','+':'S(10)',  '-':'S(11)','*':' ',  '/':' ', '(':' ',  ')':' ',  'i':' ',  '#':'R(2)'},
6:{ '=':' ','+':'R(5)',  '-':'　R(5)','*':'S(12)',  '/':'S(13)', '(':' ',  ')':'R(5)',  'i':' ',  '#':'R(5)'},
7:{ '=':' ','+':'R(8)',  '-':'R(8)','*':'R(8)',  '/':'R(8)', '(':' ',  ')':'R(8)',  'i':' ',  '#':'R(8)'},
8:{ '=':' ','+':' ',  '-':'　','*':' ',  '/':' ', '(':'S(8)',  ')':' ',  'i':'S(9)',  '#':' '},
9:{ '=':' ','+':'R(10)',  '-':'R(10)','*':'R(10)',  '/':'R(10)', '(':' ',  ')':'R(10)',  'i':' ',  '#':'R(10)'},
10:{ '=':' ','+':' ',  '-':'　','*':' ',  '/':' ', '(':'S(8)',  ')':' ',  'i':'S(9) ',  '#':' '},
11:{ '=':' ','+':' ',  '-':'　','*':' ',  '/':' ', '(':'S(8)',  ')':' ',  'i':'S(9)',  '#':' '},
12:{ '=':' ','+':' ',  '-':'　','*':' ',  '/':' ', '(':'S(8)',  ')':' ',  'i':'S(9)',  '#':' '},
13:{ '=':' ','+':' ',  '-':'　','*':' ',  '/':' ', '(':'S(8)',  ')':' ',  'i':'S(9)',  '#':' '},
14:{ '=':' ','+':'S(10)',  '-':'S(11)','*':' ',  '/':' ', '(':' ',  ')':'S(19)',  'i':' ',  '#':' '},
15:{ '=':' ','+':'R(3)',  '-':'R(3)','*':'S(12)',  '/':'S(13)', '(':' ',  ')':'R(3)',  'i':' ',  '#':'R(3)'},
16:{ '=':' ','+':'R(4)',  '-':'R(4)','*':'S(12)',  '/':'S(13)', '(':' ',  ')':'R(4)',  'i':' ',  '#':'R(4)'},
17:{ '=':' ','+':'R(6)',  '-':'R(6)','*':'R(6)',  '/':'R(6)', '(':' ',  ')':'R(6)',  'i':' ',  '#':'R(6)'},
18:{ '=':' ','+':'R(7)',  '-':'R(7)','*':'R(7)',  '/':'R(7)', '(':' ',  ')':'R(7)',  'i':' ',  '#':'R(7)'},
19:{ '=':' ','+':'R(9)',  '-':'R(9)','*':'R(9)',  '/':'R(9)', '(':' ',  ')':'R(9)',  'i':' ',  '#':'R(9)'},
20:{ '=':' ','+':' ',  '-':'　','*':' ',  '/':' ', '(':' ',  ')':' ',  'i':' ',  '#':'R(1)'} 

}
# 生成四元式
def gen(list):
	global fourTuple
	fourTuple.append(list)

# 新建临时变量
def newTemp():
	global place
	global newTempNum
	new_temp = 'T' + str(newTempNum)
	newTempNum = newTempNum + 1
	place[newTemp] = ''
	return new_temp	


def S(num):
	global stateStack
	global operStack
	global current
	
		
	stateStack.append(num)    # 移进后的下一状态
	operStack.append(current) # 移进当前字符
	if(num != 20):
		advance()
	

def entryStack(curr):   
	global operStack
	global top 
	global index
	operStack.append(curr)
	top = operStack[-1]
	index = index + 1
	
	
def R(num):  
	global operStack
	global stateStack
	global current
	global entry
	global index 
	global place
	global flag
	if(num == 1):          
		operStack.pop()
		operStack.pop()
		stateStack.pop()
		stateStack.pop()
		index = index - 2
		entryStack('S')
	
	elif(num == 2):
		operStack.pop()
		operStack.pop()
		operStack.pop()
		stateStack.pop()
		stateStack.pop()
		stateStack.pop()
		index = index - 3
		entryStack('A')
		stateStack.append(gotoTable[stateStack[-1]]['A'])   # 新状态
		gen(['=', place['E'], '_',  place['V']])		
		
	elif(num == 3):
		operStack.pop()
		operStack.pop()
		operStack.pop()
		stateStack.pop()
		stateStack.pop()
		stateStack.pop()
		index = index - 3
		entryStack('E')
		stateStack.append(gotoTable[stateStack[-1]]['E'])   # 新状态		
		E1 = newTemp()
		gen( ['+', place['E'], place['T'], E1] )
		place['E'] = E1		
		
	elif(num == 4):
		operStack.pop()
		operStack.pop()
		operStack.pop()
		stateStack.pop()
		stateStack.pop()
		stateStack.pop()
		index = index - 3
		entryStack('E')
		stateStack.append(gotoTable[stateStack[-1]]['E'])   # 新状态	
		E1 = newTemp()
		gen( ['-', place['E'], place['T'], E1] )
		place['E'] = E1		
		
	elif(num == 5):
		operStack.pop()
		stateStack.pop()
		index = index - 1
		entryStack('E')
		stateStack.append(gotoTable[stateStack[-1]]['E'])   # 新状态
		place['E'] = place['T']
			 
	elif(num == 6 ):    
		operStack.pop()
		operStack.pop()
		operStack.pop()
		stateStack.pop()
		stateStack.pop()
		stateStack.pop()
		index = index - 3
		entryStack('T')
		stateStack.append(gotoTable[stateStack[-1]]['T'])   # 新状态		
		T1 = newTemp()
		gen( ['*', place['T'], place['F'], T1] )
		place['T'] = T1	
	
	elif(num == 7):    
		operStack.pop()
		operStack.pop()
		operStack.pop()
		stateStack.pop()
		stateStack.pop()
		stateStack.pop()
		index = index - 3
		entryStack('T')
		stateStack.append(gotoTable[stateStack[-1]]['T'])   # 新状态	
		T1 = newTemp()
		gen( ['/', place['T'], place['F'], T1] )
		place['T'] = T1
				
	elif(num == 8):
		operStack.pop()
		stateStack.pop()
		index = index - 1
		entryStack('T')
		stateStack.append(gotoTable[stateStack[-1]]['T'])   # 新状态		
		place['T'] = place['F']
	
	elif(num == 9):    
		operStack.pop()
		operStack.pop()
		operStack.pop()
		stateStack.pop()
		stateStack.pop()
		stateStack.pop()
		index = index - 3
		entryStack('F')
		stateStack.append(gotoTable[stateStack[-1]]['F'])   # 新状态
		place['F'] = place['E']
	
	elif(num == 10):
		operStack.pop()
		stateStack.pop()
		index = index - 1
		entryStack('F')
		stateStack.append(gotoTable[stateStack[-1]]['F'])   # 新状态	
		place['F'] = entry['i']
			
	elif(num == 11):
		operStack.pop()
		stateStack.pop()
		index = index - 1
		entryStack('V')
		stateStack.append(gotoTable[stateStack[-1]]['V'])   # 新状态	
		place['V'] = entry['i']
		

def advance():  			# 将输入串后移一位
	global current 
	global inputString  # 
	current = inputString.pop(0)	
		
def analysis():
	global component
	global operStack
	global stateStack
	global top 
	global current 
	global inputString  # 
	global entry
	global index
	global actionTable
	global gotoTable
	global place
	global fourTuple
	global flag   #成功标志
	Vt = ['=', '+', '-', '*', '/', '(', ')', 'i' ,'#']
	operStack =['#']    #初始化栈
	top = operStack[-1]     #栈顶元素
	stateStack = [0]
	inputString = list(inputString)   # 源串
	inputString.append('#')           # 末尾再加上一个# 防止最后advance时 出界  
	current = inputString.pop(0)		  # 当前字符
	index = 0	
	component = [] # 具体表格项
	flag = False
	while(operStack[-1] != 'S' ):  # 结束条件
		tempComponent = []
		tempComponent.append(str(operStack))
		tempComponent.append(str(stateStack))
		# print("当前字符：",end = "")
		# print(current)
		# print("状态符栈：",end = "")
		# print(stateStack)
		# print("操作符栈：",end = "")
		# print(operStack)
		if (current not in Vt):
			entry['i'] = current
			current = 'i'
		state = stateStack[-1]	
		nextAction = actionTable[state][current]
		# print("采取动作：",end = "")
		# print(nextAction)
		# print("place：",end = "")
		# print(place)
		# print("entry：",end = "")
		# print(entry)
		# print("四元组：",end = "")
		# print(fourTuple)
		# print()
		tempComponent.append(nextAction) # 表项最后一列为采取的动作	
		eval(nextAction)
		tempComponent.append(str(fourTuple[-1]))
		component.append(tempComponent)
	# print("当前字符：",end = "")
	# print(current)
	# print("状态符栈：",end = "")
	# print(stateStack)
	# print("操作符栈：",end = "")
	# print(operStack)
	# print("输入串：",end = "")
	# print(inputString)
	tempComponent = []
	tempComponent.append(str(operStack))
	tempComponent.append(str(stateStack[-1]))
	tempComponent.append('匹配成功')
	tempComponent.append('匹配成功')
	component.append(tempComponent)
	# print("成功")
	return 0
		
def main():
	global inputString
	global component
	global fourTuple

	while(1):
		fourTuple = [[' ']]
		inputString = input("请输入语句（以#结束）")
		inputString = inputString.replace(' ','')
		if(inputString == "exit"):
			break			
		analysis()
		header = 'LR分析'
		subHeader = ['状态栈', '符号栈', '动作','四元式']#
		drawTable(header,subHeader,component,180,0)  # 最后一个参数为总长度
		
if __name__ == '__main__':
    main()				

	