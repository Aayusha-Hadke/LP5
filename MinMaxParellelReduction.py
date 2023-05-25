import numpy as np

def min_reduction(arr):
    return np.min(arr)

def max_reduction(arr):
    return np.max(arr)

def sum_reduction(arr):
    return np.sum(arr)

def average_reduction(arr):
    return np.mean(arr)

if __name__ == '__main__':
    n = int(input("Enter total number of elements: "))
    arr = np.empty(n, dtype=int)
    print("Enter elements:")
    for i in range(n):
        arr[i] = int(input())

    min_value = min_reduction(arr)
    max_value = max_reduction(arr)
    sum_value = sum_reduction(arr)
    average_value = average_reduction(arr)

    print("Minimum value:", min_value)
    print("Maximum value:", max_value)
    print("Sum:", sum_value)
    print("Average:", average_value)
