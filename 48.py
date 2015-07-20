class Solution:
    def rotate(self, matrix):
        n = len(matrix)-1
        s = 0
        while s < n-s:
            for i in xrange(s,n-s):
                matrix[s][i],matrix[i][n-s],matrix[n-s][n-i],matrix[n-i][s] = matrix[n-i][s],matrix[s][i],matrix[i][n-s],matrix[n-s][n-i]
            s += 1
        print matrix

a = Solution()
a.rotate([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]])

