#!/usr/bin/env python
# coding: utf-8

# In[11]:


import cmath
a=int(input("enter the first number: "))
b=int(input("enter the second number: "))
op=int(input("enter the choice: "))
if op==1:
    s=a+b
    print("sum is:",s)
elif op==2:  
    d=a-b
    print("diffrence is:",d)
elif op==3:  
    p=a*b
    print("product is:",p)
elif op==4: 
    q=a/b
    print("quotient is:",q)
elif op==5: 
    r=a%b
    print("remainder is:",r)
elif op==6: 
    e=a**b
    print("power is:",e)
else:
    print("operation not recognised")
    


# In[ ]:





# In[ ]:




