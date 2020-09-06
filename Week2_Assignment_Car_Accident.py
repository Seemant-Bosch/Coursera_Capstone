#!/usr/bin/env python
# coding: utf-8

# # Capstone Project - Car accident severity (Week 1)
# ### Applied Data Science Capstone by IBM/Coursera

# ## Table of contents
# * [Introduction: Business Problem](#introduction)
# * [Data](#data)
# * [Methodology](#methodology)
# * [Conclusion](#conclusion)

# ## Inroduction <a name="introduction"></a>
# For this Caston Project which come under my IBM certification course, I would like to perform the Data Analysis of **Road accident data** with purpose of checking corelation of Road Accident at different conditions of **Road**, **Weather** and **Light**. The data was collected by the Seattle Police Department, recorded by Traffic Records and provided by Coursera via a download link. The time period for this data starts from 2004 and consist 194,673 observations and 38 variables.
# The main purpose of doing this analysis is to help transportation department in understanding the situation in transparent way improve the decision making to reduce accidents in the future.

# ## Data <a name="data"></a>
# 
# As mentioned in Inroduction part, our Data Set contailns 38 variables and 194673 data entry. we will use **SEVERITYCODE** as our dependent variable Y and try different combinations of independent variables X to see the impact of Inependent Variable on dependent one.

# ## Methodology <a name="methodology"></a>
# 
# For making the analysis Our decision making will be maily based upon below situation:
# * Different Weather Conditions
# * Differenet Road Conditions
# * Different Light Conditions
# 
# We are going to consider seriverty as dependent variable (Y) and all the above 3 variables will act as independent (X). We will check the total count of accident happened in 3 different conditions. As first data Visualisation point of view we just going to create bar garph between X and Y. Later Data will be cleaned and analysed

# In[6]:


get_ipython().run_cell_magic('capture', '', '! pip install seaborn')


# In[7]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns


# In[5]:


print(df.dtypes)


# In[6]:


df_Weather = df['WEATHER'].value_counts().to_frame()
df_Weather.plot(kind='bar')
plt.title("The total number of car accidents during different Weather condition",fontsize= 15)


# ### Inference
# Maximum accident has happened during clear weather conditions

# In[7]:


df_Roadcond = df['ROADCOND'].value_counts().to_frame()
df_Roadcond.plot(kind='bar')
plt.title("The total number of car accidents during different Road condition",fontsize= 15)


# ### Inference
# Maximum accident has happened during Dry Road conditions

# In[13]:


df_Lightcond = df['LIGHTCOND'].value_counts().to_frame()
df_Lightcond.plot(kind='bar')
plt.title("The total number of car accidents during different Light condition",fontsize= 15)


# ### Inference
# Maximum accident has happened during daylight conditions

# ## Conclusion <a name="conclusion"></a>
# As you can see above the road accidents are mainly happening in clear wether conditions with dry road condition. This also make sense because drivers take more attention during driving if weather conditions are bad. Also in Day lights more accidents are happening.
