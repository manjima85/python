#!/usr/bin/env python
# coding: utf-8

# In[2]:


a=int(input("enter a number"))
i=2
flag=False
for i in range(2,a):
     if(a%i==0):
            flag=True    
            break
if flag:
       print(a,"is not a prime number")
else:
        print(a,"is a prime number")     


# In[ ]:




