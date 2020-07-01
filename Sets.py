def average(arr):
    arr = set(arr)
    Sum = sum(arr)
    return Sum/len(arr)
    

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)