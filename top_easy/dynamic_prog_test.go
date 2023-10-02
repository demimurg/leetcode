package top_easy

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestClimbStairs(t *testing.T) {
	testCases := []struct {
		n, expect int
	}{
		{n: 2, expect: 2},
		{n: 3, expect: 3},
	}

	for _, test := range testCases {
		assert.Equal(t, test.expect, climbStairs(test.n))
	}
}

func TestMaxProfitAtAll(t *testing.T) {
	testCases := []struct {
		prices []int
		expect int
	}{
		{prices: []int{7, 1, 5, 3, 6, 4}, expect: 5},
		{prices: []int{7, 6, 4, 3, 1}, expect: 0},
	}

	for _, test := range testCases {
		assert.Equal(t, test.expect, maxProfitAtAll(test.prices))
	}
}

func TestMaxSubArray(t *testing.T) {
	testCases := []struct {
		nums   []int
		expect int
	}{
		// [4,-1,2,1] has the largest sum = 6
		{nums: []int{-2, 1, -3, 4, -1, 2, 1, -5, 4}, expect: 6},
		{nums: []int{5, 4, -1, 7, 8}, expect: 23},
	}

	for _, test := range testCases {
		assert.Equal(t, test.expect, maxSubArray(test.nums))
	}
}

func TestRob(t *testing.T) {
	testCases := []struct {
		nums   []int
		expect int
	}{
		{nums: []int{1, 2, 3, 1}, expect: 4},
		{nums: []int{2, 7, 9, 3, 1}, expect: 12},
		{nums: []int{2, 1, 1, 2}, expect: 4},
	}

	for _, test := range testCases {
		assert.Equal(t, test.expect, rob(test.nums))
	}
}
