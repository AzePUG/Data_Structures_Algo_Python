class Node:
    # konstruktor
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    # node-un data field-ini mənimsətmək  üçün metod
    def set_data(self, data):
        self.data = data

    # node-un data field-ini almaq üçün metod
    def get_data(self):
        return self.data

    # node-un növbəti field-ini mənimsətmək üçün metod
    def set_next_node(self, next_node):
        self.next_node = next_node

    # node-un növbəti field-ini almaq üçün metod
    def get_next_node(self):
        return self.next_node

    # əgər bir node sonrakına point edirsə, true qaytar
    def has_next(self):
        return self.next_node is not None


class LinkedListStack:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def push(self, data):
        temp = Node()
        temp.set_data(data=data)
        temp.set_next_node(self.head)
        self.head = temp

    def pop(self):
        if self.head is None:
            raise IndexError("Yığın boşdur...")
        temp = self.head.get_data()
        self.head = self.head.get_next_node()
        return temp

    def peek(self):
        if self.head is None:
            raise IndexError("Yığın boşdur...")
        return self.head.get_data()

    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.get_next_node()
        return count

    def delete_stack(self):
        self.head = None

