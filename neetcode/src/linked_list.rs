#[derive(PartialEq, Eq, Clone, Debug)]
pub struct ListNode {
    pub val: i32,
    pub next: Option<Box<ListNode>>,
}

pub fn vec_to_list(vals: Vec<i32>) -> Option<Box<ListNode>> {
    let mut head: Option<Box<ListNode>> = None;
    for &val in vals.iter().rev() {
        let node = ListNode{val, next: head};
        head = Some(Box::new(node));
    }
    head
}


/// Given the head of a singly linked list, reverse the list, and return the reversed list.
/// [EASY] https://leetcode.com/problems/reverse-linked-list/
/// ```rust
/// use neetcode::linked_list::{reverse_list,vec_to_list};
/// // Convert vector to linked list for testing and assume 'vec_to_list' is implemented
/// assert_eq!(reverse_list(vec_to_list(vec![1,2,3,4,5])), vec_to_list(vec![5,4,3,2,1]));
/// assert_eq!(reverse_list(vec_to_list(vec![1,2])), vec_to_list(vec![2,1]));
/// assert_eq!(reverse_list(vec_to_list(vec![])), vec_to_list(vec![]));
/// ```
pub fn reverse_list(mut head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
    let mut prev = None;
    while let Some(mut cur) = head {
        head = cur.next;
        cur.next = prev;
        prev = Some(cur);
    }
    prev
}

/// You are given the heads of two sorted linked lists `list1` and `list2`.
/// Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
/// Return the head of the merged linked list.
/// [EASY] https://leetcode.com/problems/merge-two-sorted-lists/
/// ```rust
/// use neetcode::linked_list::{merge_two_lists,vec_to_list};
/// assert_eq!(
///     merge_two_lists(vec_to_list(vec![1,2,4]), vec_to_list(vec![1,3,4])),
///     vec_to_list(vec![1,1,2,3,4,4])
/// );
/// assert_eq!(merge_two_lists(vec_to_list(vec![]), vec_to_list(vec![])), vec_to_list(vec![]));
/// assert_eq!(merge_two_lists(vec_to_list(vec![]), vec_to_list(vec![0])), vec_to_list(vec![0]));
/// ```
pub fn merge_two_lists(mut list1: Option<Box<ListNode>>, mut list2: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
    let mut head = Box::new(ListNode{val: -1, next: None});
    let mut cur = &mut head;

    while list1.is_some() && list2.is_some() {        
        if list1.as_ref().unwrap().val > list2.as_ref().unwrap().val {
            (list1, list2) = (list2, list1)
        }
        
        cur.next = list1.take();
        cur = cur.next.as_mut().unwrap();
        list1 = cur.next.take();
    }
    cur.next = if list1.is_some() { list1 } else { list2 };
    
    head.next // skip fake first value
}
