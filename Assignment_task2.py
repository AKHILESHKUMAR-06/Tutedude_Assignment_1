#!/usr/bin/python3

import time
 
t = time.localtime(time.time())
localtime = time.asctime(t)
str = "Current Time:" + time.asctime(t)
 
print(str)
# Task 1: Perform Basic Mathmatical Operation
# 1. Take two number as input form the user.
# input is taken as string , so we conver it to float 
num1 = float(input("Enter the frist number: "))
num2 = float(input("Enter the second number: "))

#perform the basic mathmatical operation
addition = num1 + num2
substraction = num1 - num2
multiplication = num1*num2
devision = num1/num2

#3. Displays the results of each operation on the screen.
print(f"Addition: {addition}")
print(f"Subtraction: {subtraction}")
print(f"Multiplication: {multiply}")
print(f"Division: {divide}")
