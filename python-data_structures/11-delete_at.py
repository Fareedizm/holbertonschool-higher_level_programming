#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    # Check if the index is valid
    if 0 <= idx < len(my_list):
        # Create a new list excluding the item at the specified index
        new_list = my_list[:idx] + my_list[idx + 1:]
        return new_list
    # If index is invalid, return the list unchanged
    return my_list
