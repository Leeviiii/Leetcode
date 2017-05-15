class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxheight = 0
        leftmax = []
        for i in range(len(height)):
            leftmax.append(maxheight)
            maxheight = max(maxheight,height[i])
        print leftmax
        i = len(height) - 1
        maxheight = 0
        t = 0
        while i >= 0:
            tmpmax = min(maxheight,leftmax[i])
            maxheight = max(maxheight,height[i])
            if tmpmax > height[i]:
                t += tmpmax - height[i]
            else:
                pass
            i -= 1
        return t


if __name__ == "__main__":
    s = Solution()
    #nums = [0,1,0,2,1,0,1,3,2,1,2,1]
    nums = [0,2,0]
    #nums = [5,3,3,1,3,5]
    r = s.trap(nums)
    print r
