#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df_excel = pd.read_csv('budget_data.csv')
df_excel


# In[3]:


df_excel.describe()


# In[4]:


df_excel.agg(total=('Profit/Losses',sum)).head()


# In[5]:


df_excel['Profit/Losses'].min()


# In[6]:


df_excel['Profit/Losses'].max()

