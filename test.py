def test(fn, *args):
    print("Input:", args)
    result = fn(*args)
    print("Output:", args, "return:", result)
    print()

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

def LinkedList(array):
    if not array:
        return None
    
    head = ListNode(array[0])
    current = head
    for i in range(1, len(array)):
        current.next = ListNode(array[i])
        current = current.next

    return head


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