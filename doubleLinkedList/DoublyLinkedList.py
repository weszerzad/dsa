class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self, value) -> None:
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        popped_node = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = popped_node.prev
            self.tail.next = None
            popped_node.prev = None
        self.length -= 1
        return popped_node

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True

    def popfirst(self):
        if self.length == 0:
            return None
        poppped_node = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = poppped_node.next
            poppped_node.next = None
            self.head.prev = None
        self.length -= 1
        return poppped_node

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        if index < self.length / 2:
            temp = self.head
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev
        return temp

    def set_value(self, index, value):
        got_node = self.get(index)
        if got_node is None:
            return False
        got_node.value = value
        return True

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        got_node = self.get(index)
        prev_node = got_node.prev
        prev_node.next = new_node
        new_node.prev = prev_node
        got_node.prev = new_node
        new_node.next = got_node
        self.length += 1
        return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.popfirst()
        if index == self.length - 1:
            return self.pop()
        got_node = self.get(index)
        got_node.prev.next = got_node.next
        got_node.next.prev = got_node.prev
        got_node.prev = None
        got_node.next = None
        self.length -= 1
        return got_node




my_doubly_linked_list = DoublyLinkedList(0)
my_doubly_linked_list.append(1)
my_doubly_linked_list.append(2)
print(my_doubly_linked_list.remove(1).value)
# my_doubly_linked_list.append(4)
# print(my_doubly_linked_list.pop().value)
# print(my_doubly_linked_list.pop().value)
# print(my_doubly_linked_list.pop())
# print(my_doubly_linked_list.popfirst().value)
# print(my_doubly_linked_list.popfirst().value)
# print(my_doubly_linked_list.popfirst())
# my_doubly_linked_list.prepend(0)
# my_doubly_linked_list.print_list()
# print(my_doubly_linked_list.get(1).value)
# print(my_doubly_linked_list.get(2).value)
# my_doubly_linked_list.set_value(1, 100)
# my_doubly_linked_list.insert(3, 2)
my_doubly_linked_list.print_list()