package leetcode

import (
	"math"
	"unicode"
)

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

// Given two strings s and t, return true if t is an anagram of s, and false otherwise.
// An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
// typically using all the original letters exactly once.
// https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/882/
func isAnagram(s string, t string) bool {
	if len(s) != len(t) {
		return false
	}

	var alphabet [26]int16
	for i := range s {
		alphabet[s[i]-'a']++
		alphabet[t[i]-'a']--
	}

	for _, count := range alphabet {
		if count != 0 {
			return false
		}
	}
	return true
}

// A phrase is a palindrome if, after converting all uppercase letters into lowercase letters
// and removing all non-alphanumeric characters, it reads the same forward and backward.
// Alphanumeric characters include letters and numbers.
// Given a string s, return true if it is a palindrome, or false otherwise.
// * byte representation: 0-9 (48-57), A-Z (65-90), a-z (97-122)
// https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/883/
func isPalindrome(s string) bool {
	filtered := make([]rune, 0, len(s))
	for _, char := range s {
		if !unicode.IsNumber(char) && !unicode.IsLetter(char) {
			continue
		} else if unicode.IsUpper(char) {
			char = unicode.ToLower(char)
		}
		filtered = append(filtered, char)
	}

	for i := 0; i < len(filtered)/2; i++ {
		if filtered[i] != filtered[len(filtered)-i-1] {
			return false
		}
	}
	return true
}
