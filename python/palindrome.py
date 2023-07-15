class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stripped_s = ''.join(c for c in s if c.isalnum()).lower()
        return stripped_s == stripped_s[::-1] # getting the reverse and checking
