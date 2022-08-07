class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        count,l=0,[]    
        
        for i in nums :
            
            a=bisect.bisect_right  (l,i*2)
            count+=len (l)-a
            idx=bisect.bisect(l,i)
            l[idx:idx]=[i]
            
        return count