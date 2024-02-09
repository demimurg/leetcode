from typing import *
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def tree_to_list(tree: Optional[TreeNode]) -> List[int]:
    queue, lis = deque([tree]), []
    while len(queue) > 0:
        node = queue.popleft()
        if node is not None:
            lis.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            lis.append(None)
    while len(lis) > 0 and lis[-1] is None:
        lis.pop()

    return lis


def list_to_tree(lis: List[Optional[int]]) -> Optional[TreeNode]:
    if len(lis) == 0:
        return None

    root = TreeNode(lis[0])  # the first element is the root
    queue = deque([root])  # use a queue to keep track of nodes
    i = 1  # start with the second element in the list

    while i < len(lis):
        current = queue.popleft()  # get the next node from the queue
        if lis[i] is not None:  # check if the left child exists
            current.left = TreeNode(lis[i])
            queue.append(current.left)
        i += 1  # move to the next element

        if i < len(lis) and lis[i] is not None:  # check if the right child exists
            current.right = TreeNode(lis[i])
            queue.append(current.right)
        i += 1  # move to the next element

    return root


def invert_tree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    """
    Given the root of a binary tree, invert the tree, and return its root.
    
    >>> tree_to_list(invert_tree(list_to_tree([4, 2, 7, 1, 3, 6, 9])))
    [4, 7, 2, 9, 6, 3, 1]
    >>> tree_to_list(invert_tree(list_to_tree([2, 1, 3])))
    [2, 3, 1]
    >>> tree_to_list(invert_tree(list_to_tree([])))
    []
    """
    if root is None:
        return None
    root.left, root.right = root.right, root.left
    invert_tree(root.left)
    invert_tree(root.right)
    return root


def max_depth(root: Optional[TreeNode]) -> int:
    """
    Given the root of a binary tree, return its maximum depth.
    A binary tree's maximum depth is the number of nodes along the longest path
    from the root node down to the farthest leaf node.
    
    >>> max_depth(list_to_tree([3,9,20,None,None,15,7]))
    3
    >>> max_depth(list_to_tree([]))
    0
    """
    return 1 + max(max_depth(root.left), max_depth(root.right)) if root else 0


def diameter_of_binary_tree(root: Optional[TreeNode]) -> int:
    """
    Given the root of a binary tree, return the length of the diameter of the tree.
    The diameter of a binary tree is the length of the longest path between any two nodes in a tree.
    This path may or may not pass through the root.
    The length of a path between two nodes is represented by the number of edges between them.

    >>> diameter_of_binary_tree(list_to_tree([1,2,3,4,5]))
    3
    >>> diameter_of_binary_tree(list_to_tree([1,2]))
    1
    """
    max_path = 0

    def dfs(node: Optional[TreeNode]) -> int:
        if not node:
            return 0
        left_depth = dfs(node.left)
        right = dfs(node.right)
        nonlocal max_path
        max_path = max(max_path, left_depth + right)

        return 1 + max(left_depth, right)

    dfs(root)
    return max_path


def is_balanced(root: Optional[TreeNode]) -> bool:
    """
    Given a binary tree, determine if it is height-balanced

    >>> is_balanced(list_to_tree([3,9,20,None,None,15,7]))
    True
    >>> is_balanced(list_to_tree([1,2,2,3,3,None,None,4,4]))
    False
    >>> is_balanced(list_to_tree([]))
    True
    """
    root_balanced = True

    def dfs(node: Optional[TreeNode]) -> int:
        if not node:
            return 0
        depth_left = dfs(node.left)
        depth_right = dfs(node.right)

        nonlocal root_balanced
        if abs(depth_left - depth_right) > 1:
            root_balanced = False

        return 1 + max(depth_left, depth_right)

    dfs(root)
    return root_balanced


def is_same_tree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    """
    Given the roots of two binary trees p and q, write a function to check if they are the same or not.
    Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

    >>> is_same_tree(list_to_tree([1,2,3]), list_to_tree([1,2,3]))
    True
    >>> is_same_tree(list_to_tree([1,2]), list_to_tree([1,None,2]))
    False
    >>> is_same_tree(list_to_tree([1,2,1]), list_to_tree([1,1,2]))
    False
    """
    return (p is None and q is None) or \
        p is not None and q is not None and p.val == q.val and \
        is_same_tree(p.left, q.left) and \
        is_same_tree(p.right, q.right)


def is_subtree(root: Optional[TreeNode], sub_root: Optional[TreeNode]) -> bool:
    """
    Given the roots of two binary trees root and subRoot, return true if there is a subtree
    of root with the same structure and node values of subRoot and false otherwise.
    A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants.
    The tree tree could also be considered as a subtree of itself.

    >>> is_subtree(list_to_tree([3,4,5,1,2]), list_to_tree([4,1,2]))
    True
    >>> is_subtree(list_to_tree([3,4,5,1,2,None,None,None,None,0]), list_to_tree([4,1,2]))
    False
    """
    if root is None:
        return False
    return is_same_tree(root, sub_root) \
        or is_subtree(root.left, sub_root) \
        or is_subtree(root.right, sub_root)


def lowest_common_ancestor(root: TreeNode, p: int, q: int) -> int:
    """
    Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.
    According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q
    as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”
    [MEDIUM] https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

    >>> lowest_common_ancestor(list_to_tree([6,2,8,0,4,7,9,None,None,3,5]), 2, 8)
    6
    >>> lowest_common_ancestor(list_to_tree([6,2,8,0,4,7,9,None,None,3,5]), 2, 4)
    2
    >>> lowest_common_ancestor(list_to_tree([2,1]), 2, 1)
    2
    """
    if p > q:
        p, q = q, p
    while True:
        if p > root.val:
            root = root.right
        elif q < root.val:
            root = root.left
        else:
            return root.val


def level_order(root: Optional[TreeNode]) -> List[List[int]]:
    """
    Given the root of a binary tree, return the level order traversal of its nodes' values.
    (i.e., from left to right, level by level).
    [MEDIUM] https://leetcode.com/problems/binary-tree-level-order-traversal/

    >>> level_order(list_to_tree([3,9,20,None,None,15,7]))
    [[3], [9, 20], [15, 7]]
    >>> level_order(list_to_tree([1]))
    [[1]]
    >>> level_order(list_to_tree([]))
    []
    """
    lis: List[List[int]] = []

    def add_vals(node: Optional[TreeNode], level: int) -> None:
        if node is None:
            return

        nonlocal lis
        if len(lis) < level + 1:
            lis.append([])
        lis[level].append(node.val)
        add_vals(node.left, level + 1)
        add_vals(node.right, level + 1)

    add_vals(root, 0)
    return lis


def level_order_no_recursion(root: Optional[TreeNode]) -> List[List[int]]:
    queue = deque([root] if root is not None else [])
    lis: List[List[int]] = []

    while len(queue) > 0:
        level = []

        # iterate over values for current level, don't touch newly added
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)

        lis.append(level)

    return lis


def right_side_view(root: Optional[TreeNode]) -> List[int]:
    """
    Given the root of a binary tree, imagine yourself standing on the right side of it, return the values
    of the nodes you can see ordered from top to bottom.
    [MEDIUM] https://leetcode.com/problems/binary-tree-right-side-view/

    >>> right_side_view(list_to_tree([1,2,3,None,5,None,4]))
    [1, 3, 4]
    >>> right_side_view(list_to_tree([1,None,3]))
    [1, 3]
    >>> right_side_view(list_to_tree([]))
    []
    """
    if root is None:
        return []
    cur_level = [root]
    right_side = []

    while len(cur_level) > 0:
        right_side.append(cur_level[-1].val)

        next_level = []
        for node in cur_level:
            if node.left is not None:
                next_level.append(node.left)
            if node.right is not None:
                next_level.append(node.right)
        cur_level = next_level

    return right_side


if __name__ == "__main__":
    import doctest

    doctest.testmod()
