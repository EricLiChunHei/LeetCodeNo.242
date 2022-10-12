class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        arr = list(sorted(s))
        newarr = list(sorted(t))
        if arr == newarr:
            return True
        else:
            return False