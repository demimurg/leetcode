package top_easy

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestMerge(t *testing.T) {
	testCases := []struct {
		m, n               int
		num1, num2, expect []int
	}{
		{
			num1:   []int{1, 2, 3, 0, 0, 0},
			m:      3,
			num2:   []int{2, 5, 6},
			n:      3,
			expect: []int{1, 2, 2, 3, 5, 6},
		},
		{
			num1:   []int{1},
			m:      1,
			num2:   []int{},
			n:      0,
			expect: []int{1},
		},
	}

	for _, test := range testCases {
		merge(test.num1, test.m, test.num2, test.n)
		assert.Equal(t, test.expect, test.num1)
	}
}
