package leetcode

// Given an integer array nums sorted in non-decreasing order,
// remove the duplicates in-place such that each unique element appears only once.
// The relative order of the elements should be kept the same.
// Return k after placing the final result in the first k slots of nums
// https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/727/
func removeDuplicates(nums []int) int {
	k := 1 // k slots guaranteed to be non-duplicate
	for i := range nums {
		if nums[i] != nums[k-1] {
			nums[k] = nums[i]
			k++
		}
	}
	return k
}

// You are given an integer array prices where prices[i] is the price of a given stock on the ith day.
// On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.
// Find and return the maximum profit you can achieve. 0 <= prices[i] <= 10^4
// https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/564/
func maxProfit(prices []int) int {
	var (
		profit int
		bought int = 1e6 // all prices are lower
	)
	// buy on valley, sell on peak
	for i := range prices {
		if prices[i] < bought {
			bought = prices[i]
		} else if bought < prices[i] && (i == len(prices)-1 || prices[i+1] < prices[i]) {
			profit += prices[i] - bought
			bought = 1e6 // just for correct compare operation
		}
	}
	return profit
}

func maxProfit2(prices []int) int {
	// another realization, buy/sell stocks each day the cost increases
	profit := 0
	for i := 1; i < len(prices); i++ {
		if prices[i] > prices[i-1] {
			profit += prices[i] - prices[i-1]
		}
	}
	return profit
}

// Given an array, rotate the array to the right by k steps, where k is non-negative.
// * Try to come up with as many solutions as you can. There are at least three different ways to solve this problem.
// * Could you do it in-place with O(1) extra space?
// https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/646/
func rotate(nums []int, k int) {
	k = k % len(nums) // throw period away
	shift := make([]int, k)
	copy(shift, nums[len(nums)-k:])

	for i := len(nums) - len(shift) - 1; i >= 0; i-- {
		nums[i+len(shift)] = nums[i]
	}
	copy(nums, shift)
}

func rotate2(nums []int, k int) {
	// rotate realization with ram optimized
	k = k % len(nums)
	for i := 0; i < k; i++ {
		buffer := nums[0]
		for j := 0; j < len(nums); j++ {
			next := (j + 1) % len(nums)
			buffer, nums[next] = nums[next], buffer
		}
	}
}

func rotate3(nums []int, k int) {
	// hacky rotate realization, short and efficient
	reverse := func(nums []int) {
		for i := 0; i < len(nums)/2; i++ {
			j := len(nums) - i - 1
			nums[i], nums[j] = nums[j], nums[i]
		}
	}

	k = k % len(nums)
	reverse(nums)
	reverse(nums[:k])
	reverse(nums[k:])
}

// Given an integer array nums, return true if any value appears
// at least twice in the array, and return false if every element is distinct.
// https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/578/
func containsDuplicate(nums []int) bool {
	seen := make(map[int]struct{}) // use struct{} to save memory
	for _, num := range nums {
		if _, ok := seen[num]; ok {
			return true
		}
		seen[num] = struct{}{}
	}
	return false
}

// Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
// * You must implement a solution with a linear runtime complexity and use only constant extra space.
// https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/549/
func singleNumber(nums []int) int {
	res := 0
	for i := range nums {
		res ^= nums[i]
	}
	return res
}

// Given two integer arrays nums1 and nums2, return an array of their intersection.
// Each element in the result must appear as many times as it shows in
// both arrays, and you may return the result in any order.
// https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/674/
func intersect(nums1, nums2 []int) []int {
	count := make(map[int]int)
	for _, n := range nums1 {
		count[n]++
	}

	result := make([]int, 0, len(count))
	for _, n := range nums2 {
		if count[n] > 0 {
			result = append(result, n)
			count[n]--
		}
	}

	return result
}

// You are given a large integer represented as an integer array digits,
// where each digits[i] is the ith digit of the integer. The digits are
// ordered from most significant to the least significant in left-to-right order.
// The large integer does not contain any leading 0's.
// Increment the large integer by one and return the resulting array of digits.
// * 1 <= digits.length <= 100
// * 0 <= digits[i] <= 9
// * digits does not contain any leading 0's.
// https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/559/
func plusOne(digits []int) []int {
	for i := len(digits) - 1; i >= 0; i-- {
		if digits[i] < 9 {
			digits[i]++
			break
		}
		digits[i] = 0
	}

	// slice does not contain any leading 0's, so it can be only overflow (099..9)
	if digits[0] == 0 {
		return append([]int{1}, digits...)
	}
	return digits
}

// Given an integer array nums, move all 0's to the end of it while
// maintaining the relative order of the non-zero elements.
// * note that you must do this in-place without making a copy of the array.
// https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/567/
func moveZeroes(nums []int) {
	j := 0
	for i := 0; i < len(nums); i++ {
		if nums[i] != 0 {
			nums[j] = nums[i]
			j++
		}
	}
	for i := j; i < len(nums); i++ {
		nums[i] = 0
	}
}

// Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
// You may assume that each input would have exactly one solution, and you may not use the same element twice.
// You can return the answer in any order.
// https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/546/
func twoSum(nums []int, target int) []int {
	idx := make(map[int]int)
	for i1, n := range nums {
		if i2, ok := idx[target-n]; ok {
			return []int{i1, i2}
		}
		idx[n] = i1
	}
	return nil
}

// Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
// Each row must contain the digits 1-9 without repetition.
// Each column must contain the digits 1-9 without repetition.
// Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
// https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/769/
func isValidSudoku(board [][]byte) bool {
	var rows, columns, squares [9][9]bool
	for i := range board {
		for j, val := range board[i] {
			if val == '.' {
				continue
			}

			val -= '1' // use array indexes to mark already seen values
			squareIdx := i/3*3 + j/3
			if rows[i][val] || columns[j][val] || squares[squareIdx][val] {
				return false
			}
			rows[i][val], columns[j][val], squares[squareIdx][val] = true, true, true
		}
	}
	return true
}

// You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
// You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
// DO NOT allocate another 2D matrix and do the rotation.
// Constraints:
// * n == matrix.length == matrix[i].length
// * 1 <= n <= 20
// * -1000 <= matrix[i][j] <= 1000
// https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/770/
func rotateImage(matrix [][]int) {
	size := len(matrix)
	// transpose matrix first
	for i := 0; i < size-1; i++ {
		for j := 0; j < size-i-1; j++ {
			invI, invJ := size-i-1, size-j-1
			matrix[i][j], matrix[invJ][invI] = matrix[invJ][invI], matrix[i][j]
		}
	}
	// invert rows (i with size-i-i)
	for i := 0; i < size/2; i++ {
		for j := 0; j < size; j++ {
			invI := size - i - 1
			matrix[i][j], matrix[invI][j] = matrix[invI][j], matrix[i][j]
		}
	}
}
