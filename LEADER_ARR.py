def find_leaders(arr):
    n = len(arr)
    leaders = []
    max_from_right = arr[-1]
    leaders.append(max_from_right)
    
    for i in range(n-2, -1, -1):
        if arr[i] > max_from_right:
            leaders.append(arr[i])
            max_from_right = arr[i]
    
    return leaders[::-1]

arr = list(map(int, input("Enter the elements of the array, separated by spaces: ").split()))
result = find_leaders(arr)
print("Leaders:", result)