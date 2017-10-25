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
    def set_next(self, next_node):
        self.next_node = next_node

    # node-un növbəti fiel-ini almaq üçün metod
    def get_next_node(self):
        return self.next_node

    # əgər bir node sonrakına point edirsə, true qaytar
    def has_next(self):
        return self.next_node is not None


class SinglyLinkedList:
    # Birtərəfli bağlı list
    def __init__(self, head=None):
        self.head = head

    def list_size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.get_next_node()
        return count

    def insert_at_beginning(self, data):
        new_node = Node()
        new_node.set_data(data)

        if self.list_size() == 0:
            self.head = new_node
        else:
            new_node.set_next(self.head)
            self.head = new_node
