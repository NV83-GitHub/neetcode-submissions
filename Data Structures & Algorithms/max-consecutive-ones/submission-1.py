class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        current = 0
        result = 0

        for num in nums:
            if num == 1:
                current += 1
                result = max(current,result)
            else:
                current = 0
        
        return result