def convert(s, nRows):
    temp = ['']*nRows
    result = ''
    if nRows == 1:
        return s
    else:
        for j in range(len(s)):
            if j%(2*nRows-2) < nRows:
                temp[j%(2*nRows-2)] += s[j]
            else:
                temp[2*nRows-2-j%(2*nRows-2)] += s[j]
        for l in temp:
            result += l
        return result

print convert('PAYPALISHIRING',3)
