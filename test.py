def test(fn, *args):
    print("Input:", args)
    result = fn(*args)
    print("Output:", args, "return:", result)
    print()


def createTest(fn):
    def test(*args):
        print("Input:", args)
        result = fn(*args)
        print("Output:", args, "return:", result)
        print()
    return test


def createAssert(fn):
    def test(expect, *args):
        result = fn(*args)
        if expect != result:
            print(f'{fn.__name__}{args} expect {expect} but result {result}')
    return test

import time
def benchmark(fn, *args):
    start_time = time.time()
    fn(*args)
    end_time = time.time()
    run_time = end_time - start_time 
    print(f"time elapsed: {run_time:.4f} seconds")


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        result = []
        current = self
        while current is not None:
            result.append(str(current.val))
            current = current.next
        return "[ " + " -> ".join(result) + " ]"
    
    def __repr__(self) -> str:
        return str(self)

def CreateLinkedList(array):
    if not array:
        return None
    
    head = ListNode(array[0])
    current = head
    for i in range(1, len(array)):
        current.next = ListNode(array[i])
        current = current.next

    return head

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self) -> str:
        
        result = []

        queue = deque()
        queue.append(self)

        while queue:
            node = queue.popleft()
            
            if node:
                result.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append("null")


        # 去掉多余的null
        while result[-1] == "null":
            result.pop()


        return "[" + ",".join(result) + "]" 
    
    def __repr__(self) -> str:
        return str(self)



def CreateTreeNode(level_order):

    if not level_order:
        return None
    root = TreeNode(level_order[0])
    queue = [root]
    i = 1
    while i < len(level_order):
        node = queue.pop(0)
        if level_order[i] is not None:
            node.left = TreeNode(level_order[i])
            queue.append(node.left)
        i += 1
        if i < len(level_order) and level_order[i] is not None:
            node.right = TreeNode(level_order[i])
            queue.append(node.right)
        i += 1
    return root
    

def asc_array(num):
    array = []
    for i in range(num):
        array.append(i)
    return array


def sam_array(num, ele):
    array = []
    for i in range(num):
        array.append(ele)
    return array