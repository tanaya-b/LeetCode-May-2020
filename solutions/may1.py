# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        first = 1
        last = n
        found = False
        while(first<=last and not found):
            mid = (first + last)//2
            if(isBadVersion(mid) and not isBadVersion(mid-1)):
                found = True
                return mid
            else:
                if (isBadVersion(mid)):
                    last = mid - 1
                else:
                    first = mid + 1	
        return found
        
