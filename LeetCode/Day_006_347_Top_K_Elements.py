from typing import List

def topKFrequent(nums: List[int], k: int) -> List[int]:
    """
    Finds the k most frequent elements using Bucket Sort.
    
    Time Complexity: O(N) - Linear time.
    Space Complexity: O(N) - To store the count map and frequency buckets.
    """
    # 1. Count Frequencies: O(N)
    count = {}
    for n in nums:
        count[n] = count.get(n, 0) + 1
        
    # 2. Create Buckets: O(N)
    # Index i stores list of numbers that appeared exactly i times.
    # Size is len(nums) + 1 because max freq cannot exceed array length.
    freq = [[] for _ in range(len(nums) + 1)]
    
    for num, c in count.items():
        freq[c].append(num)
        
    # 3. Gather Top K: O(N)
    # Iterate backwards from highest frequency bucket
    res = []
    for i in range(len(freq) - 1, 0, -1):
        for n in freq[i]:
            res.append(n)
            if len(res) == k:
                return res
    
    return res



# test

print(topKFrequent(nums = [1,1,1,2,2,3], k = 2))