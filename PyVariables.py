# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 08:49:23 2022

@author: prati
"""

#Learning about sting variable
str = "hello world"
print (str)
print(str[0])
print(str[1])
print(str[-1])
print(str[0:5])
print(str[6:9])
print(str[6:10])
print(str[6:])
print(str + "test")
print(len(str))

#Learning about list variable
list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
print(list[0])
print(list[1])
print(list[0][0])
list[1]=1000
print(list)


#Learning about tuple variable
tuple = ( 'abcd', 786 , 2.23, 'john', 70.2  )
tinytuple = (123, 'john')
print (tuple[0])
print (tuple[1:3])
print (tuple[2:])



#Learning about dictionary variable
dict = {}
dict['one'] = "This is one"
dict['two']     = "This is two"
tinydict = {'name': 'john','code':6734, 'dept': 'sales'}
print (dict['one'])
print (tinydict)
print (tinydict.keys())
print (tinydict.values())