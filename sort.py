import ast
import csv
import random


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
    
def test():
    print(insertion_sort([5, 3, 8, 4, 2]) == [2, 3, 4, 5, 8])
    print(insertion_sort([1]) == [1])
    print(insertion_sort([]) == [])
    
    sorted_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print("\nTesting binary_search...")
    print(binary_search(5, sorted_array) == True)
    print(binary_search(10, sorted_array) == False)

    print("\nTesting binary_sort_search_member...")
    print(binary_sort_search_member(4, [5, 3, 8, 4, 2]) == True)
    print(binary_sort_search_member(10, [1, 2, 3, 4, 5]) == False)

def save_test_cases_to_csv(test_cases, filename="random_tests.csv"):
    """Saves test cases to a CSV file where each line contains: array, key, expected_result."""
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Array", "Key", "Expected Result"])
        for array, key, expected_result in test_cases:
            writer.writerow([array, key, expected_result])

def read_test_cases_from_csv(filename="random_tests.csv"):
    """Reads test cases from a CSV file and reconstructs the test case list."""
    test_cases = []
    with open(filename, "r", newline="") as f:
        reader = csv.reader(f)
        next(reader) 
        for row in reader:
            # print(f"row: {row}")
            array = ast.literal_eval(row[0]) 
            key = int(row[1])
            expected_result = bool(int(row[2]))
            # print((array, key, expected_result))
            test_cases.append((array, key, expected_result))
    return test_cases

def random_test_generator(N, num_test_cases):
    """
    In this test we generate an array of size N randomly by treating the array as our 1st variable 
    and the key as the second variable
    """
    test_cases = []
    value_range = [-50, 50]
    for i in range(num_test_cases):
        array = random.choices(range(value_range[0], value_range[1] + 1), k=N)
        key = random.choice(range(value_range[0], value_range[1] + 1))
        expected_result = 0
        for item in array:
            if key == item:
                expected_result=1
                break
        test_cases.append((array, key, expected_result))
    return test_cases

def create_random_test_cases(N, num_test_cases):
    test_cases = random_test_generator(N, num_test_cases)
    save_test_cases_to_csv(test_cases, filename="random_tests.csv")


def run_tests(test_cases):
    num_cases = 0
    num_failed_cases = 0 
    for t in test_cases:
        array = t[0]
        key = t[1]
        expected_result = t[2]
        actual_result = binary_sort_search_member(key, array)
        num_cases+=1
        if expected_result != actual_result:
            num_failed_cases+=1
    return num_cases, num_failed_cases

# test()    
num_test_cases = 1000
N=5
# create_random_test_cases(N, num_test_cases)
test_cases = read_test_cases_from_csv()
num_cases, num_failed_cases = run_tests(test_cases)
print(f"Num cases: {num_cases}")
print(f"Num failed cases: {num_failed_cases}")