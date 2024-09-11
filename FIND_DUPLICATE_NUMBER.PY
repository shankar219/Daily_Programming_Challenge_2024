def find_duplicate(arr):
    low = 1
    high = len(arr) - 1
    
    while low < high:
        mid = (low + high) // 2
        count = 0
        
        for num in arr:
            if num <= mid:
                count += 1
        
        if count > mid:
            high = mid
        else:
            low = mid + 1
    
    return low

def main():
    n_plus_1 = int(input("Enter the number of elements (n+1): "))
    arr = []
    
    print(f"Enter {n_plus_1} elements for the array (each element between 1 and n):")
    
    for i in range(n_plus_1):
        num = int(input())
        arr.append(num)
    
    duplicate = find_duplicate(arr)
    print(f"Duplicate number: {duplicate}")

main()