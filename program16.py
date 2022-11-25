#!/usr/bin/env python
# coding: utf-8

# In[5]:


n=int(input("enter a number"))
def sum(n):
    if n<1:
        return n
    else:
        return n+sum(n-1)
print("the sum is",sum(n))


# In[ ]:




