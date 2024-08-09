x=2
y=3
z=4

# print(x+y)
# print(x-y)
# print(x*y)
# print(x**y)
# print(x%y)

# print(x+y*z) # Incorrect format
# 14

# print(x+(y*z)) , Correct format
# 14

# Operator Overloading in python
# print('Chai'+'code') 
# Outputs: Chaicode

w = x,y,z # when no. are called like this they return a tuple.
# print(w) 
# Outputs: (2,3,4)

w = x+1,y+3,z-1
# print(w) 
# Outputs: (3,6,3)

# print(2**1000)
#10715086071862673209484250490600018105614048117055336074437503883703510511249361224931983788156958581275946729175531468251871452856923140435984577574698574803934567774824230985421074605062371141877954182153046474983581941267398767559165543946077062914571196477686542167660429831652624386837205668069376

# print(1<2)
# Outputs: True

# print(1>2)
# Outputs: False

# print(x<y<z) # Incorrect Method
# Outputs : True

# print(x<y and y<z) # correct Method
# Outputs : True

import math
# print(math.floor(3.5)) # Outputs: 3
# print(math.floor(-3.5)) # Outputs: -4
# print(math.ceil(3.5))# Outputs: 4
# print(math.ceil(-3.5)) # Outputs: -3
# print(math.trunc(3.5)) # Outputs: 3
# print(math.trunc(-3.5)) # Outputs: -3

# difference between Floor, ceil and trunc:
# floor : rounds to the bottom number
# ceil : rounds to the upper number
# trunc : rounds up to the nearest number from zero

import random
print(random.random()) # Gives arandom no. between 0 to 1 in decimals.
# Outputs : 0.4533803262094569
print(random.randint(1,11))
# Outputs : 10

list1 = ['Yellow','Red','Blue','Green']
print(list1)
# Outputs : ['Yellow', 'Red', 'Blue', 'Green'] || Orignal list

# print(random.choice(list1))
# Outputs : Red

random.shuffle(list1)
# print(list1)
# Outputs : ['Green', 'Blue', 'Yellow', 'Red']  || Stuffle list

setone = {1,2,3,4}
settwo = {3,4,5,6}
print(setone & settwo) # & = intersection: it gives common elements between two sets
# Outputs : {3, 4}
print(setone | settwo) # | = Union: Gives all the elements of both sets but does not repeat
# Outputs : {1,2,3,4,5,6}
print(setone - settwo) # - means difference(a-b): gives the elements in b that arre not present in a
# Outputs: {5,6}

# Empty set is denoted as set() and not {}
# Because '{}' indicates empty dictionary
