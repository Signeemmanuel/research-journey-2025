from typing import List

def twoSum(nums:List[int], target:int) -> List[int]:
    """
    The Functions finds two numbers in the list, nums that sum up to target

    Args:
        nums (List[int]): The List of integers
        target (int): The target sum

    Returns:
        List[int]: List of two numbers summing up to the target, [] otherwise
    """
    
    # Dictionary of numbers with their corresponding index
    nums_map = {}
    
    for i, num in enumerate(nums):
        complement = target - num
        if complement in nums_map:
            return [nums_map[complement], i]
        
        nums_map[num] = i
        
    return []


# Test
print(twoSum(nums = [2,7,11,15], target = 9))