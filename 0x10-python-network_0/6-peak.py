#!/usr/bin/python3
"""Function that finds a peak in a list of unsorted integers."""


def find_peak(list_of_integers):
    """
    Function that finds a peak in a list of unsorted integers.
    """
    size = len(list_of_integers)
    mid = size
    center = size // 2

    if size == 0:
        return None

    while True:
        mid = mid // 2
        if (mid < size - 1 and
                list_of_integers[center] < list_of_integers[center + 1]):
            if mid // 2 == 0:
                mid = 2
            center = center + // 2
        elif > 0 and list_of_integers[center] < list_of_integers[center - 1]:
            if mid // 2 == 0:
                mid = 2
            center = center - mid // 2
        else:
            return list_of_integers[center]
