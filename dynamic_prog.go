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

// Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
// A subarray is a contiguous part of an array.
// https://leetcode.com/explore/interview/card/top-interview-questions-easy/97/dynamic-programming/566/
func maxSubArray(nums []int) int {
	sum, maxSum := 0, -math.MaxInt32
	for _, num := range nums {
		sum += num
		if sum > maxSum {
			maxSum = sum
		}
		if sum < 0 {
			// it can only get worse
			sum = 0
		}
	}
	return maxSum
}

// You are a professional robber planning to rob houses along a street.
// Each house has a certain amount of money stashed, the only constraint stopping
// you from robbing each of them is that adjacent houses have security systems connected
// and it will automatically contact the police if two adjacent houses were broken into on the same night.
// Given an integer array nums representing the amount of money of each house,
// return the maximum amount of money you can rob tonight without alerting the police.
// https://leetcode.com/explore/interview/card/top-interview-questions-easy/97/dynamic-programming/576/
func rob(nums []int) int {
	var rob1, rob2 int
	for _, n := range nums {
		rob1, rob2 = rob2, max(n+rob1, rob2)
	}
	return rob2
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}
