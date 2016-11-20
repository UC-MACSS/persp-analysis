import numpy as np

#all of which should be less than or equal to three standard deviations 
#away from the mean of the originally input series
def kill_outliers(arr):
	'''
	--------------------------------------------------------------------
	This function removes outliers of the array.
	--------------------------------------------------------------------
	INPUTS:
	arr = a list of numeric values

	OTHER FUNCTIONS AND FILES CALLED BY THIS FUNCTION: None

	OBJECTS CREATED WITHIN THIS FUNCTION:
	mean = float, mean of the list
	sd = float, standard deviation of the list

	FILES CREATED BY THIS FUNCTION: None

	RETURNS: arr
	--------------------------------------------------------------------
	'''
	mean = np.mean(np.array(arr))
	sd = np.std(arr)
	arr = arr[np.logical_and(arr<= mean+3*sd, arr>= mean-3*sd)]
	return arr

#remove outliers for three times
def threescrubs(arr):
	'''
	--------------------------------------------------------------------
	This function removes three sets of outliers of the array.
	--------------------------------------------------------------------
	INPUTS:
	arr = a list of numeric values

	OTHER FUNCTIONS AND FILES CALLED BY THIS FUNCTION: kill_outliers

	OBJECTS CREATED WITHIN THIS FUNCTION: None

	FILES CREATED BY THIS FUNCTION: None

	RETURNS: kill_outliers(kill_outliers(kill_outliers(arr)))
	--------------------------------------------------------------------
	'''

	return kill_outliers(kill_outliers(kill_outliers(arr)))
