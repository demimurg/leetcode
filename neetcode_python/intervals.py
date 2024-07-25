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


if __name__ == "__main__":
    import doctest

doctest.testmod()
