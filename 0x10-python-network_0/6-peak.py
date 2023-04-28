#!/user/bin/python3
#A function that finds a peak in a list of unsorted integers
def find_peak(list_of_integers):
    """Finds the peak in a list of unsorted integers"""
    left = 0
    right = len(list_of_integers) - 1

    while left < right:
        midpoint = (left + right) // 2

        if list_of_integers[midpoint] < list_of_integers[midpoint + 1]:
            left = midpoint + 1

        else:
            right = midpoint
        return list_of_integers[left]
