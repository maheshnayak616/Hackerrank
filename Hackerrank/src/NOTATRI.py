__author__ = 'mahesh.nayak'

n = int(raw_input().strip())
while n != 0:
    arr = list(map(int, raw_input().strip().split()))
    arr.sort()
    count = 0

    for i in range(0,n-2):
        k = 0
        for j in range(i+1,n):
            while (k < n and arr[i] + arr[j] < arr[k]):
                if k != i or k!=j:
                    count += 1
    print count
    n = int(raw_input().strip())