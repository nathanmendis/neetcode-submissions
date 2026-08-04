class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen={}
        for word in strs:
            count=[0]*26 
            for char in word:
                count[ord(char)-ord('a')]+=1
            key=tuple(count)
            if key not in seen:
                seen[key]=[]
            seen[key].append(word)
        return list(seen.values())