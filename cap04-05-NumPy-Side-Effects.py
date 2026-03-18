#NumPy Side Effects
#numpy is great for doing vector arithmetic. If you compare its functionality with regular Python lists, however, some things are different.

#First, numpy arrays cannot contain elements with different types. If you mix types, like booleans and integers, numpy automatically converts them to a common type. Booleans like True and False are treated as 1 and 0 when combined with numbers, so the array ends up as integers.

#Second, the typical arithmetic operators, such as +, -, * and / have a different meaning for regular Python lists and numpy arrays.

#Select the code that results in the following output:

#np.array([True, 1, 2]) + np.array([3, 4, False])
#The numpy package is already imported as np. You can run each option in the IPython Shell to see the output.

#answer:

#np.array([4, 3, 0]) + np.array([0, 2, 2])
