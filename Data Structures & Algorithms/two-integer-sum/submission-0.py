class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # i search for target - current .
        # i should store already seen in hashmap for efficiency
        # since i use both value and indexes i could use enumerate()
        seen = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in seen:
                return [seen[diff],i]
            seen[n] = i
        