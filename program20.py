#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y
print("MENU")
print("-----------------")
print("1.Addition")
print("2.substraction")
print("3.multiplication")
print("4.division")
while True:
    choice=input("Enter choice(1-4):")
    num1=float(input("Enter 1st number: "))
    num2=float(input("Enter 2nd number: "))
    if choice=='1':
        print(num1,"+",num2,"=",add(num1,num2))
    elif choice=='2':
            print(num1,"-",num2,"=",sub(num1,num2))
    elif choice=='3':
            print(num1,"*",num2,"=",mul(num1,num2))
    elif choice=='4':
            print(num1,"/",num2,"=",div(num1,num2))
    else:
            print("invalid input")
x=input("Do you want to continue?(Y/N):") 
if x=="n":
    break
    
            


# In[ ]:




