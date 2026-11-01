class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_map = dict()
        for char in s:
            if char in hash_map:
                hash_map[char] += 1
            else:
                hash_map[char] = 1
        
        hash_set = dict()
        for cha in t:
            if cha in hash_set:
                hash_set[cha] += 1
            else:
                hash_set[cha] = 1
        
        if hash_map == hash_set:
            return True
        else:
            return False

        