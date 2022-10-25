N = int(input())
K = int(input())
if K % 2 != 0:
    print(K // 2 + 1)
else:
    print(N // 2 + K // 2)