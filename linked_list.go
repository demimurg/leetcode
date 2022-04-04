package leetcode

type ListNode struct {
	Val  int
	Next *ListNode
}

// Write a function to delete a node in a singly-linked list. You will not be given access
// to the head of the list, instead you will be given access to the node to be deleted directly.
// It is guaranteed that the node to be deleted is not a tail node in the list.
// https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/553/
func deleteNode(node *ListNode) {
	node.Val = node.Next.Val
	node.Next = node.Next.Next
}

// Given the head of a linked list, remove the nth node from the end of the list and return its head.
// https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/603/
func removeNthFromEnd(head *ListNode, n int) *ListNode {
	var nodes []*ListNode
	node := head
	for {
		nodes = append(nodes, node)
		if node.Next == nil {
			break
		}
		node = node.Next
	}

	i := len(nodes) - n
	if i+1 < len(nodes) {
		nodes[i].Val = nodes[i+1].Val
		nodes[i].Next = nodes[i+1].Next
	} else if i-1 >= 0 {
		nodes[i-1].Next = nil
	} else {
		head = nil
	}
	return head
}

// Given the head of a singly linked list, reverse the list, and return the reversed list.
// https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/560/
func reverseList(head *ListNode) *ListNode {
	var cur, prev *ListNode
	for cur = head; cur != nil; {
		cur.Next, prev, cur = prev, cur, cur.Next
	}
	return prev
}

// You are given the heads of two sorted linked lists list1 and list2.
// Merge the two lists in a one sorted list. The list should be made by
// splicing together the nodes of the first two lists.
// Return the head of the merged linked list.
// https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/771/
func mergeTwoLists(node1, node2 *ListNode) *ListNode {
	if node1 == nil {
		return node2
	}
	if node2 == nil {
		return node1
	}
	if node2.Val < node1.Val {
		node1, node2 = node2, node1
	}
	head := node1

	for node1 != nil {
		if node1.Next == nil || node2 != nil && node2.Val < node1.Next.Val {
			node1, node1.Next = node1.Next, node2
			node1, node2 = node2, node1
		} else {
			node1 = node1.Next
		}
	}

	return head
}
