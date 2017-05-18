global current
global inputString

def advance():
	global current
	current = inputString.pop(0) #pop默认退最后一个
	
def A():						#ok
	if (current == '+' or current == '-'):
		advance()
		return True
	else:
		return False

def M():						#ok
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
					# advance()
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
				return True
	return False			

def main():
	global current
	global inputString 	
	while(1):
		inputString = input("请输入语句(以#结尾)：")
		if(inputString[-1]!='#'):
			continue
		inputString = list(inputString)
		current=inputString.pop(0)
		print(E())
		

if __name__ == '__main__':
    main()	