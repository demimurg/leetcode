package top_easy

import (
	"math/bits"
)

// Write a function that takes the binary representation of an unsigned integer
// and returns the number of '1' bits it has (also known as the Hamming weight).
// https://leetcode.com/explore/interview/card/top-interview-questions-easy/99/others/565/
func hammingWeight(num uint32) (bits int) {
	for ; num != 0; num /= 2 {
		bits += int(num % 2)
	}
	return
}

func hammingWeight2(num uint32) int {
	return bits.OnesCount32(num)
}

// The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
// Given two integers x and y, return the Hamming distance between them.
// https://leetcode.com/explore/interview/card/top-interview-questions-easy/99/others/762/
func hammingDistance(x int, y int) (diff int) {
	for ; x != 0 || y != 0; x, y = x/2, y/2 {
		if x%2 != y%2 {
			diff++
		}
	}
	return
}

// Reverse bits of a given 32 bits unsigned integer.
// https://leetcode.com/explore/interview/card/top-interview-questions-easy/99/others/648/
func reverseBits(num uint32) (reversed uint32) {
	for pow := 31; pow >= 0; pow-- {
		reversed += (num & 1) << pow
		num = num >> 1
	}
	return
}

// Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
// https://leetcode.com/explore/interview/card/top-interview-questions-easy/99/others/601/
func generate(numRows int) [][]int {
	triangle := make([][]int, numRows)
	for i := 0; i < numRows; i++ {
		triangle[i] = make([]int, i+1)
		for j := 0; j <= i; j++ {
			if j == 0 || j == i { // first or last
				triangle[i][j] = 1
				continue
			}
			triangle[i][j] = triangle[i-1][j-1] + triangle[i-1][j]
		}
	}
	return triangle
}

// Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
// determine if the input string is valid. An input string is valid if:
// 1. Open brackets must be closed by the same type of brackets.
// 2. Open brackets must be closed in the correct order.
// https://leetcode.com/explore/interview/card/top-interview-questions-easy/99/others/721/
func isValid(s string) bool {
	var opened []int32
	for _, bracket := range s {
		switch bracket {
		case '(', '{', '[':
			opened = append(opened, bracket)
		case ')', '}', ']':
			last := len(opened) - 1
			if len(opened) == 0 || opened[last] != toOpen[bracket] {
				return false
			}
			opened = opened[:last]
		}
	}

	return len(opened) == 0
}

var toOpen = map[int32]int32{
	')': '(',
	'}': '{',
	']': '[',
}

// Given an array nums containing n distinct numbers in the range [0, n],
// return the only number in the range that is missing from the array.
// https://leetcode.com/explore/interview/card/top-interview-questions-easy/99/others/722/
func missingNumber(nums []int) int {
	n := len(nums)
	x := (n + 1) * n / 2
	for _, num := range nums {
		x -= num
	}
	return x
}
