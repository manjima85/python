#!/usr/bin/env python
# coding: utf-8

# In[3]:


a=int(input("enter upper limit"))
b=int(input("enter lower limit"))
for i in range(a,b):
    if i>1:
        for j in range(2,i):
            if(i%j==0):
                break
        else:
               print(i)


# In[ ]:




