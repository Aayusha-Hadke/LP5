def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    # Recursive calls to sort the subarrays
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    
    # Merge the sorted subarrays
    return merge(left_half, right_half)

def merge(left, right):
    merged = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    
    # Add remaining elements of left or right subarray
    merged.extend(left[i:])
    merged.extend(right[j:])
    
    return merged

if __name__ == '__main__':
    n = int(input("Enter total number of elements: "))
    arr = []
    print("Enter elements:")
    for _ in range(n):
        element = int(input())
        arr.append(element)

    sorted_arr = merge_sort(arr)

    print("\nSorted array:")
    for element in sorted_arr:
        print(element)
