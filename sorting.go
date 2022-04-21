package leetcode

// You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
// Merge nums1 and nums2 into a single array sorted in non-decreasing order.
// The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
// https://leetcode.com/explore/interview/card/top-interview-questions-easy/96/sorting-and-searching/587/
func merge(nums1 []int, m int, nums2 []int, n int) {
	nums1Only := make([]int, m)
	copy(nums1Only, nums1)

	m, n = 0, 0
	for i := range nums1 {
		if m != len(nums1Only) && (n == len(nums2) || nums1Only[m] < nums2[n]) {
			nums1[i] = nums1Only[m]
			m++
		} else {
			nums1[i] = nums2[n]
			n++
		}
	}
}

// You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.
// Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.
// You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.
// https://leetcode.com/explore/interview/card/top-interview-questions-easy/96/sorting-and-searching/774/
/*
 * Forward declaration of isBadVersion API.
 * @param   version   your guess about first bad version
 * @return 	 	      true if current version is bad
 *			          false if current version is good
 * func isBadVersion(version int) bool;
 */
// func firstBadVersion(n int) int {
//    m := 0
//    for n - m > 1 {
//        if mid := (m + n) / 2; isBadVersion(mid) {
//            n = mid
//        } else {
//            m = mid
//        }
//    }
//    return n
// }
