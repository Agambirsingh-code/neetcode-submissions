class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        for i in nums:
            seen[i] = seen.get(i, 0)+1
        
        buckets = [[] for i in range(len(nums)+1)]
        for x, freq in seen.items():
            buckets[freq].append(x)
        
        res = []
        for i in range(len(buckets)-1,0,-1):
            for n in buckets[i]:
                res.append(n)
                if len(res) == k:
                    return res