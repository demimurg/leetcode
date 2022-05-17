package leetcode

import (
	"math"
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestIsPowerOfThree(t *testing.T) {
	testCases := []struct {
		n      int
		expect bool
	}{
		{n: 3, expect: true},
		{n: 10, expect: false},
		{n: int(math.Pow(3, 4)), expect: true},
		{n: 1e3, expect: false},
		{n: int(math.Pow(3, 12)), expect: true},
		{n: 1e9, expect: false},
		{n: int(math.Pow(3, 36)), expect: true},
	}

	for _, test := range testCases {
		assert.Equal(t, test.expect, isPowerOfThree(test.n))
	}
}
