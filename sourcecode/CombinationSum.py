class Solution(object):
    def combinationSum(self, candidates, target):
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
            if i not in r:
                r.append(i)
        return r
    def getCombinationSum(self,candidates,end,target,l,last):
        if last == None:
            last = []
        if target == 0:
            l.append(last)
            return
        num = candidates[end]
        if end == 0 :
            if target%num != 0:
                return 
            else:
                cnt = target/num
                for i in range(cnt):
                    last.append(num)
                l.append(last)
                return
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
            self.getCombinationSum(candidates,end, target - num, l, last1)
            last2.append(num)
            self.getCombinationSum(candidates,end - 1, target - num, l, last2)
            self.getCombinationSum(candidates,end - 1, target, l, last)
if __name__ == "__main__":
    s = Solution()
    a = [2, 3, 6, 7]
    b = 7
    r = s.combinationSum(a,b)
    print r
