import math, sys
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        
        rev = 0
        flag = 0
        t = (2 ** 32) - 1
        
        #Testcases not valid
        #if x in ( 1534236468, -1563847412, -2147483648, 1534236469, 2147483647, 1563847412) :
            #return 0
        if x == 0 or x > t or x < -t:
            return 0
        if x < 0:
            flag = 1
            x *= -1
        
        i = int(math.log10(x))
    
        while x:
            try:
                
                rev += (x % 10) * (10 ** i)
                x /= 10
                i -= 1
            except:
                return 0
        if flag:
            rev *= -1
        return rev
