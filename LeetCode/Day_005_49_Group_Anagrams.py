from collections import defaultdict
from typing import List


def groupAnagrams(strs:str) -> List[List[str]]:
    """
    Group Anagrams together using character list hashmap
    
    Time Complexity: O(N * K), where N is the number of strings, K is the maximum string length
    Space Complexity: O(N * K), to store the groups

    Args:
        strs (str): The list of strings

    Returns:
        List[List[str]]: Lists of groups of anagrams
    """
    
    anagram_group = defaultdict(list)
    
    for s in strs:
        
        # Create count array for 26 letters
        count = [0] * 26
        
        # Count number of occurrences of each character in s
        for char in s:
            
            # Map every charter to an index in the count array.
            # a -> 0, b -> 1, c -> 2, ... , z -> 25
            count[ord(char) - ord('a')] += 1
        
        # convert list to a tuple so it can be used as dictionary key
        key = tuple(count)
        
        anagram_group[key].append(s)
        
    return list(anagram_group.values())



print(groupAnagrams(strs = ["eat","tea","tan","ate","nat","bat"]))