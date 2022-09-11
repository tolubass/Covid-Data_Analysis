#!/usr/bin/env python
# coding: utf-8

# In[202]:


import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[ ]:


df=pd.read_csv("country_wise_latest.csv")


# In[3]:


print(df)


# In[4]:


df.head()


# In[5]:


dl= df.rename(columns={'Country/Region':'Countries','New cases':'New_cases','New deaths':'New_deaths','New recovered':'New_recovered'})


# In[6]:


print(dl)


# In[7]:


dl.head(6)


# In[8]:


dl.describe()


# In[9]:


dl.describe(include = 'all').T


# In[10]:


dl.shape


# In[11]:


dl.size


# In[12]:


dl.dtypes


# In[13]:


dl.info()


# In[14]:


len("countries")


# In[15]:


#knowing the unique values of some columns


# In[16]:


dl['Countries'].unique()


# In[17]:


dl['Confirmed'].unique()


# In[18]:


dl['Deaths'].unique()


# In[19]:


dl['Recovered'].unique()


# In[20]:


#knowing the no of unique value in country


# In[21]:


dl['Countries'].nunique()


# In[22]:


dl.duplicated().sum()


# In[23]:


dl.isnull().sum()


# In[24]:


df['Deaths'].sum()


# In[25]:


df['Confirmed'].sum()


# In[26]:


dl.groupby(['Countries']).sum()


# In[27]:


dl.groupby(['Deaths']).sum()


# In[28]:


grouped = dl.groupby('Countries')
print(grouped['Deaths'].agg(np.mean))
print("\n")


# In[29]:


#checking for outliers


# In[179]:


plt.figure(figsize=(10,5))
plt.boxplot(dl['Deaths'])
plt.grid(False)
plt.show


# In[ ]:





# In[178]:


plt.boxplot(dl['Deaths'], labels=['Deaths'])
plt.title('cleaning values')


# In[ ]:


#Data visualization
#maximum and minimum number of Deaths


# In[36]:


dl.groupby("Countries")["Deaths"].count().max()


# In[37]:


dl.groupby("Countries")["Deaths"].count().min()


# In[38]:


#to get the country that has the highest rate of death and also print out max numbers of each countries


# In[39]:


dlcs = dl.groupby("Countries").sum()
dlcs.sort_values("Deaths", ascending=False ,
inplace =True)
dlcs.head()


# In[ ]:


#the united state has the highest rate of death, then after Brazil and it goes that way down.


# In[169]:


dlcs["Deaths"].head(20).plot.bar(color = 'red', linewidth =1, title = "Countries with the highest rate of death")


# In[41]:


dlcs = dl.groupby("Countries").sum()
dlcs.sort_values("Recovered", ascending=False ,
inplace =True)
dlcs.head()


# In[177]:


dlcs["Recovered"].head(10).plot.bar(title = "Countries with the highest rate of Recovery")


# In[43]:


dlcs = dl.groupby("Countries").sum()
dlcs.sort_values("New_cases", ascending=False ,
inplace =True)
dlcs.head()


# In[173]:


dlcs["Recovered"].head(10).plot.bar(title = "Countries with the highest rate of New_cases")


# In[45]:


dlcs = dl.groupby("Countries").sum()
dlcs.sort_values("Confirmed", ascending=False ,
inplace =True)
dlcs.head()


# In[189]:


dlcs["Recovered"].head(10).plot.bar(color = 'purple', title = "statiscal analysis of recovered cases by each countries")
dlcs["Deaths"].head(10).plot.bar(color = 'red', title = "statiscal analysis of recovered cases by each countries")
plt.legend()
plt.show()


# In[47]:


dlcs = dl.groupby("Countries").sum()
dlcs.sort_values("Active", ascending=False ,
inplace =True)
dlcs.head()


# In[175]:


dlcs["Active"].head(10).plot.bar(title = "Countries with the Active cases")
plt.grid()


# In[ ]:


#correlation between countries deaths, active cases, confirmed cases and recovered cases


# In[ ]:


#new cases to new death


# In[176]:


dlcs["New_cases"].head(10).plot.line(color = 'purple', linewidth = 2, title = "trend of the countries with new cases")
plt.grid()
plt.xticks(rotation=70)
plt.show()


# In[200]:


dlcs["New_deaths"].head(10).plot.line(color = 'red', title = "trend of Countries with the new deaths")
plt.grid()
plt.show()


# In[191]:


#to know the rate of new deaths, new cases and also new recovered in each country


# In[199]:


dlcs["New_cases"].head(10).plot.bar(color = 'blue', title = "the rate of death, new cases and new recovered in each country")
dlcs["Deaths"].head(10).plot.bar(color = 'red', title = "the rate of death, new cases and new recovered in each country")
dlcs["New_recovered"].head(10).plot.bar(color = 'green', title = "the rate of death, new cases and new recovered in each country")
plt.legend()
plt.show()


# In[ ]:




