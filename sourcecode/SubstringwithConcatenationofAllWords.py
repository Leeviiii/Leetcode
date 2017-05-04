#! usr/bin/python
#coding=utf-8 
class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if len(words) == 0:
            return []
        wl = len(words[0])
        if len(s) < wl:
            return []
        wmap = {}
        for t in words:
            if t in wmap:
                wmap[t] += 1
            else:
                wmap[t] = 1
        i = 0
        needmatchcnt = len(words)
        result = []
        for i in range(wl):
            j = i
            left = i
            ret = {}
            hasmatchcnt = 0
            while j < len(s):
                t = s[j:j+wl]
                if t in wmap:
                    if t in ret:
                        ret[t] += 1
                    else:
                        ret[t] = 1
                    #匹配到一个
                    if ret[t] <= wmap[t]:
                        hasmatchcnt += 1
                    else :
                        #匹配多了 需要重新赋值开始的位置
                        while ret[t] > wmap[t]:
                            tmp = s[left:left+wl]
                            if tmp in ret:
                                ret[tmp] -= 1
                                if ret[tmp] < wmap[tmp]:
                                    hasmatchcnt -= 1
                            left += wl
                    if hasmatchcnt == needmatchcnt:
                        result.append(left)
                        tmp = s[left:left+wl]
                        if tmp in ret:
                            ret[tmp] -= 1
                        hasmatchcnt -= 1
                        left += wl
                else:
                    ret = {}
                    hasmatchcnt = 0
                    left = j + wl
                j = j + wl
        return result

if __name__ == "__main__":
    s = Solution()
    #a = "barfoofoobarthefoobar"
    #b = ["foo", "bar","the"]
    #a = "barfoothefoobarman"
    #b = ["foo", "bar"]
    #a = "wordgoodgoodgoodbestword"
    #b = ["word","good","best","good"]
    r = s.findSubstring(a,b)
    print r
