class Solution(object):
    def lengthLongestPath(self, input):
        arr = input.split('\n')
        if len(arr) == 1 and '.' in input:
            return len(input)
        temp = [arr[0]]
        res = 0
        for i in range(1,len(arr)):
            for j in range(len(arr[i])):
                if arr[i][j] != '\t':
                    cnt = j
                    break
            if cnt > len(temp)-1:
                temp.append(arr[i][cnt:])
            else:
                temp = temp[:cnt+1]
                temp[cnt] = arr[i][cnt:]
            if '.' in arr[i]:
                n = len(temp)-1
                for j in temp:
                    n += len(j)
                res = max(res,n)
        return res
