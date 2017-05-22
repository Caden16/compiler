from drawTable import drawTable # 绘表工具
global component 				# 表格内容
global inputString   			# 输入串
global stack  					# 分析栈
global top 						# 栈顶元素
global step   					# 步骤数
global current 					# 当前字符
global table					# 分析表
table = {
'E':{'i':['E_','T'], '(':['E_','T']},
'E_':{'+':['E_','T','A'], '-':['E_','T','A'],	')':[],	'#':[]}, #用[]代表空串
'T':{'i':['T_','F'], '(':['T_','F']},
'T_':{'+':[],  '-':[], '*':['T_','F','M'], '/':['T_','F','M'],  ')':[],'#':[],},
'F':{'i':['i'], '(':[')','E','(']},
'A':{'+':['+'], '-':['-']},
'M':{'*':['*'], '/':['/']}
}

# 报错
def error(msg="分析错误"):		
	global component
	global step
	step = step + 1 
	component.append([step,msg,''])
	
	# exit(0)
	
# 查表
def queryTable(A,a):
	result =[]
	try:
		result = table[A][a]
	except:  
		error('查表出错')
		
		return False
	return result

# 推进	
def advance():   
	global stack
	global top 
	global current 
	global inputString  
	stack.pop()				 
	top = stack[-1]
	current = inputString.pop(0)

# 进栈，产生式右部逆序进栈
def entryStack(result):   
	global stack
	global top 
	stack.pop()
	stack.extend(result)
	top = stack[-1]

# 分析	
def analysis():
	global stack
	global top 
	global current 
	global component
	global inputString  
	global step
	Vt = ['i','+','-','*','/','(',')']
	Vn = ['E','E_','T','T_','F','A','M']
	stack =['#','E']    #初始化栈
	top = stack[-1]     #栈顶元素
	inputString = list(inputString)   # 源串
	inputString.append('#')           # 末尾添加#
	current = inputString.pop(0)	  # 当前字符
	flag = True						  # 循环标志
	step = 0	
	component = []					  
	while(flag):
		tempComponent = []			    # 表格每一行的内容
		tempComponent.append(step)	  			 
		tempComponent.append(str(stack))		 
		tempComponent.append(str(inputString))   
		component.append(tempComponent)
		if (top in Vt):					# 判断首字符是否是Vt
			if (top == current):        
				advance()				 
			else:
				error(' 非法字符 ')
				return '非法字符'
				break
		elif(top == '#'):
			if(current == '#'):
				flag = False			# 匹配成功，可以退出
			else:
				error("非法结束")
				return '非法字符'
				break
		else:
			result = queryTable(top,current)
			if(False != result):
				entryStack(result)				# 进栈
			else:	
				return '查表出错'				# 查表出错
				break
		step = step + 1	
	if(flag == False):
		return '匹配成功'
		
def main(string):
	global inputString
	global component

	inputString = string
		
	return analysis()
		
				
if __name__ == '__main__':
    main()				
	
	

	
	
	

