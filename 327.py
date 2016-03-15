class Solution(object):
    def countRangeSum(self, nums, lower, upper):
        temp = [0]
        for num in nums:
            temp.append(temp[-1]+num)
        def mergeSort(low,high):
            mid = (low+high)//2
            if mid == low:
                return 0
            count = mergeSort(low,mid)+mergeSort(mid,high)
            i = j = mid
            for left in temp[low:mid]:
                while i < high and temp[i]-left < lower:
                    i += 1
                while j < high and temp[j]-left <= upper:
                    j += 1
                count += j-i
            temp[low:high] = sorted(temp[low:high])
            return count
        return mergeSort(0,len(temp))
