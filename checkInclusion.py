class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hashmap1 = {}
        hashmap2 = {}
        length = len(s1)

        if len(s1) > len(s2):
            return False

        for num in range(ord('a'), ord('z') + 1):
            hashmap1[chr(num)] = 0
            hashmap2[chr(num)] = 0
        
        for char in s1:
            hashmap1[char] += 1
        
        for i in range(len(s1)):
            hashmap2[s2[i]] += 1

        for i in range(len(s2)):
            if hashmap1 == hashmap2:
                return True
            
            hashmap2[s2[i]] -= 1
            if i + length == len(s2):
                break
            hashmap2[s2[i+length]] += 1
        
        return False
        