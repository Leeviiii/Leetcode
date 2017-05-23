class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if len(heights) == 0:
            return 0
        minheight = []
        for i in range(len(heights)):
            tmp = []
            for j in range(len(heights)):
                tmp.append(0)
            minheight.append(tmp)
        maxsum = 0
        for i in range(len(heights)):
            for j in range(i,len(heights)):
                if i == j:
                    minheight[i][j] = heights[i]
                else:
                    minheight[i][j] = min(heights[j],minheight[i][j-1])
                sumtmp = minheight[i][j]*(j-i+1)
                if sumtmp > maxsum:
                    maxsum = sumtmp
        return maxsum
                                                    
if __name__ == "__main__":
    s = Solution()
    words = [2,1,5,6,2,3]
    r = s.largestRectangleArea(words)
    print r
