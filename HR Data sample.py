#!/usr/bin/env python
# coding: utf-8

# In[89]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[90]:


df = pd.read_csv("core_dataset.csv")


# In[91]:


df.info()


# In[92]:


df.head()


# In[93]:


df = df.where(df['Employment Status'] == 'Active')


# In[94]:


df['Department'] = df['Department'].str.strip()


# In[95]:


df['Sex'] = df['Sex'].str.capitalize()


# In[96]:


by_department = pd.pivot_table(df, values='Pay Rate', index=['Department'],
                    columns=['Sex'], aggfunc=np.mean)


# In[97]:


by_department['gap'] = by_department['Male'] - by_department['Female']


# In[106]:


by_department = by_department.sort_values(by=['gap'],ascending=False)
by_department


# In[105]:


by_department['gap'].plot(x='Department',kind='bar')

plt.title("Pay Disparity By Department")
plt.xlabel("Department")
plt.ylabel("Pay Gap From Male to Female")


# In[101]:


by_position = pd.pivot_table(df, values='Pay Rate', index=['Department','Position'],
                    columns=['Sex'], aggfunc=np.mean)
by_position['gap'] = by_position['Male'] - by_position['Female']
by_position = by_position.sort_values(by=['gap'],ascending=False)
by_position


# In[102]:


by_position['gap'].plot(x='Position',kind='bar')

plt.title("Pay Disparity By Position")
plt.xlabel("Position")
plt.ylabel("Pay Gap From Male to Female")

