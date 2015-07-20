def largestNumber(num):
    result = ''
    def sub_sort(temp,low,high) :
        key = num[low]
        while low < high :
            while low < high and int(str(key)+str(num[high])) <= int(str(num[high])+str(key)) :
                high -= 1
            while low < high and int(str(key)+str(num[high])) > int(str(num[high])+str(key)) :
                num[low] = num[high]
                low += 1
                num[high] = num[low]
        num[low] = key
        return low

    def quick_sort(num,low,high) :
        if low < high :
            key_index = sub_sort(num,low,high)
            quick_sort(num,low,key_index)
            quick_sort(num,key_index+1,high)
            
    quick_sort(num,0,len(num)-1)
    for i in range(0, len(num)):
        result += str(num[len(num)-i-1])
    return str(int(result))

print largestNumber([0,0,0,0])

