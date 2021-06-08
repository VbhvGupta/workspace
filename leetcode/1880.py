class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        x=""
        y=""
        z=""
        for i in range(0,len(firstWord)) :
            x+=str(int(ord(firstWord[i])-ord('a')))
        for i in range(0,len(secondWord)) :
            y+=str(int(ord(secondWord[i])-ord('a')))
        for i in range(0,len(targetWord)):
            z+=str(int(ord(targetWord[i])-ord('a')))

        x=int(x)
        y=int(y)
        z=int(z)

        return x+y==z
