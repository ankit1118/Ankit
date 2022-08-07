class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums
        a = self.sortArray(nums[:int(len(nums)/2)])
        b = self.sortArray(nums[int(len(nums)/2):])

        return self.merge_array(a,b)

    def merge_array(self, a, b):
        merged = []
        i: int = 0
        j: int = 0 
        for k in range(0,len(a)+len(b)):
            if j == len(b) or (i < len(a) and a[i] < b[j]):
                merged.append(a[i])
                i += 1
            else:
                merged.append(b[j])
                j +=1
        return merged