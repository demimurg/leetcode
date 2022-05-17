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

func TestRomanToInt(t *testing.T) {
	testCases := []struct {
		roman  string
		expect int
	}{
		{roman: "III", expect: 3},
		{roman: "LVIII", expect: 58},
		{roman: "MCMXCIV", expect: 1994},
	}

	for _, test := range testCases {
		t.Run(test.roman, func(t *testing.T) {
			assert.Equal(t, test.expect, romanToInt(test.roman))
		})
	}
}
