#!/usr/bin/env python
# coding: utf-8

# In this assignment you will experiment on your own. Using a health dataset of your choice (check with us if you are not sure), write code to demonstrate the following Pandas functions:<br />
# 
# Melt<br />
# Pivot<br />
# Aggregation<br />
# Iteration<br />
# Groupby<br />

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


breast_cancer = pd.read_csv('breast-cancer.data')

# got column names from .data file:
column_names = ["class", "age", "menopause", "tumor_size", "inv_nodes", "node_caps", "deg-malig", "breast", "breast_quad", "irradiat"]

# add column names to df for analysis:
df = pd.read_csv("breast-cancer.data", names = column_names)


# In[12]:


df.head(20)


# In[10]:


# make age and tumor size categorical, so they're ordered correctly
df['age']=pd.Categorical(df['age'],['20-29', '30-39', '40-49', '50-59', '60-69', '70-79'])

df['tumor_size']=pd.Categorical(df['tumor_size'],["0-4", "5-9", "10-14", "15-19", "20-24", "25-29", "30-34", "35-39", "40-44", "45-49", "50-54"])


# In[18]:


# Melt the dataframe to look only at tumor size for each individual.
df_melt = df.reset_index().melt(id_vars='index', value_vars = ['tumor_size'],
                 value_name = 'tumor size')

df_melt.head(10)


# In[24]:


# can make density/violin plot after melting:
df_melt['tumor size']=pd.Categorical(df_melt['tumor size'],["0-4", "5-9", "10-14", "15-19", "20-24", "25-29", "30-34", "35-39", "40-44", "45-49", "50-54"])

sns.violinplot(data=df_melt, x="tumor size", y="index")

# source: https://seaborn.pydata.org/generated/seaborn.violinplot.html


# In[25]:


# restructure dataframe so that the columns are tumor size, and the values in the frame are age.
df_pivot = df.pivot(columns='tumor_size', values = 'age')
print(df_pivot)


# In[26]:


# restructure dataframe so that the columns are tumor size, and the values in the frame are tumor location (breast quadrant).
df.pivot(columns='tumor_size', values = 'breast_quad')


# In[28]:


# Aggregate the min and max values of the numerical columns:

# gotta rever to NOT categorical before I can do this:
df2 = pd.read_csv("breast-cancer.data", names = column_names)

df2.aggregate({"age":['min', 'max'],
              "tumor_size": ['min', 'max'],
              "inv_nodes": ['min', 'max'],
              "deg-malig": ['min', 'max']})


# In[29]:


# Iterate through the column names to get a list of the variables included in this data set:
# source: https://www.tutorialspoint.com/python_pandas/python_pandas_iteration.htm
df_iter = pd.DataFrame(df)
for col in df:
    print(col)


# In[30]:


# Compare average degree of malignancy by age group
df_byage = df.groupby(['age']).mean(['deg-malig'])
df_byage.head()


# In[31]:


# Compare average degree of malignancy varies by class
df_byclass = df.groupby(['class']).mean(['deg-malig'])
df_byclass.head()


# In[32]:


# Determine the class distribution of breast cancer cases included in this data set
df.groupby(['class']).count()


# In[33]:


# Determine the distribution of tumor location in this data set
df.groupby(['breast_quad']).count()


# In[ ]:




