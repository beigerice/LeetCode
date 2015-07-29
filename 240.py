class Solution:
    def searchMatrix(self, matrix, target):
        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False
        top = 0
        bottom = len(matrix)-1
        while matrix[top][-1] < target:
            top += 1
        while matrix[bottom][0] > target:
            bottom -= 1
        for i in xrange(top,bottom+1):
            low = 0
            high = len(matrix[0])-1
            while low <= high:
                mid = (low+high)//2
                midVal = matrix[i][mid]
                if midVal < target:
                    low = mid+1
                elif midVal > target:
                    high = mid-1
                else:
                    return True
        return False


a = Solution()
print a.searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]],27)
