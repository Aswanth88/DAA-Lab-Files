n, d = list(map(int, input().split()))
data_list = []

for _ in range(n):
    day, lectures, curses = list(map(int, input().split()))
    data_list.append([day, lectures, curses])

def custom_sort(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - 1):
            if arr[j][2] < arr[j + 1][2]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def calculate_curse(arr):
    curse_total = 0
    current_schedule = []

    for day_number in range(1, d + 1):
        day_schedule = [entry for entry in arr if entry[0] == day_number]
        
        current_schedule += day_schedule
        current_schedule = custom_sort(current_schedule)
        
        if current_schedule:
            current_schedule[0][1] -= 1
        
        current_schedule += [[1, 0, 0] for _ in range(len(current_schedule))]
        current_schedule = [entry for entry in current_schedule if entry[1] > 0]

    for entry in current_schedule:
        if entry[1] > 0:
            curse_total += entry[2] * entry[1]

    print("Minimum total curse achievable", curse_total)

calculate_curse(data_list)
