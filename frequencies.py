"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    # Your code goes here
    itemsList = str(items)
    for k in items:
        if k not in itemsList:
            frequencies[k] = 1
        else:
            frequencies[k] += 1
    return frequencies
