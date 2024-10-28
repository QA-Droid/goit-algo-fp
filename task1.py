class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        print(elements)

def reverse_linked_list(linked_list):
    prev = None
    current = linked_list.head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    linked_list.head = prev

def merge_sort_linked_list(head):
    if not head or not head.next:
        return head

    mid = get_middle(head)
    left = head
    right = mid.next
    mid.next = None

    left = merge_sort_linked_list(left)
    right = merge_sort_linked_list(right)

    return merge(left, right)

def get_middle(head):
    slow = head
    fast = head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

def merge(left, right):
    dummy = Node(0)
    tail = dummy

    while left and right:
        if left.data < right.data:
            tail.next = left
            left = left.next
        else:
            tail.next = right
            right = right.next
        tail = tail.next

    tail.next = left or right
    return dummy.next

def merge_two_sorted_lists(list1, list2):
    dummy = Node(0)
    tail = dummy

    current1 = list1.head
    current2 = list2.head

    while current1 and current2:
        if current1.data < current2.data:
            tail.next = current1
            current1 = current1.next
        else:
            tail.next = current2
            current2 = current2.next
        tail = tail.next

    tail.next = current1 or current2
    merged_list = LinkedList()
    merged_list.head = dummy.next
    return merged_list

list1 = LinkedList()
list1.append(1)
list1.append(3)
list1.append(5)

list2 = LinkedList()
list2.append(2)
list2.append(4)
list2.append(6)

print("Список 1:")
list1.display()
print("Список 2:")
list2.display()

reverse_linked_list(list1)
print("Реверсований список 1:")
list1.display()

list2.head = merge_sort_linked_list(list2.head)
print("Відсортований список 2:")
list2.display()

merged_list = merge_two_sorted_lists(list1, list2)
print("Об'єднаний список:")
merged_list.display()