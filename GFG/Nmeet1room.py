class Solution:

    #Function to find the maximum number of meetings that can
    #be performed in a meeting room.
    def maximumMeetings(self,n,start,end):
        lst = []
        for i in range(0,len(start)) :
            lst.append((start[i],end[i]))
        lst.sort(key = lambda x:x[1])
        prev = -1
        count = 0
        for s,e in lst :
            if s > prev :
                count += 1
                prev = e
        return count

#{
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        start = list(map(int,input().strip().split()))
        end = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.maximumMeetings(n,start,end))
# } Driver Code Ends
