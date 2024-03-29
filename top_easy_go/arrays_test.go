package top_easy

import (
	"testing"

	"github.com/stretchr/testify/assert"
	"github.com/stretchr/testify/require"
)

func TestRemoveDuplicates(t *testing.T) {
	for _, test := range []struct {
		sortedList []int
		expect     []int
	}{
		{
			sortedList: []int{1, 2, 3},
			expect:     []int{1, 2, 3},
		},
		{
			sortedList: []int{1, 1, 2, 3},
			expect:     []int{1, 2, 3},
		},
		{
			sortedList: []int{1, 1, 2, 3, 3, 3, 4, 5, 5},
			expect:     []int{1, 2, 3, 4, 5},
		},
	} {
		// remove duplicates in place and don't change slice size
		i := removeDuplicates(test.sortedList)
		assert.Equal(t, test.expect, test.sortedList[:i])
	}
}

func TestMaxProfit(t *testing.T) {
	tests := []struct {
		prices []int
		expect int
	}{
		{
			prices: []int{7, 1, 5, 3, 6, 4},
			expect: 7,
			// Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
			// Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
			// Total profit is 4 + 3 = 7.
		},
		{
			prices: []int{1, 2, 3, 4, 5},
			expect: 4,
			// Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
			// Total profit is 4.
		},
		{
			prices: []int{7, 6, 4, 3, 1},
			expect: 0,
			// There is no way to make a positive profit, so we never buy the stock to achieve the maximum profit of 0.
		},
		{
			prices: []int{3, 3},
			expect: 0,
		},
	}
	for _, test := range tests {
		assert.Equal(t, test.expect, maxProfit(test.prices))
	}
}

func TestRotate(t *testing.T) {
	tests := []struct {
		nums   []int
		k      int
		expect []int
	}{
		{
			nums: []int{1, 2, 3, 4, 5, 6, 7}, k: 3,
			expect: []int{5, 6, 7, 1, 2, 3, 4},
		},
		{
			nums: []int{-1, -100, 3, 99}, k: 2,
			expect: []int{3, 99, -1, -100},
		},
		{
			nums: []int{1}, k: 0,
			expect: []int{1},
		},
	}
	for _, test := range tests {
		rotate(test.nums, test.k) // in place
		assert.Equal(t, test.expect, test.nums)
	}
}

func TestContainsDuplicate(t *testing.T) {
	tests := []struct {
		nums   []int
		expect bool
	}{
		{
			nums:   []int{1, 2, 3, 1},
			expect: true,
		},
		{
			nums:   []int{1, 2, 3, 4},
			expect: false,
		},
		{
			nums:   []int{1, 1, 1, 3, 3, 4, 3, 2, 4, 2},
			expect: true,
		},
	}
	for _, test := range tests {
		assert.Equal(t, test.expect, containsDuplicate(test.nums))
	}
}

func TestSingleNumber(t *testing.T) {
	tests := []struct {
		nums   []int
		expect int
	}{
		{
			nums:   []int{2, 2, 1},
			expect: 1,
		},
		{
			nums:   []int{4, 1, 2, 1, 2},
			expect: 4,
		},
		{
			nums:   []int{1},
			expect: 1,
		},
	}
	for _, test := range tests {
		assert.Equal(t, test.expect, singleNumber(test.nums))
	}
}

func TestIntersect(t *testing.T) {
	tests := []struct {
		nums1, nums2 []int
		expect       []int
	}{
		{
			nums1:  []int{1, 2, 2, 1},
			nums2:  []int{2, 2},
			expect: []int{2, 2},
		},
		{
			nums1:  []int{4, 9, 5},
			nums2:  []int{9, 4, 9, 8, 4},
			expect: []int{4, 9},
		},
	}
	for _, test := range tests {
		assert.ElementsMatch(
			t, test.expect,
			intersect(test.nums1, test.nums2),
		)
	}
}

func TestPlusOne(t *testing.T) {
	tests := []struct {
		nums   []int
		expect []int
	}{
		{
			nums:   []int{1, 2, 3},
			expect: []int{1, 2, 4},
		},
		{
			nums:   []int{4, 3, 2, 1},
			expect: []int{4, 3, 2, 2},
		},
		{
			nums:   []int{9},
			expect: []int{1, 0},
		},
		{
			nums:   []int{8, 9},
			expect: []int{9, 0},
		},
	}
	for _, test := range tests {
		assert.Equal(t, test.expect, plusOne(test.nums))
	}
}

func TestMoveZeroes(t *testing.T) {
	tests := []struct {
		nums   []int
		expect []int
	}{
		{
			nums:   []int{0, 1, 0, 3, 12},
			expect: []int{1, 3, 12, 0, 0},
		},
		{
			nums:   []int{0},
			expect: []int{0},
		},
	}
	for _, test := range tests {
		moveZeroes(test.nums)
		assert.Equal(t, test.expect, test.nums)
	}
}

func TestTwoSum(t *testing.T) {
	tests := []struct {
		nums   []int
		target int
		expect []int
	}{
		{
			nums: []int{2, 7, 11, 15}, target: 9,
			expect: []int{0, 1},
		},
		{
			nums: []int{3, 2, 4}, target: 6,
			expect: []int{1, 2},
		},
		{
			nums: []int{3, 3}, target: 6,
			expect: []int{0, 1},
		},
	}
	for _, test := range tests {
		assert.ElementsMatch(t, test.expect, twoSum(test.nums, test.target))
	}
}

func TestIsValidSudoku(t *testing.T) {
	assert.Equal(t, true, isValidSudoku([][]byte{
		{'5', '3', '.' /**/, '.', '7', '.' /**/, '.', '.', '.'},
		{'6', '.', '.' /**/, '1', '9', '5' /**/, '.', '.', '.'},
		{'.', '9', '8' /**/, '.', '.', '.' /**/, '.', '6', '.'},
		/*****************************************************/
		{'8', '.', '.' /**/, '.', '6', '.' /**/, '.', '.', '3'},
		{'4', '.', '.' /**/, '8', '.', '3' /**/, '.', '.', '1'},
		{'7', '.', '.' /**/, '.', '2', '.' /**/, '.', '.', '6'},
		/*****************************************************/
		{'.', '6', '.' /**/, '.', '.', '.' /**/, '2', '8', '.'},
		{'.', '.', '.' /**/, '4', '1', '9' /**/, '.', '.', '5'},
		{'.', '.', '.' /**/, '.', '8', '.' /**/, '.', '7', '9'},
	}))
}

func TestRotateImage(t *testing.T) {
	tests := []struct {
		matrix [][]int
		expect [][]int
	}{
		{
			matrix: [][]int{
				{1, 2, 3},
				{4, 5, 6},
				{7, 8, 9},
			},
			expect: [][]int{
				{7, 4, 1},
				{8, 5, 2},
				{9, 6, 3},
			},
		},
		{
			matrix: [][]int{
				{5, 1, 9, 11},
				{2, 4, 8, 10},
				{13, 3, 6, 7},
				{15, 14, 12, 16},
			},
			expect: [][]int{
				{15, 13, 2, 5},
				{14, 3, 4, 1},
				{12, 6, 8, 9},
				{16, 7, 10, 11},
			},
		},
	}
	for _, test := range tests {
		rotateImage(test.matrix)
		require.Equal(t, test.expect, test.matrix)
	}
}
