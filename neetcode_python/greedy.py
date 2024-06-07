import heapq
from typing import *


def max_sub_array(nums: List[int]) -> int:
    """
    Given an integer array nums, find the subarray with the largest sum, and return its sum.
    [MEDIUM] https://leetcode.com/problems/maximum-subarray/

    >>> max_sub_array([-2,1,-3,4,-1,2,1,-5,4])
    6
    >>> max_sub_array([1])
    1
    >>> max_sub_array([5,4,-1,7,8])
    23
    """
    cur_sum, max_sum = 0, -(10 ** 4)
    for num in nums:
        # cur_sum < 0 can't add positive value for current interval
        cur_sum = max(cur_sum, 0) + num
        max_sum = max(max_sum, cur_sum)
    return max_sum


def can_jump(nums: List[int]) -> bool:
    """
    You are given an integer array nums. You are initially positioned at the array's first index,
    and each element in the array represents your maximum jump length at that position.

    Return true if you can reach the last index, or false otherwise.
    [MEDIUM] https://leetcode.com/problems/jump-game/

    >>> can_jump([2, 3, 1, 1, 4])
    True
    >>> can_jump([3, 2, 1, 0, 4])
    False
    """
    can_jump_i = 0
    for i in range(len(nums)):
        can_jump_i = max(can_jump_i, i + nums[i])
        if can_jump_i >= len(nums):
            return True
        if can_jump_i <= i:
            return False
    return True


def jump(nums: List[int]) -> int:
    """
    You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].
    Each element nums[i] represents the maximum length of a forward jump from index i. In other words,
    if you are at nums[i], you can jump to any nums[i + j] where:
    - 0 <= j <= nums[i] and
    - i + j < n

    Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].
    [MEDIUM] https://leetcode.com/problems/jump-game-ii/

    >>> jump([2, 3, 1, 1, 4])
    2
    >>> jump([2, 3, 0, 1, 4])
    2
    """
    l, r = 0, 0
    min_steps = 0
    # stop, when we can reach last step from current level
    while r < len(nums) - 1:
        new_r = r
        # iterate over next steps
        for i in range(l, r + 1):
            # find new farthest jump r
            new_r = max(new_r, i + nums[i])
        l, r = r, new_r
        # new level of possible steps added
        min_steps += 1

    return min_steps


def can_complete_circuit(gas: List[int], cost: List[int]) -> int:
    """
    There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].

    You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next
    (i + 1)th station. You begin the journey with an empty tank at one of the gas stations.

    Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit
    once in the clockwise direction, otherwise return -1. If there exists a solution, it is guaranteed to be unique.

    [MEDIUM] https://leetcode.com/problems/gas-station/

    >>> can_complete_circuit([1,2,3,4,5], [3,4,5,1,2])
    3
    >>> can_complete_circuit([2,3,4], [3,4,3])
    -1
    """
    cur, total, start_i = 0, 0, 0
    for i in range(len(gas)):
        diff = gas[i] - cost[i]
        cur += diff
        total += diff
        if cur < 0:
            cur = 0
            start_i = i + 1

    return start_i if total >= 0 else -1


def is_n_straight_hand(hand: List[int], group_size: int) -> bool:
    """
    Alice has some number of cards and she wants to rearrange the cards into groups so that each group is of size
    group_size, and consists of group_size consecutive cards.
    Given an integer array hand where hand[i] is the value written on the i-th card and an integer group_size,
    return true if she can rearrange the cards, or false otherwise.
    [MEDIUM] https://leetcode.com/problems/hand-of-straights/

    >>> is_n_straight_hand([1,2,3,6,2,3,4,7,8], 3)
    True
    >>> is_n_straight_hand([1,2,3,4,5], 4)
    False
    >>> is_n_straight_hand([1,1,2,2,3,3], 3)
    True
    """
    if len(hand) % group_size != 0:
        return False
    heapq.heapify(hand)

    groups = []
    while len(hand) > 0:
        card = heapq.heappop(hand)

        min_group = 100000
        # add card to one of existant groups or create new
        for i in range(len(groups)):
            if card != groups[i][0] + 1:
                min_group = min(min_group, groups[i][0])
                continue

            # increment max value of group, and decrement awaited number of members
            groups[i][0] += 1
            groups[i][1] -= 1

            # remove filled group in memory efficient way
            if groups[i][1] == 0:
                if i < len(groups) - 1:
                    groups[i] = groups[-1]
                groups.pop()
            break
        else:
            if card > min_group:
                return False
            if group_size <= 1:
                break
            # add new group started from current value if consequtive card not found
            groups.append([card, group_size - 1])

    # all groups must be filled and deleted
    return len(groups) == 0


def merge_triplets(triplets: List[List[int]], target: List[int]) -> bool:
    """
    A triplet is an array of three integers. You are given a 2D integer array triplets,
    where triplets[i] = [a_i, b_i, c_i] describes the ith triplet. You are also given an integer array
    target = [x, y, z] that describes the triplet you want to obtain. To obtain target, you may apply the
    following operation on triplets any number of times (possibly zero): Choose two indices (0-indexed)
    i and j (i != j) and update triplets[j] to become [max(a_i, a_j), max(b_i, b_j), max(c_i, c_j)].
    Return true if it is possible to obtain the target triplet [x, y, z] as an element of triplets, or false otherwise.
    [MEDIUM] https://leetcode.com/problems/merge-triplets-to-form-target-triplet/

    >>> merge_triplets([[2,5,3],[1,8,4],[1,7,5]], [2,7,5])
    True
    >>> merge_triplets([[3,4,5],[4,5,6]], [3,2,5])
    False
    >>> merge_triplets([[2,5,3],[2,3,4],[1,2,5],[5,2,3]], [5,5,5])
    True
    """
    max_triplet = [0] * len(target)

    for triplet in triplets:
        for i in range(len(target)):
            # if this triplet is more than target it will ruin max_triplet, so we skip it
            if triplet[i] > target[i]:
                break
        else:
            # we can use max for triplet values without harm
            for i in range(len(triplet)):
                max_triplet[i] = max(max_triplet[i], triplet[i])

    # max triplet is the result of max func for all valid triplet
    # it is either equal to target or it's not possible to find one
    return max_triplet == target


def partition_labels(s: str) -> List[int]:
    """
    You are given a string s. We want to partition the string into as many parts as possible so that each letter
    appears in at most one part. Note that the partition is done so that after concatenating all the parts in order,
    the resultant string should be s. Return a list of integers representing the size of these parts.

    [MEDIUM] https://leetcode.com/problems/partition-labels/

    >>> partition_labels('ababcbacadefegdehijhklij')
    [9, 7, 8]
    >>> partition_labels('eccbbbbdec')
    [10]
    """
    end = {char: i for i, char in enumerate(s)}
    partitions, last_i = [], -1
    for i, char in enumerate(s):
        if i > last_i:
            partitions.append(end[char] - last_i)
            last_i = end[char]
        else:
            partitions[-1] = max(partitions[-1], partitions[-1] + end[char] - last_i)
            last_i = max(last_i, end[char])
    return partitions


def partition_labels_2(s: str) -> List[int]:
    chars = {}
    for i, char in enumerate(s):
        if char not in chars:
            chars[char] = [i, i]
        else:
            chars[char][1] = i

    chars_intervals = list(chars.values())
    return [r - l + 1 for l, r in merge_intervals(chars_intervals)]


def merge_intervals(intervals):
    if not intervals:
        return []
    # sort the intervals based on the start time
    intervals.sort(key=lambda x: x[0])

    merged_intervals = [intervals[0]]
    for current in intervals[1:]:
        last_merged = merged_intervals[-1]

        # check if the current interval overlaps with the last merged interval
        if current[0] < last_merged[1]:
            # merge the intervals by updating the end of the last merged interval
            merged_intervals[-1][1] = max(last_merged[1], current[1])
        else:
            # if they don't overlap, add the current interval to the merged list
            merged_intervals.append(current)

    return merged_intervals


def check_valid_string(s: str) -> bool:
    """
    Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.
    The following rules define a valid string:
    - Any left parenthesis '(' must have a corresponding right parenthesis ')'.
    - Any right parenthesis ')' must have a corresponding left parenthesis '('.
    - Left parenthesis '(' must go before the corresponding right parenthesis ')'.
    - '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string ''.
    [MEDIUM] https://leetcode.com/problems/valid-parenthesis-string/

    >>> check_valid_string('()')
    True
    >>> check_valid_string('(*)')
    True
    >>> check_valid_string('(*))')
    True
    """
    min_left, max_left = 0, 0
    for char in s:
        if char == "(":
            min_left += 1
            max_left += 1
        elif char == ")":
            min_left -= 1
            max_left -= 1
        else:  # "*"
            min_left -= 1
            max_left += 1

        if max_left < 0:
            return False
        min_left = max(min_left, 0)

    return min_left == 0


if __name__ == "__main__":
    import doctest

    doctest.testmod()
