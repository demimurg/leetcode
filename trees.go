package leetcode

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
