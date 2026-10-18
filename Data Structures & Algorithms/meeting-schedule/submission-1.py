"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        
        def mysort(n):
            return n.start
        intervals.sort(key=mysort)
            
        end=0
        for meet in intervals:
                
            if meet.start < end:
                return False
                break
            end = meet.end
        return True


