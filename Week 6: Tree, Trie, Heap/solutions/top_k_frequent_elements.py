from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = Counter(nums)  # Count frequency of each element
        bucket = [[] for _ in range(len(nums) + 1)]  # Buckets for frequencies

        # Fill the buckets
        for num, freq in freq_map.items():
            bucket[freq].append(num)
        
        res = []
        # Iterate buckets in reverse order to get most frequent elements first
        for i in range(len(bucket) - 1, 0, -1):
            for num in bucket[i]:
                res.append(num)
                if len(res) == k:
                    return res