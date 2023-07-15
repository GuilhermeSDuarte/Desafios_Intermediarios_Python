T = int(input())

for i in range(T):
    N, K = map(int, input().split())

    resultado = N // K + N % K
    print(N%K)
    print(resultado)