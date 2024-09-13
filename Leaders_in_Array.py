def leaders(arr):
    leader_arr = []
    max = float('-inf')
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] > max:
            leader_arr.append(arr[i])
            max = arr[i]
    return leader_arr[::-1]

arr = [100, 50, 20, 10]
print(leaders(arr))