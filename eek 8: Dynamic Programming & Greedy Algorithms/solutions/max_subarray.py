class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        maxSubarray = nums[0]
        current_sum = 0

        for num in nums:
            current_sum = current_sum + num
            maxSubarray = max(maxSubarray, current_sum)
            if current_sum < 0:
                current_sum = 0

        return maxSubarray


        