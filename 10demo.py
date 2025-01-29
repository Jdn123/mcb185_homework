print("hello world") # greeting

"""

note: python3 by itself in terminal allows in terminal python
but data will not be saved

"""

# symbols
print(1.5e-2)
print(1+1)
print(1-1)
print(1*1)
print(1/2)
print(2 ** 2) # exponential
print(5 // 2) # integer divide: round down
print(5 % 2) # remainder of integer divide (5-4) = 1
print(1 + (2/9)) # precedence or order

# general functions
abs(9-20) # absolute value of 9-20 = 11
pow(6, 2) # power: 6^2 = 36
round(17899.1891, ndigits = 3) #rounds decimal: .189 not .1891

# math library functions
import math
math.ceil(189.0001) # round up to 190, integer
math.floor(189.0001) # round down to 189, integer
math.log(1) # natural log
math.log2(1) # log 2
math.log10(1) # log 10
math.sqrt(4) # sqrt of a number
math.pow(2, 2) # same as pow() above
# note you can use pow() or math.pow to do roots
math.pow(27, (1/3)) # returns 3.0
# or use 27 ** (1/3)
math.factorial(8) #factorial

# math library values
math.e # 2.71829 eulers number
math.pi # pi 3.14...
math.inf # prints inf for infinity
math.nan # nan for no number

# python use float point numbers instead of real numbers (except for integers)
print(0.1*3) # 0.30000000000000004
print((1/10)*3) # 0.30000000000000004

# variables
# use a symbol/phrase follow by = sign and value/equation
x = 1
bon = 12
happy = bon*10 + math.pow(x, 1)

#some math.function return floats, check type using 
print(type(bon))
gg = math.ceil(189.0001)
print(type(gg))

#Functions
def pythagoras(a, b):
	return math.sqrt(a**2 + b**2)
	
print(pythagoras(1,1))

hh = pythagoras(4,5)
print(hh) # redundancy

#strings
strg = "Hello"
print(strg, type(strg))

#Conditionals
a = 123
b = 124
if b > a: print('yes')

if b > a:
	print('yes')
	print('b > a')
	
# look at comparison operator table
# >, ==, < 
# !=, >=, <=
# logic: compare a _operator_ to b

def iseven(a):
	if (a % 2) == 0: return True # if there isn't a remainder: return True
	return False # if the if statement does not run, return this

# or use else: return False, but redundant 
a = 2
b = 1

c = a == b
print(c, type(c)) # a is not equal to b: print false, boolean

#if-elif-else structures
if a < b:   print('a < b')
elif a == b: print('a = b')
else: print('a > b') # remaining must be a > b, not need conditional anymore

# note: only the first if gets ran: the rest are conditionals based on the first if
# if you do if: if: if: :: all three if: will get run

#  chaining with and, or, and not
if a < b or a > b: print('yay')
if a < b and a > b: print('impossible')
if not False: print('true') #not False makes it True
if not a == 3: print('nice')

