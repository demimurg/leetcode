package leetcode

import (
	"testing"

	"github.com/stretchr/testify/assert"
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
		i := RemoveDuplicates(test.sortedList)
		assert.Equal(t, test.expect, test.sortedList[:i])
	}
}
