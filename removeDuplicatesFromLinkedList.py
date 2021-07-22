# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(linkedList):
    temp = linkedList
    while temp.next is not None:
        temp2 = temp.next
        if temp.value == temp2.value:
            temp.next = temp2.next
            del temp2
        else:
            temp = temp.next
        if temp.next is None:
            break

    return linkedList


linkedlist = LinkedList(1)
linkedlist1 = LinkedList(1)
linkedlist.next = linkedlist1
linkedlist2 = LinkedList(3)
linkedlist1.next = linkedlist2
linkedlist3 = LinkedList(4)
linkedlist2.next = linkedlist3
linkedlist4 = LinkedList(4)
linkedlist3.next = linkedlist4
linkedlist5 = LinkedList(4)
linkedlist4.next = linkedlist5
linkedlist6 = LinkedList(5)
linkedlist5.next = linkedlist6
linkedlist7 = LinkedList(6)
linkedlist6.next = linkedlist7
linkedlist8 = LinkedList(6)
linkedlist7.next = linkedlist8
removeDuplicatesFromLinkedList(linkedlist)
print("done")
