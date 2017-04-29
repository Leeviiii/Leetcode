class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        begin = 0
        end = len(height) - 1
        maxv = 0
        while begin < end:
            v = (end - begin)*min(height[begin],height[end])
            maxv = max(v,maxv)
            if height[begin] < height[end]:
                begin += 1
            else:
                end -= 1

        return maxv


if __name__ == "__main__":
    s = Solution()
    height = [3,2,1,3]
    nums = s.maxArea(height)
    print nums
