# Design a Queue(enqueue, dequeue, isEmpty) using 2 stacks (push, pop, top, isEmpty)
# In python a list can be used as a stack, but we will implment a class to have it more clear

# this structure is given
class Stack:
    def __init__(self):
        self._internal = list()

    def top(self):
        if not self._internal:
            raise Exception("Stack is Empty!")
        return self._internal[-1]

    def push(self, elem):
        self._internal.append(elem)

    def pop(self):
        return self._internal.pop()

    def isEmpty(self):
        return len(self._internal) == 0

    def __len__(self):
        return len(self._internal)

    def size(self):
        return len(self)


class Queue:
    def __init__(self):
        self.inStack = Stack()
        self.outStack = Stack()

    def size(self):
        return self.inStack.size() + self.outStack.size()

    def enqueue(self, elem):
        self.inStack.push(elem)

    def isEmpty(self):
        return self.inStack.isEmpty() and self.outStack.isEmpty()

    def dequeue(self):
        if self.isEmpty():
            raise Exception("Queue is empty!")
        if self.outStack.isEmpty():
            while not self.inStack.isEmpty():
                self.outStack.push(self.inStack.pop())
        return self.outStack.pop()




# How would you design a LRU cache (least recently used cache).
# put(key, value), get(key), delete(), get_most_recently_used(), all in constant time
# (linked hash)

class LinkedList:
    class Node:
        def __init__(self, val, key=None):
            self.key = key
            self.val = val
            self.next = None
            self.prev = None

    def __init__(self):
        self.head = None
        self.tail = None

    def addToHead(self, val, key=None):
        new = self.Node(val, key)
        new.next = self.head
        self.head.prev = new
        head = new

    def moveToHead(self, node):
        if node is not self.head:
            tmp = node
            node.prev.next = node.next
            node.next.prev = node.prev
            tmp.next = self.head
            self.head.prev = tmp
            self.head = tmp

    def deleteLast(self):
        deleted = self.tail.val
        self.tail = self.tail.prev
        self.tail.next = None

    def delete(self, node):
        if node is self.tail:
            self.deleteLast()
        elif node is self.head:
            self.head = self.head.next
        else:
            node.prev.next = node.next


class LRUCahce:
    def __init__(self):
        self.vals = LinkedList()
        self.cache = dict()

    def put(self, key, val):
        if key in self.cache:
            node = self.cache[key]
            node.val = val
            self.vals.moveToHead(node)
        else:
            self.vals.addToHead(val, key)
            self.cache[key] = self.vals.head

    def get(self, key):
        try:
            self.vals.moveToHead(self.cache[key])
            return self.vals.head.val
        except KeyError:
            raise KeyError(str(key) + " value not in cache")

    def delete_last(self):
        k = self.vals.tail.key
        del self.cache[k]
        self.vals.deleteLast()

    def delete(self, key):
        try:
            node = self.cache[key]
            v = node.val
            self.vals.delete(node)
            return v
        except KeyError:
            raise KeyError(str(key) + " value not in cache")

    def get_last_recently_used_entry(self):
        return self.vals.head.key, self.vals.head.val


