from typing import *


class ListNode:
    val: Any

    def __init__(self, val=None, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev


def to_simple(head: Optional[ListNode]) -> list:
    simple_list = []
    while head is not None:
        simple_list.append(head.val)
        head = head.next
    return simple_list


def to_linked(simple_list: list) -> Optional[ListNode]:
    if len(simple_list) == 0:
        return None

    head = ListNode(simple_list[0])
    cur_node = head
    for val in simple_list[1:]:
        cur_node.next = ListNode(val)
        cur_node = cur_node.next

    return head


def get_len(head: Optional[ListNode]) -> int:
    size = 0
    while head is not None:
        size += 1
        head = head.next
    return size


def invert_list(head: Optional[ListNode]) -> Optional[ListNode]:
    cur, prev = head, None
    while cur is not None:
        next_copy = cur.next
        cur.next = prev
        prev = cur
        cur = next_copy
    return prev


def reorder_list(head: Optional[ListNode]) -> None:
    """
    You are given the head of a singly linked-list. The list can be represented as: L0 → L1 → … → Ln - 1 → Ln
    Reorder the list to be on the following form L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
    You may not modify the values in the list's nodes. Only nodes themselves may be changed.
    [MEDIUM] https://leetcode.com/problems/reorder-list/
    
    
    >>> linked_list = to_linked([1, 2, 3, 4])
    >>> reorder_list(linked_list)
    >>> to_simple(linked_list)
    [1, 4, 2, 3]
    >>> linked_list = to_linked([1, 2, 3, 4, 5])
    >>> reorder_list(linked_list)
    >>> to_simple(linked_list)
    [1, 5, 2, 4, 3]
    """
    node = head
    for _ in range(get_len(head) // 2):
        node = node.next

    tail = invert_list(node.next)
    node.next = None

    node = head
    while tail is not None:
        node.next = ListNode(tail.val, next=node.next)
        tail = tail.next
        node = node.next.next


def remove_nth_from_end(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    """
    Given the head of a linked list, remove the nth node from the end of the list and return its head.
    [MEDIUM] https://leetcode.com/problems/remove-nth-node-from-end-of-list/
        
    
    > to_simple(remove_nth_from_end(to_linked([1, 2, 3, 4, 5]), 2))
    [1, 2, 3, 5]
    > to_simple(remove_nth_from_end(to_linked([1]), 1))
    []
    > to_simple(remove_nth_from_end(to_linked([1, 2]), 1))
    [1]
    """
    dummy = slow = ListNode(next=head)
    fast = head

    i = 0
    while fast.next is not None:
        i += 1
        fast = fast.next
        slow = slow.next if i >= n else slow

    slow.next = slow.next.next
    return dummy.next


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


def copy_random_list(head: Optional[Node]) -> Optional[Node]:
    """
    A linked list of length n is given such that each node contains an additional random pointer,
    which could point to any node in the list, or null. Construct a deep copy of the list.
    The deep copy should consist of exactly n brand new nodes, where each new node
    has its value set to the value of its corresponding original node.
    Both the next and random pointer of the new nodes should point to new nodes in the copied list
    such that the pointers in the original list and copied list represent the same list state.
    None of the pointers in the new list should point to nodes in the original list.
    [MEDIUM] https://leetcode.com/problems/copy-list-with-random-pointer/
    """
    copy = {None: None}  # original node to copy node
    node = head
    while node is not None:
        copy[node] = Node(node.val)
        node = node.next

    node = head
    while node is not None:
        copy[node].next = copy[node.next]
        copy[node].random = copy[node.random]
        node = node.next

    return copy[head]


def add_two_numbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    """
    You are given two non-empty linked lists representing two non-negative integers.
    The digits are stored in reverse order, and each of their nodes contains a single digit.
    Add the two numbers and return the sum as a linked list.
    You may assume the two numbers do not contain any leading zero, except the number 0 itself.
    [MEDIUM] https://leetcode.com/problems/add-two-numbers/
    
    >>> to_simple(add_two_numbers(to_linked([2, 4, 3]), to_linked([5, 6, 4]))) # 342 + 465 = 807
    [7, 0, 8]
    >>> to_simple(add_two_numbers(to_linked([0]), to_linked([0])))
    [0]
    >>> to_simple(add_two_numbers(to_linked([9, 9, 9, 9, 9, 9, 9]), to_linked([9, 9, 9, 9])))
    [8, 9, 9, 9, 0, 0, 0, 1]
    """
    dummy = node = ListNode()
    carry = 0

    while l1 or l2 or carry:
        total = carry
        if l1:
            total += l1.val
            l1 = l1.next
        if l2:
            total += l2.val
            l2 = l2.next

        node.next = ListNode(total % 10)
        carry = total // 10
        node = node.next

    return dummy.next


def has_cycle(head: Optional[ListNode]) -> bool:
    """
    Given head, the head of a linked list, determine if the linked list has a cycle in it.
    There is a cycle in a linked list if there is some node in the list that can be
    reached again by continuously following the next pointer.
    Internally, pos is used to denote the index of the node that tail's next pointer is connected to.
    Note that pos is not passed as a parameter.
    Return true if there is a cycle in the linked list. Otherwise, return false.
    [MEDIUM] https://leetcode.com/problems/linked-list-cycle/
    """
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False


def find_duplicate(nums: List[int]) -> int:
    """
    Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
    There is only one repeated number in nums, return this repeated number.
    You must solve the problem without modifying the array nums and uses only constant extra space.
    [MEDIUM] https://leetcode.com/problems/find-the-duplicate-number/
    
    >>> find_duplicate([1,3,4,2,2])
    2
    >>> find_duplicate([3,1,3,4,2])
    3
    """
    slow = fast = 0
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break

    slow2 = 0
    while slow2 != slow:
        slow = nums[slow]
        slow2 = nums[slow2]

    return slow


class LRUCache:
    """
    Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.
    Implement the LRUCache class:
    LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
    int get(int key) Return the value of the key if the key exists, otherwise return -1.
    void put(int key, int value) Update the value of the key if the key exists. O
    therwise, add the key-value pair to the cache.
    If the number of keys exceeds the capacity from this operation, evict the least recently used key.
    The functions get and put must each run in O(1) average time complexity.
    
    >>> lru = LRUCache(2)
    >>> lru.put(1, 1) # cache is {1=1}
    >>> lru.put(2, 2) # cache is {1=1, 2=2}
    >>> lru.get(1)    # bubble up to first place
    1
    >>> lru.put(3, 3) # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
    >>> lru.get(2)
    -1
    >>> lru.put(4, 4) # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
    >>> lru.get(1)
    -1
    >>> lru.get(3)
    3
    >>> lru.get(4)
    4
    """
    cap: int
    dict: dict[int, ListNode]
    head: Optional[ListNode]
    last: Optional[ListNode]

    def __init__(self, capacity: int):
        self.cap = capacity
        self.dict = {}
        self.head = None
        self.last = None

    def _bubble_up(self, node: ListNode) -> None:
        if node is self.head:
            return
        if node is self.last:
            self.last = self.last.prev

        link(node.prev, node.next)
        link(node, self.head)
        node.prev = None
        self.head = node

    def get(self, key: int) -> int:
        node = self.dict.get(key)
        if node is None:
            return -1

        self._bubble_up(node)
        return node.val[1]

    def put(self, key: int, value: int) -> None:
        node = self.dict.get(key)
        if node is not None:
            node.val = (key, value)
        elif len(self.dict) == self.cap:
            del self.dict[self.last.val[0]]
            node = self.last
            node.val = (key, value)
        else:
            node = ListNode(val=(key, value))

        self._bubble_up(node)
        self.dict[key] = node
        if len(self.dict) == 1:
            self.last = node


def link(first: Optional[ListNode], second: Optional[ListNode]) -> None:
    if first is not None:
        first.next = second
    if second is not None:
        second.prev = first


if __name__ == "__main__":
    import doctest

    doctest.testmod()
