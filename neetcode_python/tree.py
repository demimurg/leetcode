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
    return 1 + max(max_depth(root.left), max_depth(root.right)) if root else None


if __name__ == "__main__":
    import doctest

    doctest.testmod()
