#!/usr/bin/env python
# coding: utf-8

# In[4]:


def swap(string):
    start=string[0]
    end=string[-1]
    swapped_string=end+string[1:-1]+start
    print("string after swapping: ",swapped_string)
a=input("Enter a string: ")
swap(a)


# In[ ]:




