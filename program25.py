#!/usr/bin/env python
# coding: utf-8

# In[7]:


a=input("Enter a string: ")
print("The original string is:",str(a))
k='$'
res=a[0]+a[1:].replace(a[0],k)
print("replaced string: "+str(res))


# In[ ]:




