class Solution:
    def isValid(self, s: str) -> bool:
        # s="([{}])"
        stack=[]
        hm={"]":"[","}":"{",")":"("}
        for i in s:
            if i in hm:
                if stack and stack[-1] == hm[i]:
                    stack.pop()
                else:
                    return False
            else :
                stack.append(i)
        return True if not stack else False