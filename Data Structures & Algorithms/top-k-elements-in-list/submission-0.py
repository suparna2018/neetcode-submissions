import heapq as PQ
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        PQ = []
        mp=defaultdict(int)
        for ele in nums:
            mp[ele]+=1
        for ele in mp:
            heapq.heappush(PQ, [-mp[ele],ele])
        i=0
        res=[]
        while i<k:
            val=heapq.heappop(PQ)
            res.append(val[1])
            i+=1
        return res