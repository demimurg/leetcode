from typing import *


def single_number(nums: List[int]) -> int:
    """
    Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
    
    You must implement a solution with a linear runtime complexity and use only constant extra space.
    [EASY] https://leetcode.com/problems/single-number/
    
    >>> single_number([2, 2, 1])
    1
    >>> single_number([4, 1, 2, 1, 2])
    4
    >>> single_number([1])
    1
    """
    unique = 0
    for num in nums:
        unique ^= num
    return unique


def hamming_weight(n: int) -> int:
    """
    Write a function that takes the binary representation of a positive integer and returns the number of set bits
    it has (also known as the Hamming weight).
    
    [EASY] https://leetcode.com/problems/number-of-1-bits/

    >>> hamming_weight(11)
    3
    >>> hamming_weight(128)
    1
    >>> hamming_weight(2147483645)
    30
    """
    ones = 0
    while n != 0:
        ones += n % 2  # or n & 1
        n //= 2  # or n >>= 1
    return ones


def count_bits(n: int) -> List[int]:
    """
    Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n),
    ans[i] is the number of 1's in the binary representation of i.
    [EASY] https://leetcode.com/problems/counting-bits/

    >>> count_bits(2)
    [0, 1, 1]
    >>> count_bits(5)
    [0, 1, 1, 2, 1, 2]
    """
    nums = [0] * (n + 1)
    offset = 1

    for i in range(1, n + 1):
        if i == 2 * offset:
            offset = i
        nums[i] = 1 + nums[i - offset]

    return nums


if __name__ == "__main__":
    import doctest

    doctest.testmod()
