#7. Reverse Integer
#https://leetcode.com/problems/reverse-integer/submissions/
#my ans(passed)
import math
class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:return 0
        sign = -1 if x<0 else 1
        x = x*sign
        ans=""
        while x !=0:
            ans+=str(x%10)
            x//=10
        if not (math.log2(2**31)*-1 <= math.log2(int(ans))*sign <= math.log2(2**31-1)):return 0
        return sign*int(ans)