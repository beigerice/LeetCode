class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dic1,dic2 = {},{}
        result = []
        for num in nums1:
            dic1[num] = dic1.get(num,0)+1
        for num in nums2:
            dic2[num] = dic2.get(num,0)+1
        for k,v in dic1.iteritems():
            if k in dic2:
                for i in range(min(dic1[k],dic2[k])):
                    result.append(k)
        return result        
