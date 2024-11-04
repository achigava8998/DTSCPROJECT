#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Reserarch Project: College Affordability
#Group 16: Ash Chigavazira, Lasya Maddula, Daniil Gavrilov, Precious Gilbert, Zack Baldorado 


# In[ ]:


#Research Question: Do colleges with higher tuition rates have higher graduation rates?


# In[ ]:


#Independent Variable (Cost of Attendance) vs Dependent Variable (Graduation Rates)


# In[29]:


import pandas as pd
import numpy as np
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.stats.outliers_influence import variance_inflation_factor


# In[30]:


data= pd.read_csv(r"C:\Users\preci\OneDrive\Documents\School\Data and Society\Projects\College_Data (1).csv")
data


# In[49]:


#visualtization Scatter plot
plt.figure(figsize = (10,6))
plt.scatter(data['Outstate'],data['Grad.Rate'], color= 'indigo')
plt.xlabel('Out Of State Tuition Costs')
plt.ylabel('Graduation Rate')
plt.title("Graduation Rates vs Tuition Costs")


# In[83]:


# Scatter plot matrix to observe relationships for public vs private 
private_data = data.loc[data['Private'] == 'Yes']
print(private_data)
#next compare the graduation rate between public vs private, maybe use different colored data points, also add a linear model line 


# In[87]:


plt.figure(figure = (8,6))
plt.scatter(private_data['Outstate'],private_data['Grad.Rate'])
plt.xlabel('Out Of State Tuition Costs')
plt.ylabel('Graduation Rate')
plt.title("Private School Graduation Rates vs Tuition Costs")
plt.show()


# In[ ]:




