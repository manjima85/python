#!/usr/bin/env python
# coding: utf-8

# In[3]:


import cmath 
a=int(input("enter the first numbers :"))
b=int(input("enter the second number :"))
c=int(input("enter the third number :"))
d=(b**2)-(4*a*c)
sol1=((-b+cmath.sqrt(d))/2*a)
sol2=((-b-cmath.sqrt(d))/2*a)
print("the solution of quadratic equation are {} and {}".format(sol1,sol2))


# In[ ]:




