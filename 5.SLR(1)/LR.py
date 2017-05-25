# 用户输入 := 的问题还没解决，主函数的状态尚未清楚

from drawTable import drawTable
global component # 表格内容
global flag   #成功标志
global inputString
global stateStack 
global operStack
global current
global inputString 
global top		#字符栈的栈顶元素
global index    #字符栈的栈顶指针
global gotoTable

gotoTable = {
0:{'E':1, 'T':2},
4:{'E':10, 'T':2},
6:{'T':8},
7:{'T':9}
}

global actionTable
actionTable = {
0:{'i':'S(3)',  '(':'S(4)','+':' ',  '-':' ',	   ')':' ',     '#':' '},
1:{'+':'S(6)',  '-':'S(7)',	'#':'S(5)', 	'(':' ',  ')':' ',  'i':' '},
2:{'+':'R(4)',  '-':'R(4)',	'(':'R(4)', ')':'R(4)', 'i':'R(4)','#':'R(4)'},
3:{'+':'R(6)',  '-':'R(6)',	'(':'R(6)', ')':'R(6)', 'i':'R(6)','#':'R(6)'},
4:{'i':'S(3)',  '(':'S(4)','+':' ',  '-':' ',	'(':' ',     '#':' '},
5:{'#':'R(1)','+':' ',  '-':' ',	'(':' ',  ')':' ',  'i':' ' },
6:{'i':'S(3)',  '(':'S(4)','+':' ',  '-':' ',	  ')':' ',   '#':' '},
7:{'i':'S(3)',  '(':'S(4)','+':' ',  '-':' ',	  ')':' ',   '#':' '},
8:{'+':'R(2)',  '-':'R(2)',	'(':'R(2)', ')':'R(2)', 'i':'R(2)','#':'R(2)'},
9:{'+':'R(3)',  '-':'R(3)',	'(':'R(3)', ')':'R(3)', 'i':'R(3)','#':'R(3)'},
10:{'+':'S(6)', '-':'S(7)', ')':'S(11)', '(':' ',    'i':' ',  '#':' '},
11:{'+':'R(5)',  '-':'R(5)',	'(':'R(5)', ')':'R(5)', 'i':'R(5)','#':'R(5)'}
}


def S(num):
	global stateStack
	global operStack
	global current
	stateStack.append(num)    # 移进后的下一状态
	operStack.append(current) # 移进当前字符
	# advance()
	
	
def entryStack(curr):   # 弹出栈顶，产生式右部逆序进栈
	global operStack
	global top 
	global index
	operStack.append(curr)
	top = operStack[-1]
	index = index + 1
	
		
def R(num):  # 按第Num条规则规约
	global operStack
	global stateStack
	global entry
	global index 
	global flag
	if(num == 1):           # 没有num = 1 的情况
		operStack.pop()
		operStack.pop()
		stateStack.pop()
		stateStack.pop()
		index = index - 2
		entryStack('S')
		# flag = True

	
	elif(num == 2 or num == 3):
		operStack.pop()
		operStack.pop()
		operStack.pop()
		stateStack.pop()
		stateStack.pop()
		stateStack.pop()
		index = index - 3
		entryStack('E')
		stateStack.append(gotoTable[stateStack[-1]]['E'])   # 新状态


		
	elif(num == 4):
		operStack.pop()
		stateStack.pop()
		index = index - 1
		entryStack('E')
		stateStack.append(gotoTable[stateStack[-1]]['E'])   # 新状态


			 
	elif(num == 6):   # 五和六颠倒了
		operStack.pop()
		stateStack.pop()	
		index = index - 1
		entryStack('T')
		stateStack.append(gotoTable[stateStack[-1]]['T'])   # 新状态

			
		
	elif(num == 5):
		operStack.pop()
		operStack.pop()
		operStack.pop()
		stateStack.pop()
		stateStack.pop()
		stateStack.pop()
		index = index - 3
		entryStack('T')
		stateStack.append(gotoTable[stateStack[-1]]['T'])   # 新状态


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
	global flag   #成功标志
	operStack =['#']    #初始化栈
	top = operStack[-1]     #栈顶元素
	stateStack = [0]
	inputString = list(inputString)   # 源串
	# inputString.append('#')           # 末尾再加上一个# 防止最后advance时 出界  
	current = inputString.pop(0)		  # 当前字符
	index = 0	
	step = 0 # 步骤数
	component = [] # 具体表格项
	flag = False
	while(operStack[-1] != 'S' ):  # 结束条件
		tempComponent = []
		# tempComponent.append(step)
		tempComponent.append(str(operStack))
		tempComponent.append(str(stateStack))
		print("当前字符：",end = "")
		print(current)
		print("状态符栈：",end = "")
		print(stateStack)
		print("操作符栈：",end = "")
		print(operStack)
		state = stateStack[-1]	
		nextAction = actionTable[state][current]
		tempComponent.append(nextAction) # 表项最后一列为采取的动作

		if(nextAction == ' '):
			advance()#   直到状态栈顶对应操作符栈顶 查表失败后，再把输入串进一下
			continue
		eval(nextAction)
		step = step + 1
		component.append(tempComponent)
		print(tempComponent)
	# print("当前字符：",end = "")
	# print(current)
	# print("状态符栈：",end = "")
	# print(stateStack)
	# print("操作符栈：",end = "")
	# print(operStack)
	# print("输入串：",end = "")
	# print(inputString)
	# print("成功")
	return 0
	
	
def main():
	global inputString
	global component
	while(1):
		inputString = input("请输入语句（以#结束）")
		inputString = 'i-(i+i)#'
		if(inputString == "exit"):
			break
		if (inputString[-1]!='#'):
			continue
		analysis()
		header = 'LR分析'
		subHeader = ['状态栈', '符号栈', '动作']#
		# print(component)
		drawTable(header,subHeader,component,110,0)  # 最后一个参数为总长度
		
if __name__ == '__main__':
    main()				
		
	