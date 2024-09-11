#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # Pad tuples with zeros if they have less than 2 elements
    tuple_a = (tuple_a + (0, 0))[:2]
    tuple_b = (tuple_b + (0, 0))[:2]
    
    # Add corresponding elements of the tuples
    result = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    
    return result
