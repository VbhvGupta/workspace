class Solution:

    def ispalindrome(self ,word : str) -> bool :
        return word == word[::-1]

    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        ans = []
        ln = len(words)
        if ln==1 :
            return []

        for i in range(0,ln):
            if words[i] == "" :
                for j in range(i+1,ln) :
                    if self.ispalindrome(words[j]):
                        ans.extend(([i,j],[j,i]))
                i+=1
            for j in range(i+1,ln):
                if words[j] == "" :
                    if self.ispalindrome(words[i]):
                        ans.extend(([i,j],[j,i]))
                else :
                    if self.ispalindrome(words[i]+words[j]) :
                        ans.append([i,j])
                    if self.ispalindrome(words[j]+words[i]) :
                        ans.append([j,i])
        return ans
