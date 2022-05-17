package leetcode

import (
	"math"
	"strconv"
)

// Given an integer n, return a string array answer (1-indexed) where:
//
// answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
// answer[i] == "Fizz" if i is divisible by 3.
// answer[i] == "Buzz" if i is divisible by 5.
// answer[i] == i (as a string) if none of the above conditions are true.
// https://leetcode.com/explore/interview/card/top-interview-questions-easy/102/math/743/
func fizzBuzz(n int) []string {
	result := make([]string, n)
	for i := range result {
		div3 := (i+1)%3 == 0
		div5 := (i+1)%5 == 0

		switch {
		case div3 && div5:
			result[i] = "FizzBuzz"
		case div3:
			result[i] = "Fizz"
		case div5:
			result[i] = "Buzz"
		default:
			result[i] = strconv.Itoa(i + 1)
		}
	}

	return result
}

// Given an integer n, return the number of prime numbers that are strictly less than n.
// https://leetcode.com/explore/interview/card/top-interview-questions-easy/102/math/744/
func countPrimes(n int) int {
	isPrime := make([]bool, n)
	for i := range isPrime {
		isPrime[i] = true
	}

	for i := 2; i < n; i++ {
		if !isPrime[i] {
			continue
		}
		for j := i * i; j < n; j++ {
			if j%i == 0 {
				isPrime[j] = false
			}
		}
	}

	primeN := 0
	for i := 2; i < n; i++ {
		if isPrime[i] {
			primeN++
		}
	}
	return primeN
}

// Given an integer n, return true if it is a power of three. Otherwise, return false.
// An integer n is a power of three, if there exists an integer x such that n == 3^x.
// https://leetcode.com/explore/interview/card/top-interview-questions-easy/102/math/745/
func isPowerOfThree(n int) bool {
	x := math.Log10(float64(n)) / math.Log10(3) // equal to log3(n)
	return math.Abs(x-math.Round(x)) < 1e-10    // lower than epsilon
}

func isPowerOfThree2(n int) bool {
	if n == 1 {
		return true
	}
	if n < 1 || n%3 != 0 {
		return false
	}
	return isPowerOfThree(n / 3)
}

func isPowerOfThree3(n int) bool {
	if n < 1 {
		return false
	}
	for n%3 == 0 {
		n /= 3
	}
	return n == 1
}

// Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
//
// Symbol       Value
// I             1
// V             5
// X             10
// L             50
// C             100
// D             500
// M             1000
// For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.
//
// Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:
//
// I can be placed before V (5) and X (10) to make 4 and 9.
// X can be placed before L (50) and C (100) to make 40 and 90.
// C can be placed before D (500) and M (1000) to make 400 and 900.
// Given a roman numeral, convert it to an integer.
// Constraints:
// * 1 <= s.length <= 15
// * s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
// * It is guaranteed that s is a valid roman numeral in the range [1, 3999].
// https://leetcode.com/explore/interview/card/top-interview-questions-easy/102/math/878/
func romanToInt(s string) int {
	var (
		result, n int
		lastRoman rune
	)
	for _, char := range s {
		if char != lastRoman {
			if r2i[lastRoman] < r2i[char] {
				n = -n
			}
			result += n
			n = 0
		}
		n += r2i[char]
		lastRoman = char
	}
	return result + n
}

var r2i = map[rune]int{
	'I': 1,
	'V': 5,
	'X': 10,
	'L': 50,
	'C': 100,
	'D': 500,
	'M': 1000,
}
