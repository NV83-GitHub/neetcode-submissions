class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # it's binary search time baby 
        L = 0
        R = len(nums) - 1

        while L <= R:
            M = (L + R)//2
            if target > nums[M]:
                L =  M + 1
            elif target < nums[M]:
                R = M - 1
            else:
                return M
        return -1