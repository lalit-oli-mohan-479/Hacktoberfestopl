# python code of above approach
# Define the structure of a
# node in the linked list


class Node:
    def __init__(self, x):
        self.data = x
        self.next = None

# Function to return the
# reverse of a linked list


def reverseList(head):
    prev = None
    cur = head
    next_ = None

    while cur is not None:
        next_ = cur.next
        cur.next = prev
        prev = cur
        cur = next_
    return prev

# Function to return the sum of two
# linked lists


def addTwoLists(l1, l2):
    dummy = Node(0)
    cur = dummy
    carry = 0

    while l1 is not None or l2 is not None:
        x = l1.data if l1 else 0
        y = l2.data if l2 else 0
        summ = carry + x + y
        carry = summ // 10
        cur.next = Node(summ % 10)
        cur = cur.next
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next
    if carry > 0:
        cur.next = Node(carry)
    return dummy.next

# Function to print a linked list


def printList(head):
    while head is not None:
        print(head.data, end=" ")
        head = head.next
    print()

# Function to create a copy of
# a linked list


def copyList(head):
    cur = head
    dummy = Node(0)
    copy = dummy

    while cur is not None:
        copy.next = Node(cur.data)
        copy = copy.next
        cur = cur.next
    return dummy.next


# Driver Code
if __name__ == '__main__':

    # Example linked list:
    # 1 -> 2 -> 3 -> 4
    head1 = Node(1)
    head1.next = Node(2)
    head1.next.next = Node(3)
    head1.next.next.next = Node(4)

    # Printing original linked list
    print("Original linked list : ", end="")
    printList(head1)

    # Step1 - Make a copy of original
    # linked list
    newList = copyList(head1)

    # Step2 - Reverse a linked list
    head2 = reverseList(newList)

    # Printing reversed linked list
    print("Reversed linked list : ", end="")
    printList(head2)

    # Step3 - Addition of a original
    # linked list and its reverse
    addition = addTwoLists(head1, head2)

    # Step4 - Reverse a addition
    # Linked list
    result = reverseList(addition)

    # Step5 - Print the resultant
    # linked list
    print("Resultant linked list : ", end="")
    printList(result)
