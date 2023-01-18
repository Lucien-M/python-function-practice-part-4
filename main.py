#Write a Python function called max_num()to find the maximum of three numbers.
def max_num(a, b, c):
 
    if (a >= b) and (a >= c):
        largest = a
 
    elif (b >= a) and (b >= c):
        largest = b
    else:
        largest = c
         
    return largest
 
# Driven code
a = int(input("Enter First number"))
b = int(input("Enter Second number"))
c = int(input("Enter Third number"))
print(max_num(a, b, c))

#Write a Python function called mult_list() to multiply all the numbers in a list.
def mult_list(numbers):
	prod = 1
	for x in numbers:
		prod *= x
	return prod
# Driver code
list1 = [11, 12, 4, 3]
print(mult_list(list1))

#Write a Python function called rev_string() to reverse a string.

def rev_string(s): 
    str = "" 
    for i in s: 
        str = i + str
    return str
  
s = "Hello world"
  
print("The original string is : ", end="") 
print(s) 
  
print("The reversed string(using loops) is : ", end="") 
print(rev_string(s)) 
#Write a Python function called num_within() to check whether a number falls in a given range.
	#The function accepts the number, beginning of range, and end of range (inclusive) as arguments.
	#Examples: num_within(3,2,4) returns True, num_within(3,1,3) returns True, num_within(10,2,5) returns False.
def num_within(n):
    if n in range(3,9):
        print( " %s is in the range"%str(n))
    else :
        print("The number is outside the given range.")
num_within(5)

#Write a Python function called pascal() that prints out the first n rows of Pascal's triangle.
	#The function accepts the number n, the number of rows to print
	#Note : Pascal's triangle is an arithmetic and geometric figure first imagined by Blaise Pascal. Each number is the two numbers above it added together.

def pascal(n):
   trow = [1]
   y = [0]
   for x in range(max(n,0)):
      print(trow)
      trow=[l+r for l,r in zip(trow+y, y+trow)]
   return n>=1
pascal(5) 
#Sample Pascal's triangle :

# undefined
# Sample output:
# def pascal():
# 	#your code here

# pascal(1)
# '''
# output:
# 1
# '''

# pascal(5)
# '''
# output:
# 1
# 1 1
# 1 2 1
# 1 3 3 1
# 1 4 6 4 1
# '''                                                              
