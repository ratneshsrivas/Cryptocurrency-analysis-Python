#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


eth_df = pd.read_csv('ETH-USD.csv')


# In[3]:


yfi_df=pd.read_csv('YFI-USD.csv')


# In[4]:


btc_df = pd.read_csv('BTC-USD (1).csv')


# In[5]:


#Adding a new column for currency denoting Bitcoin symbol
btc_df.insert(0,'Currency','BTC')


# In[6]:


#Adding a new column for currency denoting Etherium symbol
eth_df.insert(0,'Currency','ETH')


# In[7]:


#Adding a new column for currency denoting Yearn Finance symbol
yfi_df.insert(0,'Currency','YFI')


# In[8]:


#print the first five rows of ETH, BTC, YFI


# In[9]:


eth_df.head()


# In[10]:


btc_df.head(5)


# In[11]:


yfi_df.head(5)


# In[12]:


eth_df.head(5)


# In[13]:


# Renaming some columns for better understanding


# In[14]:


mapper = {'Open':'24h Open(USD)','High':'24h High(USD)','Low':'24h Low(USD)','Close':'Closing Price(USD)'}


# In[15]:


btc_df.rename(columns=mapper,inplace=True)


# In[16]:


eth_df.rename(columns=mapper,inplace=True)


# In[17]:


yfi_df.rename(columns=mapper,inplace=True)


# In[ ]:





# In[18]:


# Creating a data frame which contains the closing price of all three cryptos


# In[19]:


closing_df = pd.DataFrame({'BTC':btc_df['Closing Price(USD)'],
                          'ETH':eth_df['Closing Price(USD)'],
                          'YFI':yfi_df['Closing Price(USD)']})


# In[20]:


closing_df


# In[21]:


# Stats on data 


# In[22]:


closing_df.describe()


# In[23]:


# Visualizing the cryptos closing price


# In[24]:


import matplotlib.pyplot as plt
plt.style.available
plt.style.use('ggplot')


# In[25]:



plt.figure(figsize= (13,7))
for x in closing_df.columns.values:
    plt.plot(closing_df[x],label= x)
    
    plt.title('Cryptos Closing Graph')
    plt.xlabel('Days')
    plt.ylabel('Closing Price(USD)')
    plt.legend()


# In[26]:


# Scaling the data
from sklearn import preprocessing
min_max_scaler = preprocessing.MinMaxScaler(feature_range=(0,450))

scaled = min_max_scaler.fit_transform(closing_df)
scaled


# In[27]:


scaled_df = pd.DataFrame(scaled,columns=closing_df.columns)


# In[28]:


# Visualizing the scaled data


# In[29]:


plt.figure(figsize=(13,7))
for y in scaled_df.columns.values:
    plt.plot(scaled_df[y],label =y,linewidth=2, alpha= .6)
    
    plt.title('Cryptos scaled data graph')
    plt.xlabel('Days')
    plt.ylabel('Scaled Price(USD)')
    plt.legend()


# In[30]:


# Daily returns


# In[31]:


return_df = closing_df.pct_change()
return_df


# In[32]:


# visualizing the daily returns


# In[49]:


print('From the chart below it can be easily inferred that Yearn.Finance has given the maximum daily returns')
plt.figure(figsize=(13,7))
for z in return_df.columns.values:
    plt.plot(return_df.index ,return_df[z],label=z,linewidth =3,alpha= .8)
    plt.title('Daily Returns')
    plt.xlabel('Days')
    plt.ylabel('Percentage in decimal')
    plt.legend()


# In[34]:


# Risk Factor(Volatility)


# In[35]:


print('risk factor')
return_df.std()


# In[36]:


# Daily returns vs the daily volatility


# In[37]:


print('Quite surprising that Etherium is more stable than Bitcoin, and between Bitcoin and Yearn Finance, the latter one is less volatile and gives  higher returns')
return_df.mean()


# In[38]:


return_df.corr()


# In[39]:


# Visualizing the correlation


# In[40]:


import seaborn as sns
plt.subplots(figsize=(6,5))
sns.heatmap(return_df.corr(),annot = True,fmt = '.3%')
plt.show()


# In[41]:


# Daily cumulative simple returns


# In[42]:


cum_daily_returns = (return_df+1).cumprod()
cum_daily_returns


# In[43]:


# Visualize the daily cumulative simple returns


# In[44]:


plt.figure(figsize=(13,7))
for a in cum_daily_returns.columns.values:
    plt.plot(cum_daily_returns.index,cum_daily_returns[a], label=a, linewidth=2)
    plt.title('Daily Cumulative Returns')
    plt.xlabel('Days')
    plt.ylabel('Growth of a Dollar investment')
    plt.legend()
    plt.show()
    

    
   


# In[45]:


# Exceptional returns


# In[48]:


cum_daily_returns.boxplot()
plt.title('boxplot of daily returns')
plt.show()


# In[51]:


# Thank You


# In[ ]:




