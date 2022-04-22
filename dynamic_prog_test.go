package leetcode

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
