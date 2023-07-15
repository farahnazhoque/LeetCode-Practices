class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """_summary_

        Args:
            s (str): a string of letters
            t (str): a string of letters

        Returns:
            bool: Given two strings s and t, return true if t is an anagram of s, and false otherwise.

        """
        return sorted(list(s)) == sorted(list(t))