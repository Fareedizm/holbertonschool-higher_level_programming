#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    # Check if index is valid
    if idx < 0 or idx >= len(my_list):
        return my_list
    
    # Create a new list excluding the item at index idx
    new_list = my_list
    new_list.pop(idx)
    
    return new_list
