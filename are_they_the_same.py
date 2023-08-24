'''
Are they the "same"?

Author: Kurt Campbell
Date: 24 August 2023

NOTE: This solution does not work with one test case.
'''

import math

def comp(array1, array2):
    # Check to see if the arrays are None.
    if array1 is None or array2 is None:
        return False
    
    # Check to see if the arrays are the same length.
    if len(array1) != len(array2):
        return False
    
    # Sort the arrays to line up with each instance with the squared
    # counterparts.
    array1.sort()
    array2.sort()
    
    # For each element from array1, square the value and 
    # check to see if the element is in array2.
    # If the element is not in array2, this method will return False
    # to indicate that the given arrays are not the same.
    for i in range(len(array1)):
        # We square the element from array1 to match up with array2.
        squared_amount = array1[i] * array1[i]
        
        if squared_amount != array2[i]:
            return False
    
    # Otherwise, the given arrays are the same.
    return True

a1 = [42, 42]
a2 = [42, 42]

print(comp(a1, a2))