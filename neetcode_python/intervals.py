from typing import *


def insert_interval(intervals: List[List[int]], new_interval: List[int]) -> List[List[int]]:
    """
    You are given an array of non-overlapping intervals where intervals[i] = [start_i, end_i] represent the start and
    the end of the ith interval and intervals is sorted in ascending order by start_i. You are also given an interval
    newInterval = [start, end] that represents the start and end of another interval.

    Insert newInterval into intervals such that intervals is still sorted in ascending order by start_i and intervals
    still does not have any overlapping intervals (merge overlapping intervals if necessary).

    Return intervals after the insertion.

    Note that you don't need to modify intervals in-place. You can make a new array and return it.
    
    [MEDIUM] https://leetcode.com/problems/insert-interval/

    >>> insert_interval([[1, 3], [6, 9]], [2, 5])
    [[1, 5], [6, 9]]
    >>> insert_interval([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8])
    [[1, 2], [3, 10], [12, 16]]
    >>> insert_interval([], [5, 7])
    [[5, 7]]
    >>> insert_interval([[1, 5]], [2, 3])
    [[1, 5]]
    >>> insert_interval([[1, 5]], [2, 7])
    [[1, 7]]
    """
    start, end = 0, 1
    for i in range(len(intervals)):
        if intervals[i][start] > new_interval[start]:
            intervals.insert(i, new_interval)
            break
    else:
        intervals.append(new_interval)

    i = 0
    for j in range(1, len(intervals)):
        if intervals[j][start] <= intervals[i][end]:
            # j interval includes in i or extends it
            intervals[i][end] = max(intervals[i][end], intervals[j][end])
            continue
        i += 1
        intervals[i] = intervals[j]

    return intervals[:i + 1]


def insert_interval_2(intervals: List[List[int]], new_interval: List[int]) -> List[List[int]]:
    res = []
    start, end = 0, 1
    for i in range(len(intervals)):
        if intervals[i][start] > new_interval[end]:
            res.append(new_interval)
            return res + intervals[i:]
        if intervals[i][end] < new_interval[start]:
            res.append(intervals[i])
        else:
            new_interval = [
                min(intervals[i][start], new_interval[start]),
                max(intervals[i][end], new_interval[end]),
            ]
    res.append(new_interval)
    return res


def merge_intervals(intervals: List[List[int]]) -> List[List[int]]:
    """
    Given an array of intervals where intervals[i] = [start_i, end_i], merge all overlapping intervals, and return
    an array of the non-overlapping intervals that cover all the intervals in the input.
    [MEDIUM] https://leetcode.com/problems/merge-intervals/

    >>> merge_intervals([[1,3],[2,6],[8,10],[15,18]])
    [[1, 6], [8, 10], [15, 18]]
    >>> merge_intervals([[1,4],[4,5]])
    [[1, 5]]
    """
    intervals.sort()
    i, start, end = 0, 0, 1
    for j in range(1, len(intervals)):
        if intervals[j][start] <= intervals[i][end]:
            # j interval includes in i or extends it
            intervals[i][end] = max(intervals[i][end], intervals[j][end])
            continue
        i += 1
        intervals[i] = intervals[j]

    return intervals[:i + 1]


def erase_overlap_intervals(intervals: List[List[int]]) -> int:
    """
    Given an array of intervals where intervals[i] = [start_i, end_i], return the minimum number of intervals you need
    to remove to make the rest of the intervals non-overlapping.
    [MEDIUM] https://leetcode.com/problems/non-overlapping-intervals/

    >>> erase_overlap_intervals([[1,2],[2,3],[3,4],[1,3]])
    1
    >>> erase_overlap_intervals([[1,2],[1,2],[1,2]])
    2
    >>> erase_overlap_intervals([[1,2],[2,3]])
    0
    """
    intervals.sort()
    last, count, start, end = -10e6, 0, 0, 1
    for interval in intervals:
        if interval[start] < last:
            count += 1
            last = min(last, interval[end])
        else:
            last = interval[end]

    return count


def can_attend_meetings(intervals: List[List[int]]) -> bool:
    """
    Given an array of meeting time interval objects consisting of start and end times [[start_1,end_1],[start_2,end_2],...]
    (start_i < end_i), determine if a person could add all meetings to their schedule without any conflicts.
    [EASY] https://leetcode.com/problems/meeting-rooms/

    >>> can_attend_meetings([[0,30],[5,10],[15,20]])
    False
    >>> can_attend_meetings([[5,8],[9,15]])
    True
    """
    intervals.sort()
    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[i - 1][1]:
            return False
    return True


def min_meeting_rooms(intervals: List[List[int]]) -> int:
    """
    Given an array of meeting time interval objects consisting of start and end times [[start_1,end_1],[start_2,end_2],...]
    (start_i < end_i), find the minimum number of days required to schedule all meetings without any conflicts.
    [MEDIUM] https://leetcode.com/problems/meeting-rooms-ii/

    >>> min_meeting_rooms([[0,40],[5,10],[15,20]])
    2
    >>> min_meeting_rooms([[4,9]])
    1
    """
    intervals.sort()
    days_end = []
    for interval in intervals:
        for i in range(len(days_end)):
            if interval[0] >= days_end[i]:
                days_end[i] = interval[1]
                break
        else:
            days_end.append(interval[1])
    return len(days_end)


if __name__ == "__main__":
    import doctest

doctest.testmod()
