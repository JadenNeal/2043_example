def quick_sort(arr):
    """
    Sorts an array using the Quick Sort algorithm.
    """
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


def binary_search(arr, target):
    """
    Performs a binary search on a sorted array to find the target value.
    Returns the index of the target if found, otherwise -1.
    """
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


# Example usage:
if __name__ == "__main__":
    data = [3, 6, 8, 10, 1, 2, 1]
    sorted_data = quick_sort(data)
    print("Sorted Data:", sorted_data)

    target = 10
    index = binary_search(sorted_data, target)
    if index != -1:
        print(f"Target {target} found at index {index}.")
    else:
        print(f"Target {target} not found.")