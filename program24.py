#!/usr/bin/env python
# coding: utf-8

# In[2]:


def count_occurence(list1,n):
    count=0
    for i in list1:
        for k in i:
            if(k==n):
                count=count+1
    return count
li=[]
n=int(input("enter size of list: "))
for i in range(0,n):
    e=input("enter element of list: ")
    li.append(e)
print("Original list: ",li)
x=input("enter element to be checked list: ")
print(x,"has occured",count_occurence(li,x),"times")


# In[ ]:




