import copy
from algorithms import binary_search, insertion_sort


def insertion_sort_with_error_1(array):
    " We iterate up to  len(array)-1 instead of len(array)"
    index = 1
    while index < len(array)-1: # error
        current_position = index
        while (current_position > 0) and (array[current_position] < array[current_position - 1]):
            temp = array[current_position]
            array[current_position] = array[current_position - 1]
            array[current_position - 1] = temp
            current_position -= 1
        index += 1
    return array

def insertion_sort_with_error_2(array):
    """
    Here we don't use a temp variable before mutating the items
    """
    index = 1
    while index < len(array):
        current_position = index
        while (current_position > 0) and (array[current_position] < array[current_position - 1]):
            array[current_position] = array[current_position - 1] 
            array[current_position - 1] = array[current_position] # error
            current_position -= 1
        index += 1
    return array

def insertion_sort_with_error_3(array):
    """
    The error is doing the index increase too early
    """
    index = 1
    while index < len(array)-1: # error
        index += 1 # error
        current_position = index
        while (current_position > 0) and (array[current_position] < array[current_position - 1]):
            temp = array[current_position]
            array[current_position] = array[current_position - 1]
            array[current_position - 1] = temp
            current_position -= 1
        
    return array

def binary_search_with_error_1(key, array):
    """
    In this faulty implementation  we start the right variable from len(array) -2 
    instead of len(array) - 1
    """
    left = 0
    right = len(array) - 2 # error
    mid = (left + right) // 2

    while array[mid] != key and left <= right:
        if array[mid] < key:
            left = mid + 1
        else:
            right = mid - 1
        mid = (left + right) // 2

    return array[mid] == key

def binary_search_with_error_2(key, array):
    """
    In this faulty implementation  we introduce two errors
    """
    left = 0
    right = len(array) - 2 # error 
    mid = (left + right) // 2

    while array[mid] != key and left <= right:
        if array[mid] < key:
            left = mid + 2 # error
        else:
            right = mid - 2 # error
        mid = (left + right) // 2

    return array[mid] == key

# Six errors in binary_sort_search_member

def binary_sort_search_member_error_1(key, array):
    sorted_array = insertion_sort(array)
    # print(sorted_array)
    return binary_search_with_error_1(key, sorted_array)

def binary_sort_search_member_error_2(key, array):
    sorted_array = insertion_sort_with_error_1(array)
    # print(sorted_array)
    return binary_search(key, sorted_array)

def binary_sort_search_member_error_3(key, array):
    sorted_array = insertion_sort_with_error_2(array)
    # print(sorted_array)
    return binary_search(key, sorted_array)
    
def binary_sort_search_member_error_4(key, array):
    sorted_array = insertion_sort_with_error_3(array)
    # print(sorted_array)
    return binary_search(key, sorted_array)

def binary_sort_search_member_error_5(key, array):
    sorted_array = insertion_sort(array)
    # print(sorted_array)
    return binary_search_with_error_2(key, sorted_array)

def binary_sort_search_member_error_6(key, array):
    """
    Integration error case
    """
    sorted_array = insertion_sort(copy.copy(array))
    # print(sorted_array)
    return binary_search_with_error_2(key, array)