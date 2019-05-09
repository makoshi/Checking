# -*- coding: utf-8 -*-
"""
Created on Thu May  2 00:27:44 2019

@author: hamza
"""

print("Calculator") 
a= int(input("enter first number = "))
b= int(input("enter second number = "))
c= input("enter operator what you want  + , - , * , / .")
if c =='+':
   print (a+b)
elif c =='-':
  print (a-b)
elif c =='*':
  print (a*b)
elif c =='/':
  print (a/b)
else:
print("enter a valid operator") 
