def gcd(N, M):

    while M != 0:
        N, M = M, N % M
    return N

def find_lcm(N, M):

    return (N * M) // gcd(N, M)

print(find_lcm(4, 6))
