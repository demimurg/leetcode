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

func TestIsAnagram(t *testing.T) {
	for _, test := range []struct {
		s, t   string
		expect bool
	}{
		{"anagram", "nagaram", true},
		{"rat", "car", false},
	} {
		assert.Equal(t, test.expect, isAnagram(test.s, test.t))
	}
}

func TestIsPalindrome(t *testing.T) {
	for _, test := range []struct {
		s      string
		expect bool
	}{
		// converts to: "amanaplanacanalpanama"
		{"A man, a plan, a canal: Panama", true},
		// "raceacar" is not a palindrome
		{"race a car", false},
		// empty string reads the same forward and backward
		{"", true},
		// "remove all non-alphanumeric", so numbers should be in place
		{"0P", false},
	} {
		assert.Equalf(
			t, test.expect, isPalindrome(test.s),
			"%q not a palindrom", test.s,
		)
	}
}
