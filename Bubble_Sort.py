def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

if __name__ == '__main__':
    n = int(input("Enter total number of elements: "))
    arr = []
    print("Enter elements:")
    for _ in range(n):
        element = int(input())
        arr.append(element)

    bubble_sort(arr)

    print("\nSorted array:")
    for element in arr:
        print(element)