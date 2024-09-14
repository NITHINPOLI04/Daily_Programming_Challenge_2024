def zero_sum_subarrays(arr):
    result = []
    prefix_sum_map = {}
    current_sum = 0 

    for i in range(len(arr)):
        current_sum += arr[i]

        if current_sum == 0:
            result.append((0, i))

        if current_sum in prefix_sum_map:
            for start_index in prefix_sum_map[current_sum]:
                result.append((start_index + 1, i))

        if current_sum in prefix_sum_map:
            prefix_sum_map[current_sum].append(i)
        else:
            prefix_sum_map[current_sum] = [i]

    return result

arr = [1, 2, -3, 3, -1, 2]

print(zero_sum_subarrays(arr))