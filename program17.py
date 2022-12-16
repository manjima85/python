#!/usr/bin/env python
# coding: utf-8

# In[15]:


def fib(n):
    a=0
    b=1
    if n<0:
        print("Incorrect output")
    elif n==0:
        return a
    elif n==1:
        return b
    else:
         while a<=n:
            print(a)
            c=a+b
            a=b
            b=c
n=int(input("enter the number: "))
fib(num)


# In[ ]:




