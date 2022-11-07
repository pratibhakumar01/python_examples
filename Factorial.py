#This Program calculates factorial of a number

num = 0
count = 0
Factorial = 1

num = int(input("Enter the Number:"))

count = num

for i in range(num):
    Factorial = Factorial*count
    count = count-1

print ("Factorial of: ",num," is ", Factorial)