#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """Print all integers in the list in reverse order using my_list.reverse().

    Args:
        my_list (list): The list of integers to print.
    """
    my_list.reverse()  # Reverse the list in place
    for item in my_list:
        print("{:d}".format(item))
