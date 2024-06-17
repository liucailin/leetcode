def test(fn, *args):
    print("Input:", args)
    result = fn(*args)
    print("Output:", args, "return:", result)
    print()


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