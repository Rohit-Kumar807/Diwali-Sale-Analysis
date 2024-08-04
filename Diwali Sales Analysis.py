#!/usr/bin/env python
# coding: utf-8

# In[39]:


# Import important libraries
import pandas as pd
import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt


# In[41]:


# importing dataset
df = pd.read_csv('Diwali Sales Data.csv', encoding='latin-1')
print(df)


# In[42]:


df.head(10)


# In[43]:


# checking size of data Number of rows and column
df.shape


# In[44]:


df.info()


# In[45]:


# checking null value

df.isnull().sum()


# In[46]:


# drop unneccesary/null column
df.drop(['Status','unnamed1'],axis=1,inplace=True)


# In[53]:


# removing null value of row
df.dropna(inplace=True)


# In[50]:


df.shape


# In[20]:


# checking duplicate values
df.duplicated().sum()


# In[23]:


# dropping duplicates value
df.drop_duplicates(inplace=True)


# In[24]:


# checking data types for each column
df.dtypes


# In[55]:


# changing data type float to integer
df['Amount']=df['Amount'].astype(int)


# In[56]:


df.dtypes


# In[57]:


# getting statical information  of dataset
df.describe()


# In[69]:


# Getting the count of male and female in the data set 
plt.figure(figsize=(7,6))
ax=sns.countplot(x=df['Gender'],data=df,palette='Set1')
for bars in ax.containers:
    ax.bar_label(bars)
plt.xlabel('Gender')
plt.ylabel('No of people')
plt.title("Number of Male and Female")
plt.show()


# In[94]:


# Getting the total amount  by Genders and plot chart
gender_sales=df.groupby(['Gender'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)
gender_sales


# In[107]:


ax=sns.barplot(x='Gender',y='Amount',data=gender_sales)
plt.xlabel('Gender')
plt.ylabel('Total amount')
plt.title('Total amount by Genders')
plt.show()


# In[ ]:


# From above visual we can see that most of the buyers are females and even the purchasing power of females are greater than men


# In[105]:


# getting the count of people by age group and gender
ax=sns.countplot(data=df,x='Age Group',hue='Gender')
for bars in ax.containers:
    ax.bar_label(bars)
plt.title('Count of People by Age Group')
plt.xlabel('Age Group')
plt.ylabel('Count of People')
plt.show()


# In[ ]:


# '''According to this graph we find most of the buyers are of age 26-35 yrs female'''


# In[121]:


# Getting the Total Amount by Age_Group and Gender
sales_age=df.groupby(['Age Group'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)
sales_age


# In[124]:


sns.barplot(x='Age Group',y='Amount',data=sales_age)
plt.title('Total Amount by Age_Group')
plt.show()

# According to above visual  we can see that age_group between 26-35 yrs of people spend much on purchasing

# In[131]:


# Total number of orders from top 10 states
sales_state=df.groupby(['State'],as_index=False)['Orders'].sum().sort_values(by='Orders',ascending=False).head(10)
sns.set(rc={'figure.figsize':(16,6)})
ax=sns.barplot(x='State',y='Orders',data=sales_state)
for bars in ax.containers:
    ax.bar_label(bars)
plt.show()


# In[137]:


# Total amount of orders from top 10 states

amount_sales=df.groupby(['State'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False).head(10)

sns.set(rc={'figure.figsize':(16,6)})
sns.barplot(x='State',y='Amount',data=amount_sales)
plt.show()

# From the above graphs we can see that most of the order & total sales/amount are from Uttarpradesh, Maharashtra and Karnataka
# In[146]:


# Getting the count of people by marital status
plt.figure(figsize=(7,4))
sns.countplot(x='Marital_Status',data=df)
plt.show()


# In[153]:


# Getting the Total amount spent by marital status
Amount_category=df.groupby(['Marital_Status','Gender'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)
plt.figure(figsize=(7,4))
sns.barplot(x='Marital_Status',y='Amount',data=Amount_category,hue='Gender')
plt.show()

From the above graphs we can see that most of the buyers are unmarried(women) and they have high purchasing power
# In[162]:


# Getting the number of orders by their occupations

ax=sns.countplot(x='Occupation',data=df)
sns.set(rc={'figure.figsize':(21,12)})
for bars in ax.containers:
    ax.bar_label(bars)
plt.title('Number of Orders by their Occupations')
plt.xlabel('Occupations')
plt.ylabel('Count of orders')
plt.show()


# In[166]:


# Getting the total amount spent   by their occupation

amount_occupation=df.groupby(['Occupation'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)

sns.barplot(x='Occupation',y='Amount',data=amount_occupation)
plt.title('Total amount by occupations')
plt.xlabel('Occupations')
plt.ylabel('Total Amount')
plt.show()

From the above graph we can see that most of the buyers are working in IT,Healthcare and Aviation
# In[168]:


# Getting the purchasing  count of Product_category by each Product
ax=sns.countplot(x='Product_Category',data=df)
plt.show


# In[170]:


amount_product=df.groupby(['Product_Category'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)

sns.barplot(x='Product_Category',y='Amount',data=amount_product)
plt.title('Total amount by Product_Category')
plt.xlabel('Product_Categorys')
plt.ylabel('Total Amount')
plt.show()

From above graphs we can see that most of the sold products are from Food,Clothing and Electronic category
# In[172]:


# Getting Top 10 Selling products
selling_product=df.groupby(['Product_ID'],as_index=False)['Orders'].sum().sort_values(by='Orders',ascending=False).head(10)

sns.barplot(x='Product_ID',y='Orders',data=selling_product)
plt.title('Top 10 Selling products')
plt.xlabel('Product_ID')
plt.ylabel('Orders')
plt.show()


# In[ ]:


Conclusion

Unmarried Women age group 26-35yrs from Up, Maharashtra and Karnataka working in IT, Healthcare and Aviation are more likely to buy products from Food,
Clothing and Electronics Category


