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
