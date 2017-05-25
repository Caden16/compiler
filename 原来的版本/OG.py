global inputString   
global stack  
global top 
global current 
global Vt
global F
global G
global index
global OGtable


OGtable = {
'E':{'i':['E_','T'], '(':['E_','T']},
'E_':{'+':['E_','T','A'], '-':['E_','T','A'],	')':[],	'#':[]},#用[]代表空串
'T':{'i':['T_','F'], '(':['T_','F']},
'T_':{'+':[],  '-':[], '*':['T_','F','M'], '/':['T_','F','M'],  ')':[],'#':[],},
'F':{'i':['i'], '(':[')','E','(']},
'A':{'+':['+'], '-':['-']},
'M':{'*':['*'], '/':['/']}
}




global F_Gtable
F_Gtable = {
'E':{'i':['E_','T'], '(':['E_','T']},
'E_':{'+':['E_','T','A'], '-':['E_','T','A'],	')':[],	'#':[]},#用[]代表空串
'T':{'i':['T_','F'], '(':['T_','F']},
'T_':{'+':[],  '-':[], '*':['T_','F','M'], '/':['T_','F','M'],  ')':[],'#':[],},
'F':{'i':['i'], '(':[')','E','(']},
'A':{'+':['+'], '-':['-']},
'M':{'*':['*'], '/':['/']}
}


def error(msg="分析错误，退出"):
	print(msg)
	exit(0)

def queryTable(A,a):
	result =[]
	try:
		result = table[A][a]
	except:  
		error('查表出错')
	return result


	
def advance():  # 将输入串后移一位
	global current 
	global inputString  # 
	current = inputString.pop(0)

def entryStack(curr):   # 弹出栈顶，产生式右部逆序进栈
	global stack
	global top 
	global index
	stack.append(curr)
	top = stack[-1]
	index = index + 1

				
	
def analysis():
	global stack
	global top 
	global current 
	global inputString  # 
	global Vt
	global F
	global G
	global index
	F = {'(':1, ')':7, 'i':7, '*':5, '/':5, '+':3, '-':3, '#':1, }
	G = {'(':6, ')':1, 'i':6, '*':4, '/':4, '+':2, '-':2, '#':1, }
	Vt = ['i','+','-','*','/','(',')','#']  
	Vn = ['E','T','F','N']
	stack =['#']    #初始化栈
	top = stack[-1]     #栈顶元素

	inputString = list(inputString)   # 源串
	current = inputString.pop(0)		  # 当前字符
	index = 0	
	tempIndex = 0           # 为找到最顶端的运算符而设
	tempTop = ' '			# 为了寻找素短语的头而设

	while(len(stack) != 2 or current !='#'):  # 结束条件
		print("栈：",end = "")
		print(stack)
		print("输入串：",end = "")
		print(inputString)
				
				
		if (top in Vt):
			tempIndex = index		
		else:
			tempIndex = index -1
		print(top)	
		print(index)
		print(tempIndex)
		print('栈首操作符是%s'%stack[tempIndex] )	

		if (F[stack[tempIndex]] > G[current] ):  # 寻找素短语起始位置
			
			tempTop = stack[tempIndex]
			
			print("找素短语头")
			tempIndex = tempIndex -1

			if (stack[tempIndex] in Vt):
				
				if(F[stack[tempIndex]] < G[tempTop]):  #可归约了
					print("规约一下，长度不变")
					stack.pop()
					index = index -1
					entryStack('N')
					
			else: #找到起始操作符
				print("规约，长度减2")
				stack.pop()
				stack.pop()  
				stack.pop()  
				index = index -3
				entryStack('N')
				

		
		else:    # <= 的都应该进栈
			print("%s进展咯"%current)
			entryStack(current)
			advance()
			continue   #进入下次循环		

	print("成功\n")
			
def main():
	global inputString
	while(1):
		inputString = input("请输入语句（以#结束）")
		if(inputString == "退出"):
			break
		if (inputString[-1]!='#'):
			continue
		analysis()
	

			
if __name__ == '__main__':
    main()				
	
	

	
	
	

