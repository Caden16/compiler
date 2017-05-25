global inputString   
global stack  
global top 
global current 

global table
table = {
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


	
def advance():  # 分析栈顶的Vt 匹配成,退栈,current 后移
	global stack
	global top 
	global current 
	global inputString  # 
	stack.pop()	# 退栈
	top = stack[-1]
	current = inputString.pop(0)

def entryStack(result):   # 弹出栈顶，产生式右部逆序进栈
	global stack
	global top 
	stack.pop()
	stack.extend(result)
	top = stack[-1]
	
def analysis():
	global stack
	global top 
	global current 
	global inputString  # 
	Vt = ['i','+','-','*','/','(',')']
	Vn = ['E','E_','T','T_','F','A','M']
	stack =['#','E']    #初始化栈
	top = stack[-1]     #栈顶元素

	inputString = list(inputString)   # 源串
	current = inputString.pop(0)		  # 当前字符
	flag = True
	# i = 5
	while(flag):

		if (top in Vt):
			print("出栈")
			if (top == current):
				advance()
			else:
				error('')
		elif(top == '#'):
			if(current == '#'):
				flag = False
			else:
				error("非法结束\n")
		else:
			result = queryTable(top,current)
			print(result)
			entryStack(result)
		# i = i-1
	if(flag == False):
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
	
	

	
	
	

