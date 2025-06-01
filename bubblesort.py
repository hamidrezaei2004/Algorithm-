# Author: hamid rezaei

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


# example
numbers = [885, 3, 8843974, 298, 1]
sorted_numbers = bubble_sort(numbers)
print(sorted_numbers)