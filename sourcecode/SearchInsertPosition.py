class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        begin = 0
        end = len(nums) - 1
        while begin <= end:
            middle = (begin + end)/2
            if nums[middle] == target:
                return middle
            elif nums[middle] > target:
                if middle == 0:
                    return 0
                if nums[middle - 1] < target:
                    return middle
                end = middle - 1
            else:
                if middle == len(nums) - 1:
                    return len(nums)
                if nums[middle + 1] > target:
                    return middle + 1
                begin = middle + 1

if __name__ == "__main__":
    s = Solution()
    a = [1,3,5,6]
    b = 4
    r = s.searchInsert(a,b)
    print r
