class Solution:
    def validCharacter(self, ch):
        return ord('0') <= ord(ch) <= ord('9')
    
    def myAtoi(self, s: str) -> int:
        l = list(s)
        
        # remove whitespace
        while l and l[0] == " ":
            l.pop(0)
            
        # specify sign
        sign = 1
        if l and l[0] == '+':
            l.pop(0)
            sign = 1
        elif l and l[0] == '-':
            l.pop(0)
            sign = -1
        
        buf = ""
        while l and self.validCharacter(l[0]):
            buf += l.pop(0)
        
        result = 0
        for i in buf:
            num = ord(i) - ord('0')
            result = result* 10 + num
        result *= sign  # add sign
        if result > 2 ** 31 - 1:
            return 2 ** 31 - 1
        elif result < -(2 ** 31):
            return -(2 ** 31)
        else:
            return result
            i += 1

        val = sign * val

        if(val > 2147483647):
            return 2147483647
        elif(val < -2147483648):
            return -2147483648
        else:
            return val