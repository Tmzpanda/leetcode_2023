def reverseBits(n: int) -> int:    # 00000000 00000000 00000000 00000101 
    res = 0
    for i in range(32):
        bit = (n >> i) & 1
        res = res | (bit << (31 - i))    # 10100000 00000000 00000000 00000000

    return res
