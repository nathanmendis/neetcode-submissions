class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen={}
        for word in strs:
            key="".join(sorted(word))
            if key not in seen:
                seen[key]=[]
            seen[key].append(word)
        seen_lst=list(seen.values())
        return seen_lst