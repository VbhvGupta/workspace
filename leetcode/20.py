class Solution:
    def isValid(self, s: str) -> bool:
        ln = len(s)
        if ln%2 :
            return False
        stack = ['']
        dic = { ')' : '(' , '}':'{' , ']':'[' }
        for c in s :
            if c in ['(' , '[', '{']:
                stack.append(c)
            elif dic[c] != stack[-1] :
                return False
            else :
                stack.pop()
        return stack[-1] == ''
