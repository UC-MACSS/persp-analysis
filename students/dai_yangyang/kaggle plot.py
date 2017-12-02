# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 15:53:50 2017

@author: 1995b
"""

#Plot:
import matplotlib.pyplot as plt
%matplotlib inline
import random
import numpy as np
import pandas as pd

#read csv file
titanic_df = pd.read_csv(r'C:\Users\1995b\OneDrive\Documents\persp-analysis\students\dai_yangyang\train.csv')
#group the survivor rate by class and sex
class_sex_grouping = titanic_df.groupby(['Pclass','Sex']).mean()
#plot the histogram of survival rate grouped by different sex and class
class_sex_grouping['Survived'].plot.bar()
plt.title('Titanic survival rate by class and sex')