# dfs
def numTilings(n: int) -> int:
    MOD = 1_000_000_007

    @cache
    def p(n):
        if n == 2:
            return 1
        return p(n-1) + f(n-2)

    @cache
    def f(n):
        if n <= 2:
            return n
        return f(n-1) + f(n-2) + 2*p(n-1)

    return f(n) % MOD

# dp
def numTilings(n: int) -> int:
    MOD = 1_000_000_007
    if n <= 2:
        return n

    f = [0] * (n + 1) 
    p = [0] * (n + 1) 

    f[1] = 1
    f[2] = 2
    p[2] = 1
    for k in range(3, n + 1):
        f[k] = (f[k - 1] + f[k - 2] + 2 * p[k - 1])
        p[k] = (p[k - 1] + f[k - 2]) 

    return f[n] % MOD


# space optimization
def numTilings(n: int) -> int:
    MOD = 1_000_000_007
    if n <= 2:
        return n

    f = [0] * (n + 1) 
    p = [0] * (n + 1) 

    f_pp = 1
    f_p = 2
    p_p = 1
    for i in range(3, n + 1):
        f_c = (f_p + f_pp + 2 * p_p) 
        p_c = (p_p + f_pp) 

        f_pp = f_p
        f_p = f_c
        p_p = p_c

    return f_c % MOD
