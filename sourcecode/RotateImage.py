class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if len(matrix)%2 == 1:
            center = len(matrix)/2
            for level in range(center+1):
                self.rotateOneLevel1(matrix,level,center)
        else:
            centerl = len(matrix)/2 - 1
            centerr = len(matrix)/2
            for level in range(centerr):
                self.rotateOneLevel2(matrix,level,centerl,centerr)

    def rotateOneLevel1(self, matrix, level, center):
        if level == 0:
            return
        for i in range(center-level,center + level):
            d = i - (center-level)
            tmp = matrix[center-level][i]
            matrix[center-level][i] = matrix[center+level-d][center-level]
            matrix[center+level-d][center-level] = matrix[center+level][center+level-d]
            matrix[center+level][center+level-d] =  matrix[center-level+d][center+level]
            matrix[center-level+d][center+level] = tmp


    def rotateOneLevel2(self, matrix, level, centerl, centerr):
        for i in range(centerl-level,centerr+level):
            d = i - (centerl-level)
            tmp = matrix[centerl-level][i]
            matrix[centerl-level][i] = matrix[centerr+level-d][centerl-level] 
            matrix[centerr+level-d][centerl-level] = matrix[centerr+level][centerr+level-d]
            matrix[centerr+level][centerr+level-d] = matrix[centerl-level+d][centerr+level]
            matrix[centerl-level+d][centerr+level] = tmp






                                                    
                                                    
if __name__ == "__main__":
    s = Solution()
    #a = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    #a = [[1,2,3],[4,5,6],[7,8,9]]
    #a = [[1,2],[3,4]]
    a = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
    s.rotate(a)
    print a
