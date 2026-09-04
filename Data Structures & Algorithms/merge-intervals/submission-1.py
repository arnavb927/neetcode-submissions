class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        last_start, last_end = intervals[0]
        
        for interval in intervals[1:]:
            current_start, current_end = interval

            if current_start <= last_end:
                last_end = max(last_end, current_end)
            else:
                res.append([last_start, last_end])
                last_start = current_start
                last_end = current_end
            
        res.append([last_start, last_end])
        return res


                