class Solution(object):
    def isAnagram(self, s:str, t:str) -> bool:
        """
        Determines if t is an anagram of s by comparing character frequency counts.

        Args:
            s (str): The first string
            t (str): The second string

        Returns:
            bool: True if t is an anagram of s, False otherwise
        """
        
        # Anagrams must have the same length
        if len(s) != len(t):
            return False
        
        # Character frequency count dictionary {character: frequency_count}
        count = {}
        
        for i in range(len(s)):
            # Count s
            count[s[i]] = count.get(s[i], 0) + 1
            
            # Count t (Subtract immediately)    
            count[t[i]] = count.get(t[i], 0) - 1
            
        
        for val in count.values():
            if val != 0:
                return False
        
        return True