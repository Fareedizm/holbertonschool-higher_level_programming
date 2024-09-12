#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # Extract elements or default to 0 if not available
    a1, a2 = tuple_a[0] if len(tuple_a) > 0 else 0, tuple_a[1] if len(tuple_a) > 1 else 0
    b1, b2 = tuple_b[0] if len(tuple_b) > 0 else 0, tuple_b[1] if len(tuple_b) > 1 else 0
    
    # Return the tuple with the sums of the corresponding elements
    return (a1 + b1, a2 + b2)
