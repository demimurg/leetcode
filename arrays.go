package leetcode

// Given an integer array nums sorted in non-decreasing order,
// remove the duplicates in-place such that each unique element appears only once.
// The relative order of the elements should be kept the same.
// Return k after placing the final result in the first k slots of nums
// https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/727/
func RemoveDuplicates(nums []int) int {
	k := 1 // k slots guaranteed to be non-duplicate
	for i := range nums {
		if nums[i] != nums[k-1] {
			nums[k] = nums[i]
			k++
		}
	}
	return k
}

// You are given an integer array prices where prices[i] is the price of a given stock on the ith day.
// On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.
// Find and return the maximum profit you can achieve. 0 <= prices[i] <= 10^4
// https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/564/
func MaxProfit(prices []int) int {
	var (
		profit int
		bought int = 1e6 // all prices are lower
	)
	// buy on valley, sell on peak
	for i := range prices {
		if prices[i] < bought {
			bought = prices[i]
		} else if bought < prices[i] && (i == len(prices)-1 || prices[i+1] < prices[i]) {
			profit += prices[i] - bought
			bought = 1e6 // just for correct compare operation
		}

	}
	return profit
}

// another realization, buy/sell stocks each day the cost increases
func MaxProfit2(prices []int) int {
	profit := 0
	for i := 1; i < len(prices); i++ {
		if prices[i] > prices[i-1] {
			profit += prices[i] - prices[i-1]
		}
	}
	return profit
}
