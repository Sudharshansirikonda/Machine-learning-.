#!/usr/bin/env python
# coding: utf-8

# In[3]:


import statistics
import numpy as np

stock_prices = [12,324,456,8767,2343,36,23,34]
variance = statistics.variance(stock_prices)
variance


# In[ ]:





# In[4]:


numpy_variance = np.var(stock_prices,ddof=1)
numpy_variance


# # SCATTER PLOTS

# In[11]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'temp':[23,64,85,24,86,24,87],
    'ice':[232,445,865,366,467,965,246],
    'adv':[23,54,85,23,89,34,36],
    'cust':[80,231,64,688,32,232,564],
}
df = pd.DataFrame(data)
sns.pairplot(df,diag_kind='kde',markers='o',plot_kws={'alpha':0.7})
plt.suptitle("pair plots if icecream_sales",
             y=1.02,fontsize=16)
plt.show()


# In[ ]:




