class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        #on cherche le nbr de subarrays dont la moyenne est >= treshold
        curr_sum = 0
        i =0
        maxSub = 0 #occurence de subarray répondant à la condition

        for j in range(len(arr)):
            curr_sum += arr[j]
            if j - i + 1 == k:
                if curr_sum / k >= threshold: # taille de la fenêtre / k est la moyenne
                    maxSub += 1
                curr_sum -= arr[i]
                i += 1
        return maxSub