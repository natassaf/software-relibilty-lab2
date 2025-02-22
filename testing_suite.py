import random

from algorithms_with_errors import binary_sort_search_member_error_1, binary_sort_search_member_error_2, binary_sort_search_member_error_3, binary_sort_search_member_error_4, binary_sort_search_member_error_5, binary_sort_search_member_error_6
from utils import save_test_cases_to_csv


# def test():
#     print(insertion_sort([5, 3, 8, 4, 2]) == [2, 3, 4, 5, 8])
#     print(insertion_sort([1]) == [1])
#     print(insertion_sort([]) == [])
    
#     sorted_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#     print("\nTesting binary_search...")
#     print(binary_search(5, sorted_array) == True)
#     print(binary_search(10, sorted_array) == False)

#     print("\nTesting binary_sort_search_member...")
#     print(binary_sort_search_member(4, [5, 3, 8, 4, 2]) == True)
#     print(binary_sort_search_member(10, [1, 2, 3, 4, 5]) == False)


def generate_pairwise_test_cases(num_elements, lowest, highest):
    original_values = [random.randint(lowest, highest) for _ in range(num_elements)]
    mutated_values = []
    test_cases = []

    for i in range(num_elements):
        new_value = random.randint(lowest, highest)
        while new_value == original_values[i]:
            new_value = random.randint(lowest, highest)
        mutated_values.append(new_value)
    
    random_index = random.randint(0, len(original_values)-1)
    search_key = original_values[random_index]
    expected_result = True
    test_cases.append((original_values, search_key, expected_result))
    
    for i in range(num_elements):
        new_test_case = original_values[:i] + [mutated_values[i]] + original_values[i+1:]
        random_index = random.randint(0, len(new_test_case)-1)
        search_key = new_test_case[random_index]

        test_cases.append((new_test_case, search_key, True))
    
    for i in range(num_elements):
        for j in range(i + 1, num_elements):
            new_test_case = (
                original_values[:i] + [mutated_values[i]] +
                original_values[i+1:j] + [mutated_values[j]] +
                original_values[j+1:]
            )
            new_test_case = original_values[:i] + [mutated_values[i]] + original_values[i+1:]
            random_index = random.randint(0, len(new_test_case)-1)
            search_key = new_test_case[random_index]
            test_cases.append((new_test_case, search_key, True))
    
    
    return test_cases

def random_test_generator(num_elements, lowest_value, highest_value):
    """
    In this test we generate an array of size N randomly by treating the array as our 1st variable 
    and the key as the second variable
    """
    value_range = [lowest_value, highest_value]

    array = random.choices(range(value_range[0], value_range[1] + 1), k=num_elements)
    key = random.choice(range(value_range[0], value_range[1] + 1))
    expected_result = 0
    for item in array:
        if key == item:
            expected_result=1
            break
    test_case = (array, key, expected_result)
    return test_case

# def create_random_test_cases(N, num_test_cases):
#     test_cases = random_test_generator(N, num_test_cases)
#     save_test_cases_to_csv(test_cases, filename="random_tests.csv")


# def run_tests(test_cases, func_to_test):
#     num_cases = 0
#     num_failed_cases = 0 
#     for t in test_cases:
#         array = t[0]
#         key = t[1]
#         expected_result = t[2]
#         actual_result = func_to_test(key, array)
#         num_cases+=1
#         if expected_result != actual_result:
#             num_failed_cases+=1
#     return num_cases, num_failed_cases

def run_check(test_case, func)->bool:
    array = test_case[0]
    key = test_case[1]
    expected_result = test_case[2]
    result = func(key, array)
    found_error = True  if (result != expected_result) else False
    return found_error
    

def run_experiment(N, lowest_value, highest_value):
    """
        Run random test generator and pairwise test generator and return how many cases 
        needed to be generated by each to track all ingected errors. 
        Store the test cases while while running
    """

    def print_status_random():
        print("********************************************")
        print(f"flag_error_1_random is {flag_error_1_random}")
        print(f"flag_error_2_random is {flag_error_2_random}")
        print(f"flag_error_3_random is {flag_error_3_random}")
        print(f"flag_error_4_random is {flag_error_4_random}")
        print(f"flag_error_5_random is {flag_error_5_random}")
        print(f"flag_error_6_random is {flag_error_6_random}")
        print("***************************************************")

    def print_status_pairwise():
        print(f"flag_error_1_pairwise is {flag_error_1_pairwise}")
        print(f"flag_error_2_pairwise is {flag_error_2_pairwise}")
        print(f"flag_error_3_pairwise is {flag_error_3_pairwise}")
        print(f"flag_error_4_pairwise is {flag_error_4_pairwise}")
        print(f"flag_error_5_pairwise is {flag_error_5_pairwise}")
        print(f"flag_error_6_pairwise is {flag_error_6_pairwise}")

     
    # Initialization
    flag_error_1_random = False
    flag_error_2_random = False
    flag_error_3_random = False
    flag_error_4_random = False
    flag_error_5_random = False
    flag_error_6_random = False

    flag_error_1_pairwise = False
    flag_error_2_pairwise = False
    flag_error_3_pairwise = False
    flag_error_4_pairwise = False
    flag_error_5_pairwise = False
    flag_error_6_pairwise = False

    flag_random = False
    flag_pairwise = False

    # # Running experiment
    test_cases_random = []
    i = 0
    while not flag_random:
        test_case = random_test_generator(N, lowest_value, highest_value )
        assert len(test_case)==3
        flag_error_1_random = run_check(test_case, binary_sort_search_member_error_1) if flag_error_1_random==False else True
        flag_error_2_random = run_check(test_case, binary_sort_search_member_error_2) if flag_error_2_random==False else True
        flag_error_3_random = run_check(test_case, binary_sort_search_member_error_3) if flag_error_3_random==False else True
        flag_error_4_random = run_check(test_case, binary_sort_search_member_error_4) if flag_error_4_random==False else True
        flag_error_5_random = run_check(test_case, binary_sort_search_member_error_5) if flag_error_5_random==False else True
        flag_error_6_random = run_check(test_case, binary_sort_search_member_error_6) if flag_error_6_random==False else True

        test_cases_random.append(test_case)
        flag_random = flag_error_1_random & flag_error_2_random & flag_error_3_random & flag_error_4_random & flag_error_5_random & flag_error_6_random
        flag_random = flag_error_1_random & flag_error_2_random & flag_error_3_random
        i += 1
        if i % 10000 == 0:
            print_status_random()

    test_cases_pairwise = []
    i = 0
    while not flag_pairwise:
        test_cases = generate_pairwise_test_cases(N, lowest_value, highest_value)
        for test_case in test_cases:
            assert len(test_case)==3
            flag_error_1_pairwise = run_check(test_case, binary_sort_search_member_error_1) if flag_error_1_pairwise==False else True
            flag_error_2_pairwise = run_check(test_case, binary_sort_search_member_error_2) if flag_error_2_pairwise==False else True
            flag_error_3_pairwise = run_check(test_case, binary_sort_search_member_error_3) if flag_error_3_pairwise==False else True
            flag_error_4_pairwise = run_check(test_case, binary_sort_search_member_error_4) if flag_error_4_pairwise==False else True
            flag_error_5_pairwise = run_check(test_case, binary_sort_search_member_error_5) if flag_error_5_pairwise==False else True
            flag_error_6_pairwise = run_check(test_case, binary_sort_search_member_error_6) if flag_error_6_pairwise==False else True


        test_cases_pairwise.extend(test_cases)
        flag_pairwise = flag_error_1_pairwise & flag_error_2_pairwise & flag_error_3_pairwise & flag_error_4_pairwise & flag_error_5_pairwise & flag_error_6_pairwise
        i += 1
        if i % 10000 == 0:
            print_status_pairwise()
    save_test_cases_to_csv(test_cases_random, filename="random_tests.csv")
    save_test_cases_to_csv(test_cases_pairwise, filename="pairwise_tests.csv")
    return (len(test_cases_random), len(test_cases_pairwise))



lowest_value = -10000
highest_value = 10000
N = 20

num_cases_random, num_cases_pairwise = run_experiment(N, lowest_value, highest_value)

print(f"Num elements is {N}")
print(f"Values' range in the array is: {[lowest_value, highest_value]}")
print(f"Num cases random: {num_cases_random}")
print(f"Num cases pairwise: {num_cases_pairwise}")