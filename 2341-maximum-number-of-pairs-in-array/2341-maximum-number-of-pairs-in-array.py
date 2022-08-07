class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return [0, 1]
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        res1, res2 = 0, 0
        for val in count.values():
            res1 += val // 2
            res2 += val % 2
        return [res1, res2]