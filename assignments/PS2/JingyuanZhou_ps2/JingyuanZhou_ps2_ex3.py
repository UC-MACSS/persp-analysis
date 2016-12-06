import numpy as np
import pandas as pd
from pandas import Series, DataFrame
'''
------------------------------------------------------------------------
Exercise a: 
------------------------------------------------------------------------
'''

A = np.array([[0, 2, 4], [1, 3, 5]])
B = np.array([[3, 0, 0], [3, 3, 0], [3, 3, 3]])
C = np.array([[-2, 0, 0], [0, -2, 0], [0, 0, -2]])


def ipmstack (A, B, C):
	'''
	--------------------------------------------------------------------
	This function creates a stacked matrix from A, B, C
	--------------------------------------------------------------------
	INPUTS:
	A,B,C = matrices specified in the question

	OTHER FUNCTIONS AND FILES CALLED BY THIS FUNCTION: None

	OBJECTS CREATED WITHIN THIS FUNCTION:
	line_1 = matrix, the first line of stakced matrix
	line_2 = matrix, the second line of stakced matrix
	line_3 = matrix, the third line of stakced matrix

	FILES CREATED BY THIS FUNCTION: None

	RETURNS: np.vstack((line_1, line_2, line_3))
	--------------------------------------------------------------------
	'''
	line_1 = np.hstack(( np.zeros((3,3), dtype=np.int),A.T,np.identity(3, dtype= np.int)))
	line_2 = np.hstack((A, np.zeros((2,2), dtype =np.int), np.zeros((2,3), dtype = np.int)))
	line_3 = np.hstack((B, np.zeros((3,2), dtype =np.int),C))
	return np.vstack((line_1, line_2, line_3))

print(ipmstack (A, B, C))


'''
------------------------------------------------------------------------
Exercise b(i): 
------------------------------------------------------------------------
'''
#Make a data frame without the first four lines
#make both gender and age index columns of the DataFrame
#relabel the values of the gender variable to 0=both, 1=male, 2=female
#exclude the lines with age = 999
df = pd.read_csv('popagesex2015.csv', \
				 header = 0,\
				 names = ['gender', 'age', 'pop10', 'pop11', 'pop12', 'pop13', 'pop14', 'pop15'],\
				 index_col=['gender','age'], \
				 skiprows = [0, 1, 2, 3], \
				 converters ={'gender': lambda x:str(x).replace('0','both').replace('1','male').replace('2','female')})\
				 .drop(999,axis=0,level='age')
print("Result of b(i) is:")
print(df)


'''
------------------------------------------------------------------------
Exercise b(ii): 
------------------------------------------------------------------------
'''
s_grouped = df.drop('both', axis = 0, level='gender').reset_index().drop('age',1).groupby(['gender']).sum().apply(lambda x: x/x.sum())
print()
print("Result of b(ii) is:")
print(s_grouped)

'''
------------------------------------------------------------------------
Exercise b(iii): 
------------------------------------------------------------------------
'''
a_grouped = df.drop('both', axis = 0, level='gender').reset_index().drop('gender',1).groupby(['age']).sum().apply(lambda x: x/x.sum()).T.mean().iloc[:]
#print(type(a_grouped))
print()
print("Result of b(iii) is:")
print(a_grouped)

