package leetcode

import "math"

// Write a function that reverses a string. The input string is given as an array of characters s.
// You must do this by modifying the input array in-place with O(1) extra memory.
// https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/879/
func reverseString(s []byte) {
	for left, right := 0, len(s)-1; left < right; left, right = left+1, right-1 {
		s[left], s[right] = s[right], s[left]
	}
}

// Given a signed 32-bit integer x, return x with its digits reversed.
// If reversing x causes the value to go outside the signed
// 32-bit integer range [-2^31, 2^31 - 1], then return 0.
// https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/880/
func reverseInt(x int) int {
	var reversed int
	for x != 0 {
		reversed, x = reversed*10+x%10, x/10
	}
	if reversed > math.MaxInt32 || reversed < -math.MaxInt32 {
		return 0
	}
	return reversed
}

// Given a string s, find the first non-repeating character in it
// and return its index. If it does not exist, return -1.
// * 1 <= s.length <= 10^5
// * s consists of only lowercase English letters.
// https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/881/
func firstUniqChar(s string) int {
	var count [26]int
	for _, char := range s {
		count[char-'a']++ // ascii values for abcd.. stores sequentially, we remove 'a' for correct indexing
	}
	for i, char := range s {
		if count[char-'a'] == 1 {
			return i
		}
	}
	return -1
}
