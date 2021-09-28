class Solution:
    def reverseWords(self, s: str) -> str:
        prev = 0
        def fn(strng) :
            return str(strng)[::-1]
        arr = ' '.join(map(fn,s.split(' ')))
        return arr