class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        if len(words) == 0:
            return
        ret = []
        leftwidth = maxWidth
        tmpret = []
        begin = 0
        end = 0
        for word in words:
            if len(word) <= leftwidth:
                leftwidth -= len(word)
                leftwidth -= 1
                if leftwidth == 0:
                    tmpret = self.childfullJustify(words, begin, end, maxWidth,leftwidth)
                    ret.append(tmpret)
                    begin = end + 1
                    leftwidth = maxWidth
                end += 1
            else:
                tmpret = self.childfullJustify(words, begin, end-1, maxWidth,leftwidth)
                ret.append(tmpret)
                begin = end
                leftwidth = maxWidth
                leftwidth -= len(word)
                leftwidth -= 1
                end += 1
        if begin != end:
            tmpret = self.childfullJustify(words,begin,end-1,maxWidth,leftwidth)
            ret.append(tmpret)
        return ret
    def childfullJustify(self,words,begin,end,maxWidth,leftwidth):
        tmpret = [' ']*maxWidth
        space = leftwidth + end - begin + 1
        extraspace = 0
        avgspace = 0
        if end == len(words) - 1:
            extraspace = 0
            avgspace = 1
        elif end != begin:
            avgspace = space/(end - begin)
            extraspace = space%(end - begin)
        else:
            extraspace = 0
        j = 0
        extrak = 0
        for i in range(begin,end+1):
            word = words[i]
            for k in word:
                tmpret[j] = str(k)
                j += 1
            if i == end:
                break
            for i in range(avgspace):
                j += 1
            if extrak < extraspace:
                j += 1
                extrak += 1
        return "".join(tmpret)
if __name__ == "__main__":
    s = Solution()
    #words = ["This", "is", "an", "example", "of", "text", "justification."]
    #maxWidth = 16
    #words = ["a"]
    #maxWidth = 2
    #words = ["What","must","be","shall","be."]
    #maxWidth = 12
    words = ["Don't","go","around","saying","the","world","owes","you","a","living;","the","world","owes","you","nothing;","it","was","here","first."]
    maxWidth = 30
    r = s.fullJustify(words,maxWidth)
    print r
