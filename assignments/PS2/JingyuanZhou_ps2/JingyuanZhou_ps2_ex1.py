import numpy as np
import pandas as pd


'''
------------------------------------------------------------------------
Exercise 1: 
------------------------------------------------------------------------
'''
#a
def firsthalf(string):
	'''
	--------------------------------------------------------------------
	This function cuts the first half of the string.
	--------------------------------------------------------------------
	INPUTS:
	string = string argument passed into function

	OTHER FUNCTIONS AND FILES CALLED BY THIS FUNCTION: None

	OBJECTS CREATED WITHIN THIS FUNCTION: size
	size = int, size of the string

	FILES CREATED BY THIS FUNCTION: None

	RETURNS: string[:size//2]
	--------------------------------------------------------------------
	'''
	size = len(string)
	return string[:size//2]

#b
def backward(string):
    '''
    --------------------------------------------------------------------
    This function reverses  string.
    --------------------------------------------------------------------
    INPUTS:
    string = string argument passed into function

    OTHER FUNCTIONS AND FILES CALLED BY THIS FUNCTION: None

    OBJECTS CREATED WITHIN THIS FUNCTION: None

    FILES CREATED BY THIS FUNCTION: None

    RETURNS: sting[-1::-1]
    --------------------------------------------------------------------
    '''
    return string[-1::-1]

#c
def pig_latin(string):
    '''
    --------------------------------------------------------------------
    This function converts a string to its pig latin version.
    --------------------------------------------------------------------
    INPUTS:
    string = string argument passed into function

    OTHER FUNCTIONS AND FILES CALLED BY THIS FUNCTION: None

    OBJECTS CREATED WITHIN THIS FUNCTION: 
    c = int, an accumulative counting integer for the number of consonants in the string
    pl = string, the translated pig_latin of the input string

    FILES CREATED BY THIS FUNCTION: None
    
    RETURNS: pl
    --------------------------------------------------------------------
    '''
    if string[0].lower() in ("a", "e", "i", "o", "u"):
        pl = string[1:] + "hay"
    else:
        c = 0
        for i in string:
            if i.lower() not in ("a", "e", "i", "o", "u"):
                c += 1
            else:
                break
        pl = string[c:]+string[:c]+"ay"
    return pl


#d
def max_value(grid):
    '''
    --------------------------------------------------------------------
    This function finds the greatest product of four adjacent numbers in\
    the same direction in the grid.
    --------------------------------------------------------------------
    INPUTS:
    grid = data passed into function
    
    OTHER FUNCTIONS AND FILES CALLED BY THIS FUNCTION: None
    
    OBJECTS CREATED WITHIN THIS FUNCTION: 
    a = matrix, matrix of products of four adjacent numbers in horizontal direction
    b = matrix, matrix of products of four adjacent numbers in vertical direction
    c = matrix, matrix of products of four adjacent numbers in positively sloped diagonal direction
    d = matrix, matrix of products of four adjacent numbers in negatively sloped diagonal direction
    
    FILES CREATED BY THIS FUNCTION: None

    RETURNS: maximum of all values in a, b, c, d
    --------------------------------------------------------------------
    '''
	
    a = grid[:17, :]*grid[1:18, :]*grid[2:19,:]*grid[3:,:]
    b = grid[:, :17]*grid[:,1:18]*grid[:,2:19]*grid[:,3:]
    c = grid[:17, :17]*grid[1:18,1:18]*grid[2:19,2:19]*grid[3:,3:]
    d = grid[3:,:17]*grid[2:19,1:18]*grid[1:18, 2:19]*grid[:17,3:]

    return max([a.max(),b.max(), c.max(), d.max()])

grid = np.load('grid.npy')
print("The greatest product of four adjacent numbers in the same direction in the grid is", max_value(grid))



