# O(min(m,n)⋅(m+n)) O(min(m,n))
def gcdOfStrings(str1: str, str2: str) -> str:
    def isDivisor(a, b, x):
        if a % x or b % x: 
            return False

        f1, f2 = a // x, b // x
        return str1[:x]*f1 == str1 and str1[:x]*f2 == str2

    a, b = len(str1), len(str2)
    for x in range(min(a, b), 0, -1): # greedy
        if isDivisor(a, b, x):
            return str1[:x]

    return ""
