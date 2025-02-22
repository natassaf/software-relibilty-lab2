import ast
import csv


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