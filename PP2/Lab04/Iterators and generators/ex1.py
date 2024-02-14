def squares(N):
    a=(i**2 for i in range(1,N+1))
    for i in a:
        print(i)
N=int(input())
squares(N)