class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        begin = 0
        end = len(nums) - 1
        while begin <= end:
            middle = (begin + end)/2
            if nums[middle] == target:
                r = middle 
                while r + 1 <= end and nums[r + 1] == target:
                    r += 1
                l = middle 
                while l - 1 >= begin and nums[l - 1] == target:
                    l -= 1
                return [l,r]
            elif nums[middle] > target:
                if middle == 0:
                    return [-1,-1]
                if nums[middle - 1] < target:
                    return [-1,-1]
                end = middle - 1
            else:
                if middle == len(nums) - 1:
                    return [-1,-1]
                if nums[middle + 1] > target:
                    return [-1,-1]
                begin = middle + 1
        return [-1,-1]

if __name__ == "__main__":
    s = Solution()
    a = []
    b = 0
    r = s.searchRange(a,b)
    print r
