#!/usr/bin/env python3

#from colorama import init
#init()
#from colorama import Fore, Back, Style

import readline
import operator
import math

operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
}

def calculate(myarg):
    stack = list()
    for token in myarg.split():
        try:
            token = int(token)
            stack.append(token)
        except ValueError:
            #function = operators[token]
            #arg2 = stack.pop()
            #arg1 = stack.pop()
            #result = function(arg1, arg2)
            #stack.append(result)
            
            if token == '+':
            	arg2 = stack.pop()
            	arg1 = stack.pop()
            	return arg1 + arg2
            if token == '-':
            	arg1 = stack.pop()
            	arg2 = stack.pop()
            	return arg2 - arg1
            if token == '*':
            	arg1 = stack.pop()
            	arg2 = stack.pop()
            	return arg1 * arg2
            if token == '/':
            	arg1 = stack.pop()
            	arg2 = stack.pop()
            	return arg2 / arg1
            if token == '!':
            	arg1 = stack.pop()
            	return math.factorial(arg1)
            if token == 'sin':
            	arg1 = stack.pop()
            	return math.sin(arg1)
            if token == 'cos':
            	arg = stack.pop()
            	return math.cos(arg)
            if token == 'tan':
            	arg = stack.pop()
            	return math.tan(arg)
            if token == 'copy':
            	arg = stack.pop();
            	stack.append(arg)
            	stack.append(arg)
            	print(stack)
            	size = len(stack)
            	
            	return size
            	
            
        print(stack)
    #if len(stack) != 1:
     #   raise TypeError("Too many parameters")
    #return stack.pop()

def main():
    while True:
        result = calculate(input("rpn calc> "))
        print("Result: ", result)

if __name__ == '__main__':
    main()

    
#deinit()
