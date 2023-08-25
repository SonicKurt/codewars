'''
Highest and Lowest

Author: Kurt Campbell
Created: 25 August 2023
'''

import re

def high_and_low(numbers):
    # Grab each number from the numbers string and store it into an array.
    # NOTE: The below statement will also work. However, you will need to construct
    # a RegEx expression for this statement to work properly.
    # num_array = [int(num) for num in re.findall('-?\d+', numbers)]
    num_array = [int(num) for num in numbers.split(" ")]

    # Sort the numbers in ascending order
    num_array.sort()
    
    # Grab the lowest number and highest number
    low_num = num_array[0]
    high_num = num_array[len(num_array) - 1]

    # Create a string that has the highest number as the first number and the lowest number as the last character.
    return f'{high_num} {low_num}'