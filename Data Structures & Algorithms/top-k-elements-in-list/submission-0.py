class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # i would try a hashmap
        hash = {}
        for num in nums:
            if num not in hash:
                hash[num] = 0
            hash[num] += 1
        # Part 2 return k most frequent. 
        sorted_items = sorted(hash.items(), key=lambda item: item[1], reverse=True)
        result = []
        for i in range(k):
            result.append(sorted_items[i][0])
        return result