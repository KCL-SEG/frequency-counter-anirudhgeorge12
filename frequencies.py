"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    # Your code goes here
    
    for k in items:
        item = str(k)
        if item not in items:
            frequencies[k] = 1
        else:
            frequencies[k] += 1
    return frequencies
