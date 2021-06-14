#!/bin/python3

import math
import os
import random
import re
import sys

class DoublyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = DoublyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail


        self.tail = node

def print_doubly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

#
# Complete the 'sortedInsert' function below.
#
# The function is expected to return an INTEGER_DOUBLY_LINKED_LIST.
# The function accepts following parameters:
#  1. INTEGER_DOUBLY_LINKED_LIST llist
#  2. INTEGER data
#

#
# For your reference:
#
# DoublyLinkedListNode:
#     int data
#     DoublyLinkedListNode next
#     DoublyLinkedListNode prev
#
#


class DoubleNode:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.prev = prev
        self.next = next
        self.size = 0
        

def size(head):
    current = head
    count = 0
    
    while current:
        count+=1
        current = current.next
    return count
    
def sortedInsert(head, data):
    newNode = DoubleNode(data, None, None)
    if size(head) == 0:
        return DoubleNode(data, None, None)
    else:
        if newNode.data <= head.data:
            newNode.next = head
            head.prev = newNode
            head = newNode
        else:
            curr = head      
            while curr.next and curr.next.data <= newNode.data:
                curr = curr.next
            
            if curr.next == None:
                curr.next = newNode
                newNode.prev = curr
            else:
                newNode.next = curr.next
                newNode.prev = curr
                curr.next.prev = newNode
                curr.next = newNode
        
               
    
    return head