package top_easy

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func convertToList(head *ListNode) []int {
	var vals []int
	for {
		if head == nil {
			break
		}
		vals = append(vals, head.Val)
		head = head.Next
	}
	return vals
}

func convertToLinkedList(vals []int) *ListNode {
	head := &ListNode{Val: vals[0]}
	node := head
	for _, val := range vals[1:] {
		node.Next = &ListNode{Val: val}
		node = node.Next
	}
	return head
}

func TestDeleteNode(t *testing.T) {
	testCases := []struct {
		list   []int
		i      int
		expect []int
	}{
		{
			list:   []int{1, 2, 3, 4},
			i:      2,
			expect: []int{1, 2, 4},
		},
	}

	for _, test := range testCases {
		head := convertToLinkedList(test.list)
		node := head
		for i := 0; i < test.i; i++ {
			node = node.Next
		}
		deleteNode(node)
		assert.Equal(t, test.expect, convertToList(head))
	}
}

func TestRemoveFromEnd(t *testing.T) {
	testCases := []struct {
		list   []int
		n      int
		expect []int
	}{
		{
			list:   []int{1, 2, 3, 4},
			n:      2,
			expect: []int{1, 2, 4},
		},
	}

	for _, test := range testCases {
		head := removeNthFromEnd(convertToLinkedList(test.list), test.n)
		assert.Equal(t, test.expect, convertToList(head))
	}
}

func TestReverseList(t *testing.T) {
	testCases := []struct {
		list   []int
		expect []int
	}{
		{
			list:   []int{1, 2, 3, 4},
			expect: []int{4, 3, 2, 1},
		},
		{
			list:   []int{1, 2},
			expect: []int{2, 1},
		},
		{
			list:   []int{1},
			expect: []int{1},
		},
	}

	for _, test := range testCases {
		head := reverseList(convertToLinkedList(test.list))
		assert.Equal(t, test.expect, convertToList(head))
	}
}

func TestMergeTwoLists(t *testing.T) {
	testCases := []struct {
		list1, list2 []int
		expect       []int
	}{
		{
			list1:  []int{1, 2, 4},
			list2:  []int{1, 3, 4},
			expect: []int{1, 1, 2, 3, 4, 4},
		},
	}

	for _, test := range testCases {
		head1, head2 := convertToLinkedList(test.list1), convertToLinkedList(test.list2)
		assert.Equal(t, test.expect, convertToList(mergeTwoLists(head1, head2)))
	}
}

func TestIsPalindromeList(t *testing.T) {
	testCases := []struct {
		list   []int
		expect bool
	}{
		{
			list:   []int{1, 2, 2, 1},
			expect: true,
		},
		{
			list:   []int{1, 2},
			expect: false,
		},
	}

	for _, test := range testCases {
		head := convertToLinkedList(test.list)
		assert.Equal(t, test.expect, isPalindromeList(head))
	}
}
