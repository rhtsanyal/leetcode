class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        charset = set()
        max_len = 0
        i = 0
        j = 0
        n = len(s)
        while i < n and j < n:
            if s[j] not in charset:
                charset.add(s[j])
                j += 1
                max_len = max(j-i,max_len)
            else:
                charset.remove(s[i])
                i += 1
        return max_len