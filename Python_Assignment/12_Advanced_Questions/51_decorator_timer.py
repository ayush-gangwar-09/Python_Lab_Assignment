# Question 1: Create a decorator to measure function execution time.

import time


def calculate_time(function):
    # This wrapper runs the original function and measures its time.
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = function(*args, **kwargs)
        end_time = time.time()

        print("Execution time:", round(end_time - start_time, 4), "seconds")
        return result

    return wrapper


@calculate_time
def find_sum(limit):
    total = 0
    for number in range(1, limit + 1):
        total = total + number
    return total


number = int(input("Enter the limit: "))
print("Sum:", find_sum(number))
