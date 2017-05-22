# 算符优先
from drawTable import drawTable
global component # 表格内容
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
	global component # 表格内容
	global index
	F = {'(':1, ')':7, 'i':7, '*':5, '/':5, '+':3, '-':3, '#':1, }
	G = {'(':6, ')':1, 'i':6, '*':4, '/':4, '+':2, '-':2, '#':1, }
	Vt = ['i','+','-','*','/','(',')','#']  
	Vn = ['E','T','F','N']
	stack =['#']    #初始化栈
	top = stack[-1]     #栈顶元素

	inputString = list(inputString)   # 源串
	inputString.append('#')
	current = inputString.pop(0)		  # 当前字符
	index = 0	
	tempIndex = 0           # 为找到最顶端的运算符而设
	tempTop = ' '			# 为了寻找素短语的头而设
	step = 0
	component = [] # 具体表格项
	while(len(stack) != 2 or current !='#'):  # 结束条件	
		tempComponent = []
		tempComponent.append(step)
		tempComponent.append(str(stack))
		tempComponent.append(str(inputString))	
		if (top in Vt):
			tempIndex = index		
		else:
			tempIndex = index -1
			
		try:
			result = F[stack[tempIndex]] > G[current]
		except:  
			error('输入符号错误')	
			return '输入符号错误'
			
		if (result ):  # 寻找素短语起始位置			
			tempTop = stack[tempIndex]		 
			tempIndex = tempIndex -1
			if (stack[tempIndex] in Vt):
				
				if(F[stack[tempIndex]] < G[tempTop]):  #可归约 
					stack.pop()
					index = index -1
					entryStack('N')				
			else: #找到起始操作符 
				stack.pop()
				stack.pop()  
				stack.pop()  
				index = index -3
				entryStack('N')			
			step = step + 1
			component.append(tempComponent)
		
		else:   		 # <= 的都应该进栈
 
			entryStack(current)
			advance()
			step = step + 1
			component.append(tempComponent)
			continue   #进入下次循环		
	
		tempComponent = []
		tempComponent.append(step)
		tempComponent.append(str(stack))
		tempComponent.append(str(inputString))	
		component.append(tempComponent)
	step += step
	tempComponent = [step,'匹配成功','匹配成功']
	component.append(tempComponent)
	return '匹配成功'
			
def main(string):
	global inputString
	global component # 表格内容
	
	inputString = string
	
	return analysis()


			
if __name__ == '__main__':
    main('i')				
	
	

	
	
	

