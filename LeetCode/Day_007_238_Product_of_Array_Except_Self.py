from typing import List

def productExceptSelf(nums: List[int]) -> List[int]:
    """
    Calculates product of array except self without division.
    
    Strategy:
    1. Pass 1 (Left -> Right): Store the 'Prefix' product in the result array.
    2. Pass 2 (Right -> Left): Multiply the result by the 'Postfix' running product.
    
    Time: O(N)
    Space: O(1) (excluding output array)
    """
    n = len(nums)
    res = [1] * n
    
    # --- Pass 1: Prefix Products ---
    # res[i] will store the product of everything to the LEFT of i
    prefix = 1
    for i in range(n):
        res[i] = prefix
        prefix *= nums[i] # Update prefix for the next iteration
        
    # --- Pass 2: Postfix Products ---
    # Multiply res[i] by everything to the RIGHT of i
    postfix = 1
    for i in range(n - 1, -1, -1): # Iterate backwards
        res[i] *= postfix
        postfix *= nums[i] # Update postfix for the next iteration
        
    return res