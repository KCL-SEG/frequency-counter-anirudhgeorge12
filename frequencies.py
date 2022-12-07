"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    # Your code goes here
    
    for k in items:
        item = str(k)
        if item not in frequencies.keys():
            frequencies[item] = 1
        else:
            frequencies[item] += 1
    return frequencies
