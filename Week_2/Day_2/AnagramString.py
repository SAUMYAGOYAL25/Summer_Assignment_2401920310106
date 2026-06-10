class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        res = []

        if len(p) > len(s):
            return res

        p_count = [0] * 26
        s_count = [0] * 26

        for c in p:
            p_count[ord(c) - ord('a')] += 1

        for i in range(len(p)):
            s_count[ord(s[i]) - ord('a')] += 1

        if p_count == s_count:
            res.append(0)

        for i in range(len(p), len(s)):
            s_count[ord(s[i]) - ord('a')] += 1
            s_count[ord(s[i - len(p)]) - ord('a')] -= 1

            if p_count == s_count:
                res.append(i - len(p) + 1)

        return res
