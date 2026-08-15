class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        hm={"+":lambda a,b:a+b,"-":lambda a,b:a-b,"/":lambda a,b:int(a/b),"*":lambda a,b:a*b}
        stack=[]
        for i in range(len(tokens)):
            if tokens[i] in hm:
                ans=hm[tokens[i]](int(stack[-2]),int(stack[-1]))
                stack.pop()
                stack.pop()
                stack.append(ans)
            else:
                stack.append(tokens[i])

        return int(stack[-1])
        