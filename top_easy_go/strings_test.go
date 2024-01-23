package top_easy

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

func TestMyAtoi(t *testing.T) {
	for _, test := range []struct {
		s      string
		expect int
	}{
		{"42", 42},
		{"   -42", -42},
		{"4193 with words", 4193},
		{"-91283472332", -2147483648},
		{"9223372036854775808", 2147483647},
	} {
		t.Run(test.s, func(t *testing.T) {
			assert.Equal(t, test.expect, myAtoi(test.s))
		})

	}
}

func TestStrStr(t *testing.T) {
	for _, test := range []struct {
		haystack, needle string
		expect           int
	}{
		{"hello", "ll", 2},
		{"aaaaa", "bba", -1},
		{"", "", 0},
		{"mississippi", "issip", 4},
	} {
		assert.Equal(t, test.expect, strStr(test.haystack, test.needle))
	}
}

func TestLongestCommonPrefix(t *testing.T) {
	for _, test := range []struct {
		strs   []string
		expect string
	}{
		{[]string{"flower", "flow", "flight"}, "fl"},
		{[]string{"dog", "racecar", "car"}, ""},
		{[]string{"dog", "dog", "dog"}, "dog"},
	} {
		assert.Equal(t, test.expect, longestCommonPrefix(test.strs))
	}
}
