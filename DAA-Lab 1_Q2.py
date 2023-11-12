def alternate_sort(arr):
    arr.sort()

    n = len(arr)
    result = []

    for i in range(n // 2):
        result.append(arr[i])
        result.append(arr[n - i - 1])

    if n % 2 != 0:
        result.append(arr[n // 2])

    return result

arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
sorted_alternating_result = alternate_sort(arr)
print(sorted_alternating_result)
