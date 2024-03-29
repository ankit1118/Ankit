class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        def digit_sum(num):
            res = 0
            while num:
                res += num % 10
                num = num // 10
            return res
        count = collections.defaultdict(list)
        for i, n in enumerate(nums):
            val = digit_sum(n)
            if len(count[val]) == 2:
                temp = count[val]
                if n > temp[0] or n > temp[1]:
                    if temp[0] > temp[1]:
                        temp[1] = n
                    else:
                        temp[0] = n
                count[val] = temp
            else:
                count[val].append(n)

        res = -1
        for val in count:
            if len(count[val]) > 1:
                res = max(res, sum(count[val]))
        return res
        