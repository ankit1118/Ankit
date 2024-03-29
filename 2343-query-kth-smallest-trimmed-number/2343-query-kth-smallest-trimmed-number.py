class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        res = []
        for q in queries:
            k = q[0]
            trim = q[1]
            heap = []
            for i, n in enumerate(nums):
                heap.append([int(n[-trim:]), i])
            heap.sort(key = lambda x: (x[0], x[1]))
            res.append(heap[k-1][1])
        return res
        