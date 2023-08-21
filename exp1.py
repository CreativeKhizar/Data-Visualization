#!/usr/bin/env python
# coding: utf-8

# In[28]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv("z:\data.csv")

data


# In[52]:


plt.plot(data["Country"],data["Birth Rate"])
plt.show()


# In[32]:


data.head()


# In[44]:


plt.scatter(data["Country"],data["Birth Rate"])
plt.show()


# In[48]:


plt.hist(data["Birth Rate"])
plt.show()


# In[59]:


plt.bar(data2['Country'],data2['Birth Rate'])
plt.show()


# In[60]:


data2=data.head()

colors=['red', 'blue', 'green', 'orange', 'purple']

labels=['AF','AL','DZ','AD','AO']
plt.pie(data2["Birth Rate"], labels=labels, colors=colors, autopct='%1.1f%%')


# In[61]:


plt.boxplot(data2['Birth Rate'])
plt.show()


# In[ ]:


import seaborn as sb

