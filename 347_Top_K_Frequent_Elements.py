class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # method 1:
        #   Time Complexity: O(n*logn)
        #   Space Complexity: O(n)
        # return [element[0] for element in collections.Counter(nums).most_common(k)]

        # method 2: heap
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        freq = {}
        for num in nums:
            freq[num] = freq.get(num,0) + 1
        
        heap = []
        for key,v in freq.items():
            heapq.heappush(heap,(-v,key)) # heapq => minheap Time Complexity: O(logn) 

        res = []
        while k != 0:
            res.append(heapq.heappop(heap)[1])
            k -= 1
        
        return res
