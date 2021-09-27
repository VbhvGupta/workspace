class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ran_mp = Counter(ransomNote)
        mag_mp = Counter(magazine)
        
        if len(ran_mp) > len(mag_mp) :
            return False
        for k in ran_mp :
            if ran_mp[k] > mag_mp[k] :
                return False
        return True