# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        def bin_search(l,r) :
            if l == r :
                return l
            if l+1 == r :
                return l if isBadVersion(l) else r
            mid = (l+r)//2
            if isBadVersion(mid) :
                return bin_search(l,mid)
            return bin_search(mid,r)
        return bin_search(1,n)