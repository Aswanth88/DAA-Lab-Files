def find_leaders(arr):
    n = len(arr)
    leaders = [arr[n - 1]]

    max_right = arr[n - 1]

    for i in range(n - 2, -1, -1):
        if arr[i] >= max_right:
            leaders.append(arr[i])
            max_right = arr[i]

    return leaders[::-1]  

arr1 = [3, 1, 4, 1, 5, 2, 6, 5, 8]
leaders_result = find_leaders(arr1)
print(leaders_result)
