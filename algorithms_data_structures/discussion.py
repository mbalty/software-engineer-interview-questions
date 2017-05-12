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

    def __str__(self):
        return str(self._internal)


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

    def __str__(self):
        return str(self.inStack)[:-1] + ', ' + str(self.outStack)[1:]


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

        def __repr__(self):
            return str((self.val, self.key))

    def __init__(self):
        self.head = None
        self.tail = None

    def addToHead(self, val, key=None):
        new = self.Node(val, key)
        new.next = self.head
        if self.head:
            self.head.prev = new
        else:
            self.tail = new
        self.head = new

    def moveToHead(self, node):
        if node is not self.head:
            tmp = node
            self.delete(node)
            tmp.next = self.head
            tmp.prev = None
            self.head = tmp

    def deleteLast(self):
        if self.tail:
            deleted = self.tail.val
            self.tail = self.tail.prev
            if not self.tail:
                self.head = None
            else:
                self.tail.next = None
            return deleted
        else:
            return None

    def delete(self, node):
        if node is self.tail:
            self.deleteLast()
        elif node is self.head:
            self.head = self.head.next
            if not self.head:
                self.tail = None
            else:
                self.head.prev = None
        elif node.prev and node.next:
            node.prev.next = node.next
            node.next.prev = node.prev
        else:
            raise Exception("node to delete not in list")

    def __str__(self):
        n = self.head
        s = []
        while n:
            s.append(str((n.key, n.val)))
            s.append(' -> ')
            n = n.next
        return ''.join(s[:-1])

    def empty(self):
        return self.head is None


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
        if self.empty():
            return None
        k = self.vals.tail.key
        v = self.vals.tail.val
        self.vals.deleteLast()
        del self.cache[k]
        return k, v


    def delete(self, key):
        try:
            node = self.cache[key]
            v = node.val
            self.vals.delete(node)
            return v
        except KeyError:
            raise KeyError(str(key) + " value not in cache")

    def get_last_recently_used_entry(self):
        if self.empty():
            return None
        return self.vals.head.key, self.vals.head.val

    def empty(self):
        return self.vals.empty()

    def __str__(self):
        return "Dict:\nn" + str(self.cache) + '\nOrder:\n' + str(self.vals)

def testQueue():
    print ("***test Queue")
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)

    print ("enqueued 1,2,3: ", q)
    print (
        "dequeued " + str(q.dequeue()) + ": ", q
    )


def testLRUCache():
    print("***test LRU cache")
    l = LRUCahce()
    l.put('a', 1)
    print (l.delete_last())
    l.put('b', 1)
    l.put('c', 1)
    print (l.get_last_recently_used_entry())
    print (l)


if __name__ == "__main__":
    testQueue()
    testLRUCache()