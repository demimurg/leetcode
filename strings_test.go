package leetcode

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestReverseString(t *testing.T) {
	for _, test := range []struct {
		str    []byte
		expect []byte
	}{
		{
			str:    []byte{'h', 'e', 'l', 'l', 'o'},
			expect: []byte{'o', 'l', 'l', 'e', 'h'},
		},
		{
			str:    []byte{'H', 'a', 'n', 'n', 'a', 'h'},
			expect: []byte{'h', 'a', 'n', 'n', 'a', 'H'},
		},
	} {
		// reverse string in place
		reverseString(test.str)
		assert.Equal(t, test.expect, test.str)
	}
}

func TestReverseInt(t *testing.T) {
	for _, test := range []struct {
		x, expect int
	}{
		{151, 151},
		{1350, 531},
		{-321, -123},
	} {
		assert.Equal(t, test.expect, reverseInt(test.x))
	}
}

func TestFirstUniqChar(t *testing.T) {
	for _, test := range []struct {
		s      string
		expect int
	}{
		{"leetcode", 0},
		{"loveleetcode", 2},
		{"aabb", -1},
	} {
		assert.Equal(t, test.expect, firstUniqChar(test.s))
	}
}
