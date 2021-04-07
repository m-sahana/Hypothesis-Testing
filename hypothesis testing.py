#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import scipy 
from scipy import stats
import statsmodels.stats.descriptivestats as sd


# In[2]:


data=pd.read_csv("D:\projects\Hypothesis testing\LabTAT.csv")


# In[5]:


data.rename(columns={'Laboratory 1':'Lab1'},inplace=True)


# In[6]:


data.rename(columns={'Laboratory 2':'Lab2'},inplace=True)


# In[7]:


data.rename(columns={'Laboratory 3':'Lab3'},inplace=True)


# In[8]:


data.rename(columns={'Laboratory 4':'Lab4'},inplace=True)


# In[9]:


data.head()


# In[10]:


print(stats.shapiro(data.Lab1))
print(stats.shapiro(data.Lab2))
print(stats.shapiro(data.Lab3))
print(stats.shapiro(data.Lab4))


# In[11]:


print(scipy.stats.anderson(data.Lab1,dist = 'norm'))


# In[12]:


print(scipy.stats.anderson(data.Lab2,dist = 'norm'))


# In[13]:


print(scipy.stats.anderson(data.Lab3,dist = 'norm'))


# In[14]:


print(scipy.stats.anderson(data.Lab4,dist = 'norm'))


# In[15]:


scipy.stats.levene(data.Lab1,data.Lab2)


# In[16]:


stats.f_oneway(data.Lab1,data.Lab2)


# In[18]:


scipy.stats.ttest_ind(data.Lab1,data.Lab2,nan_policy='omit')


# In[ ]:




