def reverseBits(n):
    return int(bin(n)[2:].zfill(32)[::-1],2)

print reverseBits(43261596)
