
def insertion_sort(array):
    index = 1
    while index < len(array):
        current_position = index
        while (current_position > 0) and (array[current_position] < array[current_position - 1]):
            temp = array[current_position]
            array[current_position] = array[current_position - 1]
            array[current_position - 1] = temp
            current_position -= 1
        index += 1
    return array

def binary_search(key, array):
    left = 0
    right = len(array) - 1
    mid = (left + right) // 2

    while array[mid] != key and left <= right:
        if array[mid] < key:
            left = mid + 1
        else:
            right = mid - 1
        mid = (left + right) // 2

    return array[mid] == key

def binary_sort_search_member(key, array):
    sorted_array = insertion_sort(array)
    # print(sorted_array)
    return binary_search(key, sorted_array)
