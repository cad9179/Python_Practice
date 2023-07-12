#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
# turn jupyter notebook warnings off
import warnings
warnings.filterwarnings("ignore")


# In[2]:


df1 = pd.DataFrame({'tradeid':range(5),'profit':range(1000,2000,200)})
df2 = pd.DataFrame({'tradeid':range(2,7,1), 'stock':   ['APL','MST','JNJ','TSL','BAB']})
display(df1)
display(df2)


# In[3]:


pd.concat([df1,df2],axis=0).drop_duplicates(subset='tradeid',keep=False)


# In[6]:


diff = set(df1.tradeid).symmetric_difference(set(df2.tradeid))


# In[7]:


pd.concat([df1.loc[df1['tradeid'].isin(list(diff)),:],df2.loc[df2['tradeid'].isin(list(diff)),:]])


# In[10]:


diff = np.setxor1d(np.array(df1.tradeid), np.array(df2.tradeid))
pd.concat([df1.loc[df1['tradeid'].isin(list(diff)),:],df2.loc[df2['tradeid'].isin(list(diff)),:]])


# In[11]:


df1 = pd.DataFrame({'tradeid':[0,2,2,3,4],'profit':range(1000,2000,200)})
df2 = pd.DataFrame({'tradeid':[2,3,4,5,5], 'stock':['APL','MST','JNJ','TSL','BAB']})
display(df1)
display(df2)


# In[13]:


df3 = df1.merge(df2, on='tradeid', how='outer', indicator=True)
display(df3)
df3 = df3.loc[df3["_merge"] != 'both', :]
# cleanup to make df3 our final result
del df3["_merge"]
df3

