class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # on cherche la taille min d'un subarray dont la somme est >= à target
        min_sub_length = float("inf")  # keep track of min length
        curr_sum = 0
        i = 0

        for j in range(len(nums)):
            curr_sum += nums[j]
            while curr_sum >= target: # Tant que vrai do this multiple times (originally i used if instead of while)
                min_sub_length = min(min_sub_length, j - i + 1)
                curr_sum -= nums[i]
                i += 1

        if min_sub_length != float("inf"):
            return min_sub_length
        else:
            return 0