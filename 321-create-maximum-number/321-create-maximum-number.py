class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        l1,l2 = len(nums1),len(nums2)
        rs = []
        
        
        def helper(nums,c_len):
            ans = []
            ln = len(nums)
            for idx,val in enumerate(nums):
                while ans and ans[-1]<val and ln-idx> c_len-len(ans):
                    ans.pop(-1)
                if len(ans)<c_len:
                    ans.append(val)
            return ans
        
        for s1 in range(max(0,k-l2),min(k,l1)+1):
            p1,p2 = helper(nums1,s1),helper(nums2,k-s1)
            rs = max(rs,[max(p1,p2).pop(0) for _ in range(k)])
        return rs