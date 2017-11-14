
# coding: utf-8

# In[131]:


# Fangfang Wan
# MACS 30000 Assignment 5, Kaggle Open Call Project, Question 3
# Dataset: Students' Academic Performance Dataset
# Link to website: https://www.kaggle.com/aljarah/xAPI-Edu-Data
import pandas as pd
import matplotlib.pyplot as plt


# In[132]:


student_performance = pd.read_csv('xAPI-Edu-Data.csv')


# In[133]:


student_performance


# In[134]:


H_perf = student_performance['Class'] == "H"


# In[135]:


#Subset - high level student
high_performance = student_performance[H_perf]


# In[136]:


# Count parent education satisfaction of students classified as high level
parent_sat_H = high_performance['ParentschoolSatisfaction'].value_counts()


# In[137]:


parent_sat_H


# In[138]:


M_perf = student_performance['Class'] == "M"


# In[139]:


#Subset - middle level student
mid_performance = student_performance[M_perf]


# In[140]:


# Count parent education satisfaction of students classified as middle level
parent_sat_M = mid_performance['ParentschoolSatisfaction'].value_counts()


# In[141]:


parent_sat_M


# In[142]:


L_perf = student_performance['Class'] == "L"


# In[143]:


#Subset - low level student
low_performance = student_performance[L_perf]


# In[144]:


# Count parent education satisfaction of students classified as low level
parent_sat_L = low_performance['ParentschoolSatisfaction'].value_counts()


# In[145]:


parent_sat_L


# In[146]:


# Plot the parents' satisfaction (Good or Bad) of education for students classified as high level
parent_sat_H.plot("bar")
plt.title('Parent satisfaction of High level students', fontsize=10)
plt.xlabel('Satisfaction')
plt.ylabel('Frequency')


# In[147]:


plt.show()


# In[148]:


# Plot the parents' satisfaction (Good or Bad) of education for students classified as middle level
parent_sat_M.plot("bar")
plt.title('Parent satisfaction of Middle level students', fontsize=10)
plt.xlabel('Satisfaction')
plt.ylabel('Frequency')


# In[149]:


plt.show()


# In[150]:


# Plot the parents' satisfaction (Good or Bad) of education for students classified as low level
parent_sat_L.plot("bar")
plt.title('Parent satisfaction of Low level students', fontsize=10)
plt.xlabel('Satisfaction')
plt.ylabel('Frequency')


# In[151]:


plt.show()


# In[ ]:


# References: 
# The pandas library. https://classes.cs.uchicago.edu/archive/2017/fall/12100-1/lecture-examples/Pandas/Pandas.html

