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
func MaxProfitReadability(prices []int) int {
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
func MaxProfitShorteness(prices []int) int {
	profit := 0
	for i := 1; i < len(prices); i++ {
		if prices[i] > prices[i-1] {
			profit += prices[i] - prices[i-1]
		}
	}
	return profit
}

// Given an array, rotate the array to the right by k steps, where k is non-negative.
// * Try to come up with as many solutions as you can. There are at least three different ways to solve this problem.
// * Could you do it in-place with O(1) extra space?
func RotateCPU(nums []int, k int) {
	k = k % len(nums)
	shift := make([]int, k)
	copy(shift, nums[len(nums)-k:])

	for i := len(nums) - len(shift) - 1; i >= 0; i-- {
		nums[i+len(shift)] = nums[i]
	}
	copy(nums, shift)
}

func RotateRAM(nums []int, k int) {
	for i := 0; i < k; i++ {
		buffer := nums[0]
		for j := 0; j < len(nums); j++ {
			next := (j + 1) % len(nums)
			buffer, nums[next] = nums[next], buffer
		}
	}
}

func RotateHack(nums []int, k int) {
	reverse := func(nums []int) {
		for i := 0; i < len(nums)/2; i++ {
			j := len(nums) - i - 1
			nums[i], nums[j] = nums[j], nums[i]
		}
	}

	k = k % len(nums)
	reverse(nums)
	reverse(nums[:k])
	reverse(nums[k:])
}
