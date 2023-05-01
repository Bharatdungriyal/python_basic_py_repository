#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np


# In[50]:


df = pd.read_csv("Downloads/indian.csv")
df


# In[30]:


df.index


# In[33]:


df.columns


# In[37]:


df.describe()


# In[38]:


df.head(4)


# In[59]:


df.tail(5)


# In[52]:


df.to_csv("indian.csv", index= False)
df


# In[42]:


df


# In[46]:


df = pd.read_csv("Downloads/indian.csv")


# In[47]:


df


# In[52]:


df.info()


# In[61]:


df.min()


# In[62]:


df.max()


# In[106]:


df = pd.read_csv("Downloads/indian.csv")
df


# In[108]:


df=df.rename(columns={"death":"total death","state":"states new"})
df


# In[110]:


df = pd.read_csv("Downloads/indian.csv")
df


# In[112]:


df.state== "IN"


# In[113]:


df.state


# In[115]:


df["state"][0]


# In[116]:


df["state"][0]= "nepal"


# In[117]:


df


# In[139]:


df.iloc[1,4]= None 
# for changing something wihtout name of rows columns


# In[135]:


df


# In[166]:


df.loc[3,"state"]= None


# In[167]:


df


# In[164]:


df.loc[3,"deathConfirmed"]= None


# In[165]:


df

