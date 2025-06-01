# Author : hamid rezaei

def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

nums = [1, 3, 5, 7, 9, 11]
target = int(input("Enter a number: "))

index = binary_search(nums, target)

if index != -1:
    print("Found at", index)
else:
    print("Not found")