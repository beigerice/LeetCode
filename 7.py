def reverse(x):
    if x == 0:
        return 0
    else:
        result = x/abs(x)*int(str(abs(x))[::-1])
        if result > 2147483647 or result < -2147483647:
            return 0
        else:
            return result
    
print reverse(1000000003)
