#!/usr/bin/python3
"""Function that finds a peak in a list of unsorted integers."""

def find_peak(list_of_integers):
    """

    """
    if not list_of_integers:
        return None
    start = 0
    stop = len(list_of_integers) - 1
    
    while (start < stop):
        centre = (start + stop) // 2
        if list_of_integers[centre] < list_of_integers[centre + 1]:
            start = centre + 1
        else:
            stop = centre

    return list_of_integers[start]
