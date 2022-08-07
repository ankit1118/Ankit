class Solution:
    def repeatedCharacter(self, s: str) -> str:
        res={}
        for i in s:
            if i in res:
                return i
            else:
                res[i]=0
        return ""
        