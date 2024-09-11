#!/usr/bin/python3
def no_c(my_string):
    # Create a list to store characters that are not 'c' or 'C'
    result_list = []
     # Iterate through each character in the input string
    for char in my_string:
        # Check if the character is not 'c' and not 'C'
        if char != 'c' and char != 'C':
            # Append the character to the result list
            result_list.append(char)
      # Join the list into a single string and return it
    return ''.join(result_list)
