#!/usr/bin/env python
# coding: utf-8

# In[39]:


import pandas as pd
import numpy as np
import seaborn as sns                       #visualisation
import matplotlib.pyplot as plt             #visualisation
get_ipython().run_line_magic('matplotlib', 'inline')
sns.set(color_codes=True)


# In[3]:


df = pd.read_csv("retail_sales_dataset.csv")
# To display the top 5 rows 
df.head(5) 


# In[4]:


df.tail(5)


# In[5]:


df.dtypes


# In[11]:


df = df.drop(['Age'], axis=1)
df.head(5)


# In[12]:


df = df.rename(columns={"Transaction ID": "Transaction ID", "Customer ID": "Customer ID", "product category": "product category", "Quantity": "Quantity", "Price per Unit": "price per unit", "Total Amount": "total amount" })
df.head(5)


# In[13]:


df.shape


# In[14]:


duplicate_rows_df = df[df.duplicated()]
print("number of duplicate rows: ", duplicate_rows_df.shape)


# In[15]:


df.count()


# In[16]:


df = df.drop_duplicates()
df.head(5)


# In[17]:


df.count()


# In[18]:


print(df.isnull().sum())


# In[19]:


df = df.dropna()    # Dropping the missing values.
df.count()


# In[20]:


print(df.isnull().sum())


# In[21]:


sns.boxplot(x=df['total amount'])


# In[24]:


sns.boxplot(x=df['Quantity'])


# In[25]:


sns.boxplot(x=df['price per unit'])


# In[32]:


df.Quantity.value_counts().nlargest(40).plot(kind='bar', figsize=(5,5))
plt.title("Number of products sold")
plt.ylabel('Product Category')
plt.xlabel('price per unit');


# In[37]:


fig, ax = plt.subplots(figsize=(6,6))
ax.scatter(df['Product Category'], df['total amount'])
ax.set_xlabel('Product Category')
ax.set_ylabel('total amount')
plt.show()


# In[ ]:




