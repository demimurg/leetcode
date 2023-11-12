package top_easy

import (
	"fmt"
	"github.com/stretchr/testify/assert"
	"strconv"
	"testing"
)

func TestHammingWeight(t *testing.T) {
	testCases := []struct {
		num    uint32
		expect int
	}{
		{
			num:    parseUint("00000000000000000000000000001011"),
			expect: 3,
		},
		{
			num:    parseUint("00000000000000000000000010000000"),
			expect: 1,
		},
		{
			num:    parseUint("11111111111111111111111111111101"),
			expect: 31,
		},
	}

	for _, test := range testCases {
		assert.Equal(t, test.expect, hammingWeight(test.num))
	}
}

func TestHammingDistance(t *testing.T) {
	testCases := []struct {
		x, y   int
		expect int
	}{
		{
			x:      parseInt("0001"), // 1
			y:      parseInt("0100"), // 4
			expect: 2,
		},
		{
			x:      parseInt("0001"), // 1
			y:      parseInt("0011"), // 3
			expect: 1,
		},
	}

	for _, tc := range testCases {
		assert.Equal(t, tc.expect, hammingDistance(tc.x, tc.y))
	}
}

func TestReverseBits(t *testing.T) {
	testCases := []struct {
		num    uint32
		expect uint32
	}{
		{
			num:    parseUint("10"),
			expect: 1,
		},
		{
			num:    parseUint("00000010100101000001111010011100"),
			expect: 964176192,
		},
		{
			num:    parseUint("11111111111111111111111111111101"),
			expect: 3221225471,
		},
	}

	for _, test := range testCases {
		t.Run(strconv.Itoa(int(test.num)), func(t *testing.T) {
			assert.Equal(t, int(test.expect), int(reverseBits(test.num)))
		})
	}
}

func parseUint(binaryStr string) uint32 {
	n, _ := strconv.ParseUint(binaryStr, 2, 32)
	return uint32(n)
}

func parseInt(binaryStr string) int {
	n, _ := strconv.ParseInt(binaryStr, 2, 32)
	return int(n)
}

func TestGenerate(t *testing.T) {
	tests := []struct {
		name     string
		numRows  int
		expected [][]int
	}{
		{
			numRows:  5,
			expected: [][]int{{1}, {1, 1}, {1, 2, 1}, {1, 3, 3, 1}, {1, 4, 6, 4, 1}},
		},
		{
			numRows:  2,
			expected: [][]int{{1}, {1, 1}},
		},
	}

	for _, test := range tests {
		result := generate(test.numRows)
		assert.Equal(t, test.expected, result)
	}
}

func TestIsValid(t *testing.T) {
	tests := []struct {
		input    string
		expected bool
	}{
		{"()", true},
		{"()[]{}", true},
		{"(]", false},
		{"([)]", false},
		{"{[]}", true},
		{"", true},
		{"((({[]})))", true},
	}

	for _, test := range tests {
		t.Run(test.input, func(t *testing.T) {
			assert.Equal(t, test.expected, isValid(test.input))
		})
	}
}

func TestMissingNumber(t *testing.T) {
	tests := []struct {
		input    []int
		expected int
	}{
		{[]int{0}, 1},
		{[]int{0, 1}, 2},
		{[]int{3, 0, 1}, 2},
		{[]int{9, 6, 4, 2, 3, 5, 7, 0, 1}, 8},
	}

	for _, test := range tests {
		t.Run(fmt.Sprintf("%v", test.input), func(t *testing.T) {
			assert.Equal(t, test.expected, missingNumber(test.input))
		})
	}
}
