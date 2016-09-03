class Solution(object):
    def isRectangleCover(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: bool
        """
        ref = set()
        dic = {}
        ll = [2**32,2**32]
        ur = [0,0]
        area = 0
        for rectangle in rectangles:
            if rectangle[0]<= ll[0] and rectangle[1] <= ll[1]:
                ll = [rectangle[0],rectangle[1]]
            if rectangle[2] >= ur[0] and rectangle[3] >= ur[1]:
                ur = [rectangle[2],rectangle[3]]
            key1 = tuple([rectangle[0],rectangle[1]])
            if tuple(rectangle) not in ref:
                ref.add(tuple(rectangle))
                dic[key1] = dic.get(key1,0)+1
                key2 = tuple([rectangle[2],rectangle[1]])
                dic[key2] = dic.get(key2,0)+1
                key3 = tuple([rectangle[2],rectangle[3]])
                dic[key3] = dic.get(key3,0)+1
                key4 = tuple([rectangle[0],rectangle[3]])
                dic[key4] = dic.get(key4,0)+1
            area += (rectangle[2]-rectangle[0])*(rectangle[3]-rectangle[1])
        if area != (ur[0]-ll[0])*(ur[1]-ll[1]):
            return False
        for k,v in dic.iteritems():
            if k == tuple(ll) or k == tuple(ur):
                continue
            if k == tuple([ll[0],ur[1]]) or k == tuple([ur[0],ll[1]]):
                continue
            if v == 3:
                return False
            if v == 1:
                return False
        return True
