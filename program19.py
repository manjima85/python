#!/usr/bin/env python
# coding: utf-8

# In[12]:


x=int(input("enter the number"))
n=int(input("enter n"))
s=1
def fact (n):
    f=1
    for i in range(1,(n+1)):
        f=f*i
    return(f)
for i in range(1,n):
        s=s+((x**i)/fact(i))
print("the exponential series is:",s)


# In[ ]:





# In[ ]:




