#!/usr/bin/python

class Node:
    def __init__(self, val, node):
        self.data = val
        self.next = node

class LinkedList:
    def __init__(self, head):
        self.head = head

    def insert(self, data):
        new_node = Node(data, self.head)
        # print "New node data: " + str(new_node.data)
        # print "New node next data: " + str(new_node.next.data)
        # new_node.next = self.head
        self.head = new_node
        # print "Head node data: " + str(self.head.data)
        # print "Head node next data: " + str(self.head.next.data)
        # if self.head.next.next:
        #     print "Head node next next data: " + str(self.head.next.next.data)
        #     print "Head node next next ref: " + str(self.head.next.next.next)

    def printList(self):
        cur_node = self.head
        # print "Printing the list ..."
        llist = list()
        while cur_node.next != None:
            llist.append(str(cur_node.data))
            cur_node = cur_node.next
        llist.append(str(cur_node.data))
        print ",".join(llist)

head = Node(1, None)
llist = LinkedList(head)
llist.printList()
llist.insert(2)
llist.printList()
llist.insert(3)
llist.printList()
