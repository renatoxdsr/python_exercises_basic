#Subsetting 2D NumPy Arrays
#If your 2D numpy array has a regular structure, i.e. each row and column has a fixed number of values, complicated ways of subsetting become very easy. Have a look at the code below where the elements "a" and "c" are extracted from a list of lists.

# numpy
#import numpy as np
#np_x = np.array(x)
#np_x[:, 0]
#The indexes before the comma refer to the rows, while those after the comma refer to the columns. The : is for slicing; in this example, it tells Python to include all rows.

#instructions:
#Instructions

#Print out the 50th row of np_baseball.
#Make a new variable, np_weight_lb, containing the entire second column of np_baseball.
#Select the height (first column) of the 124th baseball player in np_baseball and print it out.
import numpy as np

np_baseball = np.array(baseball)

# Print out the 50th row of np_baseball
print(np_baseball[50:])

# Select the entire second column of np_baseball: np_weight_lb
np_weight_lb = np_baseball[:,1];

# Print out height of 124th player
print(np_baseball[:123,]);
