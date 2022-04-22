package leetcode

import "math"

// You are climbing a staircase. It takes n steps to reach the top.
// Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
// https://leetcode.com/explore/interview/card/top-interview-questions-easy/97/dynamic-programming/569/
func climbStairs(n int) int {
	a, b := 1, 1
	for i := 0; i < n-1; i++ {
		a, b = a+b, a
	}
	return a
}

// You are given an array prices where prices[i] is the price of a given stock on the ith day.
// You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
// Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
// https://leetcode.com/explore/interview/card/top-interview-questions-easy/97/dynamic-programming/572/
func maxProfitAtAll(prices []int) int {
	profit, min := 0, math.MaxInt32
	for _, price := range prices {
		if price < min {
			min = price
			continue
		}
		if price-min > profit {
			profit = price - min
		}
	}
	return profit
}
