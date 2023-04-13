class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        result =0
        dict1 = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        for i in range(len(s)):
            if i+1<len(s) and dict1[s[i]]<dict1[s[i+1]]:
                result-= dict1[s[i]]
            else:
                result+=dict1[s[i]]
        return result