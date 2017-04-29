class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = len(height)
        maxv = 0
        for i in range(l):
            for j in range(i,l):
                if i == j:
                    continue;
                v = (j-i)*min(height[i],height[j])
                if v > maxv:
                    maxv = v

        return maxv


if __name__ == "__main__":
    s = Solution()
    height = [3,2,1,3]
    nums = s.maxArea(height)
    print nums
