# O(min(m,n)⋅(m+n)) O(min(m,n))
def gcdOfStrings(str1: str, str2: str) -> str:
  
    def isDivisor(l):
        if len1%l or len2%l:
            return False
        f1, f2 = len1//l, len2//l
        return str1[:l]*f1 == str1 and str1[:l]*f2 == str2

    len1, len2 = len(str1), len(str2)
    for l in range(min(len1, len2), 0, -1):
        if isDivisor(l):
            return str1[:l]

    return ""


def gcdOfStrings(str1: str, str2: str) -> str:
    # check if they have non-zero GCD string.
    if str1 + str2 != str2 + str1:
        return ""

    # get the GCD of the two lengths.
    max_length = gcd(len(str1), len(str2))
    return str1[:max_length]
