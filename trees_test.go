package leetcode

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

const null = -1e10 // out of tree values range (-100 <= TreeNode.Val <= 100)

func ConvertToTreeNode(tree []int) *TreeNode {
	nodes := make([]*TreeNode, len(tree))
	for i, val := range tree {
		if val == null {
			continue
		}
		nodes[i] = &TreeNode{Val: val}
	}
	for i := range nodes {
		if j := i*2 + 1; j < len(nodes) {
			nodes[i].Left = nodes[j]
		}
		if j := i*2 + 2; j < len(nodes) {
			nodes[i].Right = nodes[j]
		}
	}

	return nodes[0]
}

func TestDepth(t *testing.T) {
	testCases := []struct {
		list   []int
		expect int
	}{
		{
			list:   []int{3, 9, 20, null, null, 15, 7},
			expect: 3,
		},
		{
			list:   []int{1, null, 2},
			expect: 2,
		},
	}

	for _, test := range testCases {
		tree := ConvertToTreeNode(test.list)
		assert.Equal(t, test.expect, maxDepth(tree))
	}
}
