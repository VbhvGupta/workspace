class Solution:
    def reverse(self, x: int) -> int:
        if x<0:
            ans = str(x)[1:]
            ans = ans[::-1]
            if (-1 * int(ans) ) >= -2147483648 :
                return (-1*int(ans))
            else :
                return 0
        else :
            ans = str(x)
            ans = ans[::-1]
            if int(ans) <= 2147483647 :
                return int(ans)
            else :
                return 0
