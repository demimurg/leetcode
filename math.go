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
