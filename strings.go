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

// Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).
// The algorithm for myAtoi(string s) is as follows:
// Read in and ignore any leading whitespace.
// Check if the next character (if not already at the end of the string) is '-' or '+'. Read this character in if it is either. This determines if the final result is negative or positive respectively. Assume the result is positive if neither is present.
// Read in next the characters until the next non-digit character or the end of the input is reached. The rest of the string is ignored.
// Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).
// If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then clamp the integer so that it remains in the range. Specifically, integers less than -231 should be clamped to -231, and integers greater than 231 - 1 should be clamped to 231 - 1.
// Return the integer as the final result.
// Note:
// Only the space character ' ' is considered a whitespace character.
// Do not ignore any characters other than the leading whitespace or the rest of the string after the digits.
// https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/884/
func myAtoi(s string) int {
	bytes, i := []byte(s), 0
	for ; i < len(bytes); i++ {
		if bytes[i] != ' ' {
			break
		}
	}
	if i == len(bytes) {
		return 0
	}

	var negative bool
	if bytes[i] == '-' {
		negative = true
		i++
	} else if bytes[i] == '+' {
		i++
	}

	var n int
	for _, char := range bytes[i:] {
		if char < '0' || char > '9' {
			break
		}
		n = n*10 + int(char-'0')
		if n > math.MaxInt32 {
			break
		}
	}

	if negative {
		if n > math.MaxInt32 {
			n = -math.MaxInt32 - 1
		} else {
			n *= -1
		}
	} else if n >= math.MaxInt32 {
		n = math.MaxInt32
	}
	return n
}

// Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
// (find first entry of the needle substring to haystack string and return index)
// https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/885/
func strStr(haystack string, needle string) int {
	if len(needle) == 0 {
		return 0
	}
	needleBytes := []byte(needle)
LOOP:
	for i := range haystack {
		if haystack[i] != needleBytes[0] {
			continue
		}
		for j := range needleBytes {
			if i+j == len(haystack) || haystack[i+j] != needleBytes[j] {
				continue LOOP
			}
		}
		return i
	}
	return -1
}
