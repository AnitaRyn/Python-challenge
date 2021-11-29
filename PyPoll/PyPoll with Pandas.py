#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[7]:


df = pd.read_csv('election_data.csv')
df.head(10)


# In[8]:


df.tail()


# In[9]:


df["Candidate"].unique()


# In[10]:


df.agg(totals =('Candidate', pd.Series.nunique))


# In[11]:


df.groupby(['Candidate']).agg(number_votes=('Voter ID',pd.Series.nunique)).sort_values('number_votes',ascending=False)


# In[ ]:




