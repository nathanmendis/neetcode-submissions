class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        parent={')':'(','}':'{',']':'['}
        for char in s:
            if char in parent:
                if not stack or stack[-1]!=parent[char]:
                    return False
                stack.pop()
            else:
                 stack.append(char) 
        return len(stack)==0



        