# 用户输入 := 的问题还没解决，主函数的状态尚未清楚


global inputString
global place
place = {'A':'', 'V':'', 'E':'', 'T':'', 'F':'' }
global entry
entry = {'i': ''}

global newTempNum  #新建变量的个数，从T1开始
newTempNum = 1

global fourTuple
fourTuple = []

global stateStack 
global operStack
global current
global GS
GS = [
'',
'S→A',
'A→V:=E',
'E→E+T',
'E→T',
'T→T*F',
'T→F',
'F→(E)',
'F→i',
'V→i'
]
global inputString 


global top		#字符栈的栈顶元素

global index    #字符栈的栈顶指针

global gotoTable
gotoTable = {
0:{'A':1, 'V':2, 'i':3},
2:{':=':4},
4:{'E':5, 'T':6, 'F':7, '(':8, 'i':9},
5:{'+':10},
6:{'*':11},
8:{'E':12,'T':6, 'F':7, '(':8, 'i':9},
10:{'T':13,'F':7, '(':8, 'i':9},
11:{'F':14,'(':8, 'i':9},
12:{'(':15, '+':10},
13:{'*':11},
}

global analysisTable

analysisTable = {
0:{'A':1, 'V':2, 'i':3},
2:{':=':4},
4:{'E':5, 'T':6, 'F':7, '(':8, 'i':9},
5:{'+':10},
6:{'*':11},
8:{'E':12,'T':6, 'F':7, '(':8, 'i':9},
10:{'T':13,'F':7, '(':8, 'i':9},
11:{'F':14,'(':8, 'i':9},
12:{'(':15, '+':10},
13:{'*':11},

}

	
def gen(list):
	global fourTuple
	fourTuple.append(list)
	

def S(num):
	global stateStack
	global operStack
	global current
	global place
	global entry
	place = {'A':'', 'V':'', 'E':'', 'T':'', 'F':'' }
	stateStack.append(num)    # 移进后的下一状态
	operStack.append(current) # 移进当前字符
	advance()
	
	
def entryStack(curr):   # 弹出栈顶，产生式右部逆序进栈
	global stack
	global top 
	global index
	stack.append(curr)
	top = stack[-1]
	index = index + 1
	
	
	
def R(num):  # 按第Num条规则规约
	global operStack
	global stateStack
	global entry
	global index 
	if(num == 2):           # 没有num = 1 的情况
		operStack.pop()
		index = index - 1
		operStack.entryStack('S')
		stateStack
		gen([':=', place['E'],'', place['V']])
		stateStack.pop()
		stateStack.pop()
		stateStack.pop()
		stackStack.append(GOTO(stateStack[-1],'A'))
	
	elif(num == 3):
		operStack.pop()
		operStack.pop()
		operStack.pop()
		index = index - 3
		operStack.entryStack('A')
	
		E1 = newTemp()
		gen( ['+', place['E'], place['T'], E1] )
		place['E'] = E1
		stateStack.pop()
		stateStack.pop()
		stateStack.pop()
		stackStack.append(GOTO(stateStack[-1],'E'))
	

		
	elif(num == 4):
		operStack.pop()
		index = index - 1
		operStack.entryStack('E')
		
		place['E'] = place['T']
		stateStack.pop()
		stackStack.append(GOTO(stateStack[-1],'E'))
			
	elif(num == 5):
		operStack.pop()
		operStack.pop()
		operStack.pop()
		index = index - 3
		operStack.entryStack('T')
		
		T1 = newTemp()
		gen( ['*', place['T'], place['F'], T1 ] )
		place['T'] = T1

		stateStack.pop()
		stateStack.pop()
		stateStack.pop()
		stackStack.append(GOTO(stateStack[-1],'T'))
			
		
	elif(num == 6):
		operStack.pop()
		index = index - 1
		operStack.entryStack('T')
		
		place['T'] = place['F']
		stateStack.pop()
		stackStack.append(GOTO(stateStack[-1],'T'))
			
	elif(num == 7):
		operStack.pop()
		operStack.pop()
		operStack.pop()
		index = index - 3
		operStack.entryStack('F')
		
		place['F'] = place['E']
		stateStack.pop()
		stateStack.pop()
		stateStack.pop()
		stackStack.append(GOTO(stateStack[-1],'F'))
		
		
	elif(num == 8):
		operStack.pop()
		index = index - 1
		operStack.entryStack['F']
		
		place['F'] = entry['i']	
		stateStack.pop()
		stackStack.append(GOTO(stateStack[-1],'F'))
		
	elif(num == 9):
		operStack.pop()
		index = index - 1
		operStack.entryStack('V')
		place['V'] = entry['i']		
		stateStack.pop()
		stackStack.append(GOTO(stateStack[-1],'V'))
	
	
def advance():  			# 将输入串后移一位
	global current 
	global inputString  # 
	current = inputString.pop(0)	
	
		
def GOTO(S,X):   #S是当状态，x是面临输入符，
	global gotoTable
	return gotoTable[S][X]
	

	
def newTemp():
	global place
	global newTempNum
	new_temp = 'T' + str(newTempNum)
	newTempNum = newTempNum + 1
	place[newTemp] = ''
	return new_temp
	
	
	
def analysis():
	global operStack
	global stateStack
	global top 
	global current 
	global inputString  # 
	global entry
	global index
	operStack =['#']    #初始化栈
	top = operStack[-1]     #栈顶元素
	stateStack = [0]
	
	
	inputString = list(inputString)   # 源串
	current = inputString.pop(0)		  # 当前字符
	index = 0	
	tempIndex = 0           # 为找到最顶端的运算符而设
	tempTop = ' '			# 为了寻找素短语的头而设

	while(len(operStack) != 2 or current !='#'):  # 结束条件
		print("状态符栈：",end = "")
		print(stateStack)
		print("操作符栈：",end = "")
		print(operStack)
		print("输入串：",end = "")
		print(inputString)
		state = stackStack[-1]
		if(state == 0):
			S(2)
			continue	
		elif()

			

	print("成功\n")	
	print(fourTuple)	
	
	
def main():
	global inputString
	while(1):
		# inputString = input("请输入语句（以#结束）")
		inputString = ['X',':=','B','+','C','*','D']
		if(inputString == "退出"):
			break
		if (inputString[-1]!='#'):
			continue
		analysis()
if __name__ == '__main__':
    main()				
		
	