class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def IS_LOOP_OR_NOT(head):
    slow = head
    fast = head.next

    if slow and fast and fast.next is not None:
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                print("Given list is circular")
                return
        print("Given list is not in circular")

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = head

IS_LOOP_OR_NOT(head)
