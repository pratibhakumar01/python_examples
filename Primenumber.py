# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 21:19:39 2022

@author: prati

print("My name is Pratibha")
print("I have two kids, they are in high school.\
     One of them is 15 years old and the second\
     one is 17 years old. My daughter is a\
     senior and she is applying for college.")

# This Program takes input from the user for three items and calculates the 
# total

item_1 = int(input("Enter value of item_1"))
item_2 = int(input("Enter value oe item_2"))
item_3 = int(input("Enter value oe item_3"))
total = item_1 + item_2 + item_3
print("The total is :", total)
"""
Input = int(input("Enter value of the number: ", ))

div_range = Input // 2

print(Input, div_range)

prime = True

for i in range(2, div_range):
    temp = Input % i
    if temp == 0:
        print(Input, " is a not a prime number")
        prime = False
        break
if prime == True:
    print("The number is prime")
