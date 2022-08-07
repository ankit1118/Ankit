class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        myset=set()
        result=[]
        for i in nums:
            length=len(myset)
            myset.add(i)
            if length==len(myset):
                result+=[i]
        return result