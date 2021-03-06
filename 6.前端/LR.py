#!/usr/bin/python
# -*- coding: utf-8 -*-
# 用户输入 := 的问题还没解决，主函数的状态尚未清楚

from drawTable import drawTable
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
	global operStack
	global stateStack
	global top 
	global current 
	global inputString  # 
	global entry
	global actionTable
	global index 
	global gotoTable
	global flag   #成功标志
	operStack =['#']    #初始化栈
	top = operStack[-1]     #栈顶元素
	index = 0
	stateStack = [0]
	inputString.append('#')           # 末尾再加上一个# 防止最后advance时 出界  
	current = inputString.pop(0)		  # 当前字符
	
	while(operStack[-1] != 'S' ):  # 结束条件
		state = stateStack[-1]	
		try:
			nextAction = actionTable[state][current]
		except:
			return '查表错误'	

		if(nextAction == ' '):
			advance()#   直到状态栈顶对应操作符栈顶 查表失败后，再把输入串进一下
			continue
		eval(nextAction)
	 
	return '匹配成功'
	
	
def main(string):  
	global inputString
	global index 
	index = -1
	inputString = list(string)
	inputString = inputString.replace(' ','')
	return analysis()
		
if __name__ == '__main__':
    main('i+i-(i)')				
		
	