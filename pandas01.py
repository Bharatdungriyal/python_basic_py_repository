#!/usr/bin/env python
# coding: utf-8

# Pandas is a open source data analysis library written in python pandas has two type of data structures: a)series:- it's a one dimensional array with indexes,it stores a single column or row of data in a dataframe. b):- it's a tabular spreadsheet like structure reprsenting rows each of which contain one or multiple columns.
# 

# In[1]:


import pandas as pd
import numpy as np

# create a Series with default index
s1 = pd.Series([1, 2, 3, 4, 5])
print(s1)


# In[2]:


import pandas as pd
put_index = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])
print(put_index)


# In[3]:


colors=["red","orange","blue","green","yellow"]
degree=[1,2,3,4,7]
number=[12,34,55,66,74]
newdf= pd.DataFrame({"colors":colors,"degree":degree,"number":number},columns=["colors","degree","number"],index=range(1,6))
newdf


# In[21]:


newdf2 = newdf.copy()


# In[24]:


newdf2[0,"degree"]=8
newdf2


# always use loc funciton for changing values in dataframe
# 

# In[25]:


newdf2.loc[1,"degree"]= 90


# In[26]:


newdf2


# In[33]:


newdf2.iloc[1,0]= "purple"
newdf2.loc[2,"degree"]=2
newdf2


# In[39]:


newdf.sort_index(axis=0,ascending=False)


# In[43]:


newdf2.drop(["number"],axis=1)


# In[44]:


newdf2        # here number is present in dataframe 


# In[48]:


newdf2.drop(["number"],axis=1,inplace=True) 


# for removing any column or row for always,with inplace we can 
# can modify the original dataframe

# In[49]:


newdf2


# In[54]:


newdf.info()


# In[55]:


newdf.describe()


# In[57]:


newdf.iloc[[1,2], :]


# In[58]:


newdf.iloc[: ,[1,2]]


# In[ ]:




