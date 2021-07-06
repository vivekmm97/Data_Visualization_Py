#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as n
import matplotlib as mp
import matplotlib.pyplot as mtp
get_ipython().run_line_magic('matplotlib', 'inline')

a = n.arange(40,50)
b = n.arange(50,60)
mtp.xlabel("A-values")
mtp.ylabel("B-values")
mtp.plot(a, b)


# In[4]:


import numpy as n
import matplotlib as mp
import matplotlib.pyplot as mtp
get_ipython().run_line_magic('matplotlib', 'inline')

days = [1,2,3,4,5,6,7]
sales_1 = [160,150,140,145,175,165,180] #Comp.1
sales_2 = [70,90,160,150,140,145,175]  #Comp.2
mtp.xlabel("Days")
mtp.ylabel("Sales")

#mtp.plot(days, sales_1, sales_2) ###this will also work!
mtp.plot(days, sales_1, label = "Comp1")
mtp.plot(days, sales_2, label = "Comp2")
mtp.legend()


# In[16]:


import numpy as n
import matplotlib as mp
import matplotlib.pyplot as mtp
get_ipython().run_line_magic('matplotlib', 'inline')

x = [1,2,3,4]
y1 = [4,3,2,1]
y2 = [10,20,30,40]
y3 = [40,30,20,10]
y4 = [1,2,1,2]
y5 = [40,70,90,70]

mtp.subplot(3, 3, 1)
mtp.plot(x, y1, 'r')
mtp.subplot(3, 3, 2)
mtp.plot(x, y2, 'g')
mtp.subplot(3, 3, 3)
mtp.plot(x, y3, 'y')
mtp.subplot(3, 3, 4)
mtp.plot(x, y4, 'b')
mtp.subplot(3, 3, 5)
mtp.plot(x, y5, 'r')
mtp.subplot(3, 3, 6)
mtp.plot(y2, y1, 'c')
mtp.subplot(3, 3, 7)
mtp.plot(y3, y1, 'g')
mtp.subplot(3, 3, 8)
mtp.plot(y4, y3, 'c')
mtp.subplot(3, 3, 9)
mtp.plot(y5, y1, 'r')


# In[ ]:





# In[ ]:




