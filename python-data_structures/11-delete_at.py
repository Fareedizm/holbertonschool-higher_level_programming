#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    
    # Check if the index is valid
    if idx < 0 or idx >= len(my_list):
        return my_list
    
    # Create a new list excluding the item at the specified index
    new_list = my_list
    new_list.remove(new_list[idx])
    
    return new_list
