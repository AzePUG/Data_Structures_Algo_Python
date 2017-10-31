class Node:
    # Konstruktor
    # Əgər istifadəçi tərəfindən heçnə verilmirsə, bu zaman None(NULL) olaraq inisializasiya edirik
    def __init__(self, data=None, next_node=None, prev_node=None):
        self.data = data
        self.next_node = next_node
        self.prev_node = prev_node

    # node-un data field-ini mənimsətmək  üçün metod
    def set_data(self, data):
        self.data = data

    # node-un data field-ini almaq üçün metod
    def get_data(self):
        return self.data

    # node-un növbəti(next) field-ini mənimsətmək üçün metod
    def set_next_node(self, next_node):
        self.next_node = next_node

    # node-un növbəti(next) field-ini almaq üçün metod
    def get_next_node(self):
        return self.next_node

    # əgər bir node sonrakına point edirsə, True qaytar
    def has_next(self):
        return self.next_node is not None

    # node-un əvvəlki(previous) field-ini mənimsətmək üçün metod
    def set_prev_node(self, prev_node):
        self.prev_node = prev_node

    # node-un əvvəlki(previous) field-ini almaq üçün metod
    def get_prev_node(self, prev_node):
        return self.prev_node

    # node-dan əvvəlki varsa, True
    def has_prev(self):
        return self.prev_node is not None

class DoublyLinkedList:

    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def insert_at_beginning(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.set_prev_node(None)
            new_node.set_next_node(self.head)
            self.head.set_prev_node(new_node)
            self.head = new_node
