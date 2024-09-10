def find_missing_number(arr):
    n = len(arr) + 1
    total_sum = n * (n + 1) // 2
    arr_sum = 0
    for num in arr:
        arr_sum += num
    return total_sum - arr_sum
arr = list(map(int, input("Enter the array elements separated by spaces: ").split()))
print("Missing number:", find_missing_number(arr))