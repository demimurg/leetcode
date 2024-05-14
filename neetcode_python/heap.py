from typing import *


class Heap:
    def __init__(self, is_max=True):
        self.storage = []
        # x before y, if x biggen than y for max_heap
        self.before = lambda x, y: x > y
        if not is_max:
            # x before y, if x less than y for min_heap
            self.before = lambda x, y: x < y

    def __len__(self):
        return len(self.storage)

    def add(self, val):
        self.storage.append(val)
        self.heapify_up()

    def get_top(self):
        if len(self.storage) == 0:
            return None
        return self.storage[0]

    def pop_top(self):
        if len(self.storage) == 0:
            return None
        if len(self.storage) == 1:
            return self.storage.pop()
        top = self.storage[0]
        self.storage[0] = self.storage.pop()
        self.heapify_down()

        return top

    # left = 2n+1, right = 2n+2
    def heapify_up(self):
        i = len(self.storage) - 1
        while i != 0:
            parent_i = (i - 1) // 2
            if not self.before(self.storage[i], self.storage[parent_i]):
                return
            self.storage[i], self.storage[parent_i] = self.storage[parent_i], self.storage[i]
            i = parent_i

    def heapify_down(self):
        i = 0
        while 2 * i + 1 < len(self.storage):
            child_i = 2 * i + 1  # left child
            if child_i + 1 < len(self.storage) and self.before(self.storage[child_i + 1], self.storage[child_i]):
                # right child
                child_i += 1
            if self.before(self.storage[i], self.storage[child_i]):
                return
            self.storage[i], self.storage[child_i] = self.storage[child_i], self.storage[i]
            i = child_i


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = Heap(is_max=False)
        for num in nums:
            self.heap.add(num)
        while len(self.heap) > k:
            self.heap.pop_top()

    def add(self, val: int) -> int:
        self.heap.add(val)
        if len(self.heap) > self.k:
            return self.heap.pop_top()
        return self.heap.get_top()
