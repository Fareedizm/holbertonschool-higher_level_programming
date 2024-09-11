#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """Replace an element in the list at a specific position.

    Args:
        my_list (list): The list where the element will be replaced.
        idx (int): The index of the element to replace.
        element: The new element to place at the specified index.

    Returns:
        The modified list if index is valid, otherwise the original list.
    """
    if idx < 0 or idx >= len(my_list):
        return my_list
    my_list[idx] = element
    return my_list
