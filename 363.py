class Solution(object):
    def maxSumSubmatrix(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        result = -(2**32)
        m = len(matrix)
        n = len(matrix[0])
        M = max(m,n)
        N = min(m,n)
        for i in range(N):
            temp = [0]*M
            for j in range(i,N):
                for x in range(len(temp)):
                    if m > n:
                        temp[x] += matrix[x][j]
                    else:
                        temp[x] += matrix[j][x]
                sums = [0]
                nums = [0]
                for x in range(len(temp)):
                    sums.append(temp[x]+sums[-1])
                    idx1 = bisect.bisect_left(nums,sums[-1]-k)
                    if idx1 < len(nums):
                        result = max(result,sums[-1]-nums[idx1])
                    bisect.insort(nums,sums[-1])
        return result
                    
            
