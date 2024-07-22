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


def reverse_bits(n: int) -> int:
    """
    Reverse bits of a given 32 bits unsigned integer.
    [EASY] https://leetcode.com/problems/reverse-bits/

    >>> reverse_bits(0b00000010100101000001111010011100)
    964176192
    >>> reverse_bits(0b11111111111111111111111111111101)
    3221225471
    """
    result = 0
    for i in range(32):
        result <<= 1  # Shift result left to make room for the next bit
        result |= (n & 1)  # Add the least significant bit of n to result
        n >>= 1  # Shift n right to process the next bit
    return result


def missing_number(nums: List[int]) -> int:
    """
    Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range
    that is missing from the array.
    [EASY] https://leetcode.com/problems/missing-number/

    >>> missing_number([3,0,1])
    2
    >>> missing_number([0,1])
    2
    >>> missing_number([9,6,4,2,3,5,7,0,1])
    8
    """
    missing = 0
    for num in nums:
        missing ^= num
    for num in range(1, len(nums) + 1):
        missing ^= num
    return missing
    # return int(((1 + len(nums)) / 2) * len(nums)) - sum(nums)


if __name__ == "__main__":
    import doctest

doctest.testmod()
