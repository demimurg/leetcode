package leetcode

import "math"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

// Given the root of a binary tree, return its maximum depth.
// A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
// https://leetcode.com/explore/interview/card/top-interview-questions-easy/94/trees/555/
func maxDepth(root *TreeNode) int {
	var maxDepth int
	var dfs func(*TreeNode, int) // Depth-first search
	dfs = func(node *TreeNode, depth int) {
		if node == nil {
			if depth > maxDepth {
				maxDepth = depth
			}
			return
		}
		depth++
		dfs(node.Left, depth)
		dfs(node.Right, depth)
	}
	dfs(root, 0)
	return maxDepth
}

// Given the root of a binary tree, determine if it is a valid binary search tree (BST).
// A valid BST is defined as follows:
// The left subtree of a node contains only nodes with keys less than the node's key.
// The right subtree of a node contains only nodes with keys greater than the node's key.
// Both the left and right subtrees must also be binary search trees.
// https://leetcode.com/explore/interview/card/top-interview-questions-easy/94/trees/625/
func isValidBST(root *TreeNode) bool {
	var isValid func(*TreeNode, int, int) bool
	isValid = func(node *TreeNode, min, max int) bool {
		if node == nil {
			return true
		}
		if node.Val <= min || node.Val >= max {
			return false
		}
		return isValid(node.Left, min, node.Val) && isValid(node.Right, node.Val, max)
	}
	return isValid(root, -math.MaxInt64, math.MaxInt64)
}

// Given the root of a binary tree, check whether it is a mirror of itself
// (i.e., symmetric around its center).
// https://leetcode.com/explore/interview/card/top-interview-questions-easy/94/trees/627/
func isSymmetric(root *TreeNode) bool {
	var dfs func(left, right *TreeNode) bool
	dfs = func(l, r *TreeNode) bool {
		if l == nil || r == nil {
			return l == r
		}
		return l.Val == r.Val && dfs(l.Left, r.Right) && dfs(l.Right, r.Left)
	}
	return dfs(root.Left, root.Right)
}

// Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).
// https://leetcode.com/explore/interview/card/top-interview-questions-easy/94/trees/628/
func levelOrder(root *TreeNode) [][]int {
	var lis [][]int
	var f func(*TreeNode, int)
	f = func(node *TreeNode, level int) {
		if node == nil {
			return
		}
		if level >= len(lis) {
			lis = append(lis, []int{})
		}
		lis[level] = append(lis[level], node.Val)
		level++
		f(node.Left, level)
		f(node.Right, level)
	}
	f(root, 0)
	return lis
}
