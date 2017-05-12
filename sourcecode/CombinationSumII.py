class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        end = len(candidates) - 1
        if end < 0 :
            return None
        l = []
        self.getCombinationSum(candidates,end,target,l,None)
        r = []
        for i in l:
            i.sort()
            if i not in r:
                r.append(i)
        return r
    def getCombinationSum(self,candidates,end,target,l,last):
        if end == -1:
            return 
        if last == None:
            last = []
        num = candidates[end]
        if target < num:
            return self.getCombinationSum(candidates,end - 1, target, l, last)
        elif target == num:
            last1 = last[0:len(last)]
            last.append(num)
            l.append(last)
            self.getCombinationSum(candidates,end-1, target, l, last1)
        else:
            last1 = last[0:len(last)]
            last2 = last[0:len(last)]
            last1.append(num)
            self.getCombinationSum(candidates,end - 1, target - num, l, last1)
            self.getCombinationSum(candidates,end - 1, target, l, last)
if __name__ == "__main__":
    s = Solution()
    a = [10, 1, 2, 7, 6, 1, 5]
    b = 8
    r = s.combinationSum2(a,b)
    print r
