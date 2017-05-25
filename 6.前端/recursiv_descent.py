from drawTable import drawTable

global current
global inputString

def advance():
	global current
	current = inputString.pop(0) #pop默认退最后一个
	
def A():		

	if (current == '+' or current == '-'):
		advance()
		return True
	else:
		return False

def M():						 
	if (current == '*' or current == '/'):
		advance()
		return True
	else:
		return False
			
def F():						# ok
	if (current =='('):
		advance()
		if(E()):   # E
			if(current == ')'):
				advance()
				return True
	elif(current =='i'):
		advance()
		return True	
	return False
	
def T_():

	if(current == '*' or current =='/'):
		if(M()):
			if(F()):
				if(T_()):
					return True
	elif(current ==')' or current =='#' or current =='+' or current =='-'):
		# advance()       不确定
		return True
	return False	
		
def T():
	if(current =='i' or current =='('):
		if (F()):
			if(T_()):
				return True
	return False
		
def E_():

	if(current =='+' or current =='-'):
		if (A()):
			if(T()):
				if (E_()):
					return True
					
	elif(current ==')' or current =='#'):
		return True
	return False
	
def E():
	
	if(current =='i' or current =='('):
		if(T()):
			if(E_()):
				return '匹配成功'		
	return '匹配失败'			

def main(string):
	global current
	global inputString 	
	inputString = list(string)
	
	inputString.append('#')
	current=inputString.pop(0)
	return E()
		

if __name__ == '__main__':
    main()	