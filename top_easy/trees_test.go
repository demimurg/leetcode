package top_easy

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

const null = -1e10 // out of array values range (-100 <= TreeNode.Val <= 100)

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
		tree   []int
		expect int
	}{
		{
			tree:   []int{3, 9, 20, null, null, 15, 7},
			expect: 3,
		},
		{
			tree:   []int{1, null, 2},
			expect: 2,
		},
	}

	for _, test := range testCases {
		tree := ConvertToTreeNode(test.tree)
		assert.Equal(t, test.expect, maxDepth(tree))
	}
}

func TestIsValidBST(t *testing.T) {
	testCases := []struct {
		tree   []int
		expect bool
	}{
		{
			tree:   []int{2, 1, 3},
			expect: true,
		},
		{
			tree:   []int{5, 1, 4, null, null, 3, 6},
			expect: false,
		},
	}

	for _, test := range testCases {
		tree := ConvertToTreeNode(test.tree)
		assert.Equal(t, test.expect, isValidBST(tree))
	}
}

func TestIsSymmetric(t *testing.T) {
	testCases := []struct {
		tree   []int
		expect bool
	}{
		{
			tree:   []int{1, 2, 2, 3, 4, 4, 3},
			expect: true,
		},
		{
			tree:   []int{1, 2, 2, null, 3, null, 3},
			expect: false,
		},
	}

	for _, test := range testCases {
		tree := ConvertToTreeNode(test.tree)
		assert.Equal(t, test.expect, isSymmetric(tree))
	}
}

func TestLevelOrder(t *testing.T) {
	testCases := []struct {
		tree   []int
		expect [][]int
	}{
		{
			tree:   []int{3, 9, 20, null, null, 15, 7},
			expect: [][]int{{3}, {9, 20}, {15, 7}},
		},
		{
			tree:   []int{1},
			expect: [][]int{{1}},
		},
	}

	for _, test := range testCases {
		tree := ConvertToTreeNode(test.tree)
		assert.Equal(t, test.expect, levelOrder(tree))
	}
}

func TestSortedArrayToBST(t *testing.T) {
	testCases := []struct {
		array      []int
		expectTree []int
	}{
		{
			array:      []int{-10, -3, 0, 5, 9},
			expectTree: []int{0, -3, 9, -10, null, 5},
		},
		{
			array:      []int{1, 3},
			expectTree: []int{3, 1},
		},
	}

	for _, test := range testCases {
		assert.Equal(t, ConvertToTreeNode(test.expectTree), sortedArrayToBST(test.array))
	}
}
