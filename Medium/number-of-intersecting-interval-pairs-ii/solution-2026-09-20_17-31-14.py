class Solution:
    def countIntersectingIntervals(self, intervals: list[list[int]]) -> int:

        intervals.sort()
        res = 0
        min_heap = []
        heapq.heapify(min_heap)
        heapq.heappush(min_heap, intervals[0][1])

        for i in range(1, len(intervals)):
            new_start = intervals[i][0]
            
            while min_heap and new_start > min_heap[0]:
                heapq.heappop(min_heap)
            
            res += len(min_heap)
            heapq.heappush(min_heap, intervals[i][1])

        return res 