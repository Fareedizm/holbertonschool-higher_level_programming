#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    # Initialize the result list
    result = []
    
    # Iterate through each integer in the input list
    for num in my_list:
        # Check if the integer is divisible by 2
        if num % 2 == 0:
            result.append(True)
        else:
            result.append(False)
    
    # Return the list of boolean values
    return result
