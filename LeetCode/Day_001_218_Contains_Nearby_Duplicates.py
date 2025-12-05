from typing import List


class Solution(object):
    def containsNearbyDuplicate(self, nums:List[int], k:int) -> bool:
        """
        Determines if an array, nums contains two distinct indices i and j such that 
        num[i] == num[j] and the absolute different between i and j is at most k.
        
        
        
        Checks if a list, nums contains duplicates, such that the duplicates are at a maximum distance of k
        
        Args:
            nums (List[int]): The input list of integers
            k (int): the maximum allowed absolute difference between indices

        Returns:
            bool: True if such a pair exist, otherwise False
        """

        # Dictionary store {number: number_last_seen_index}
        seen = {}
        
        for i, num in enumerate(nums):
            if num in seen and i - seen[num] <= k:
                return True
            
            seen[num] = i
        
        return False