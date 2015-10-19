class Solution(object):
    def fourSum(self, nums, target):
        result = {}
        dic = {}
        refer = {}
        for i in xrange(len(nums)):
            refer[nums[i]] = refer.get(nums[i],0)+1
            for j in xrange(i+1,len(nums)):
                if nums[i]+nums[j] in dic:
                    dic[nums[i]+nums[j]].append([nums[i],nums[j]])
                else:
                    dic[nums[i]+nums[j]] = [[nums[i],nums[j]]]
        dup = {}
        for k,v in dic.iteritems():
            if k not in dup and target-k in dic:
                dup[k] = 1
                dup[target-k] = 1
                for a in v:
                    for b in dic[target-k]:
                        temp = {}
                        temp[a[0]] = temp.get(a[0],0)+1
                        temp[a[1]] = temp.get(a[1],0)+1
                        temp[b[0]] = temp.get(b[0],0)+1
                        temp[b[1]] = temp.get(b[1],0)+1
                        for key in temp:
                            if temp[key] > refer[key]:
                                break
                        else:
                            result[tuple(sorted([a[0],a[1],b[0],b[1]]))] = 1
        toreturn = []
        for k in result:
            toreturn.append(list(k))
        return toreturn
