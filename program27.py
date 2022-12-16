#!/usr/bin/env python
# coding: utf-8

# In[1]:


def change(text1,text2):
    first=text1[0]
    second=text2[0]
    a=list(text1)
    b=list(text2)
    a[0]=second
    b[0]=first
    string1="".join(a)
    string2="".join(b)
    find=string1+" "+string2
    return find
word1=input("Enter the 1st word: ")
word2=input("Enter the 2nd word: ")
print("Joined word with swapping letters in 1st position is: ",change(word1,word2))


# In[ ]:




