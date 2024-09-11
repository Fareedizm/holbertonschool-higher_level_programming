#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if 0 <= idx < len(my_list):
        # Use slicing to create a new list without the item at index idx
        return my_list[:idx] + my_list[idx + 1:]
    # If idx is out of range or negative, return the original list
    return my_list
