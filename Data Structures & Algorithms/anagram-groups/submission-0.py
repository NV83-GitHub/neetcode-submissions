class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
       # Utiliser la fréquence comme clé pour un hashmap (attention default dict), et stocker comme valeurs les occurence avec 
       # cette fréquence sous forme d'array.

        result = defaultdict(list)
        for s in strs:
            count = [0]*26
            for c in s:
                count[ord(c) - ord("a")] += 1
            result[tuple(count)].append(s)
        return list(result.values())