class Solution:
    def longestPalindrome(self, s: str) -> int:
        hash_mp = {}
        for i in range(0,len(s)) :
            if s[i] not in hash_mp :
                hash_mp[s[i]] = 0;
            hash_mp[s[i]]+=1
        ans = 0
        rem = []
        for h in hash_mp :
            if hash_mp[h] % 2 == 1 :
                rem.append(h)
            ans += ((hash_mp[h]//2)*2)

        if rem :
            ans += 1
        return ans
