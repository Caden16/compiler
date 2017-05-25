from drawTable import drawTable

global current
global inputString
global component
global step

def advance():
	global current
	current = inputString.pop(0) #pop默认退最后一个
	
def A():		
	global component
	global step

	if (current == '+' or current == '-'):
		advance()
		return True
	else:
		return False

def M():						 
	global component
	global step
	step = step + 1
	component.append([step , 'M'])
	if (current == '*' or current == '/'):
		advance()
		return True
	else:
		return False
			
def F():						# ok
	global component
	global step

	if (current =='('):
		advance()
		if(E()):   # E
			step = step + 1
			component.append([step , 'E'])
			if(current == ')'):
				advance()
				return True
	elif(current =='i'):
		advance()
		return True	
	return False
	
def T_():
	global component
	global step

	if(current == '*' or current =='/'):
		if(M()):
			step = step + 1
			component.append([step , 'M'])
			if(F()):
				step = step + 1
				component.append([step , 'F'])
				if(T_()):
					step = step + 1
					component.append([step , 'T_'])
					# advance()
					return True
	elif(current ==')' or current =='#' or current =='+' or current =='-'):
		# advance()       不确定
		return True
	return False	
		
def T():
	global component
	global step

	if(current =='i' or current =='('):
		if (F()):
			step = step + 1
			component.append([step , 'F'])
			if(T_()):
				step = step + 1
				component.append([step , 'T_'])
				return True
	return False
		
def E_():
	global component
	global step

	if(current =='+' or current =='-'):
		if (A()):
			step = step + 1
			component.append([step , 'A'])
			if(T()):
				step = step + 1
				component.append([step , 'T'])
				if (E_()):
					step = step + 1
					component.append([step , 'E_'])
					return True
					
	elif(current ==')' or current =='#'):
		return True
	return False
	
def E():
	global component
	global step
	
	if(current =='i' or current =='('):
		if(T()):
			step = step + 1
			component.append([step , 'T'])
			if(E_()):
				step = step + 1			
				component.append([step , 'E_'])	
				return True			
	step = step + 1			
	component.append([step , 'fail'])			
	return False			

def main():
	global current
	global inputString 	
	global component
	global step
	
	
	while(1):
		component =[]
		step = -1
		inputString = input("请输入语句(递归下降)：")
		inputString = list(inputString)
		inputString .append('#')
		current=inputString.pop(0)
		step = step + 1
		component.append([step , 'E'])
		if(E()):
			step = step + 1
			component.append([step , 'succes'])
		header = '递归下降'
		subHeader = [ '步骤', '调用关系']#
		drawTable(header,subHeader,component,60,1)  # 最后一个参数为总长度
		

if __name__ == '__main__':
    main()	