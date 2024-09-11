#!/usr/bin/python3
def multiple_returns(sentence):
    # Get the length of the string
    length = len(sentence)

    # Check if the string is empty
    if length == 0:
        first_char = None
    else:
        # Get the first character of the string
        first_char = sentence[0]

    # Return the tuple with length and first character (or None)
    return (length, first_char)
