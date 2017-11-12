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


class CircularLinkedList:
    def __init__(self, head=None):
        self.head = head

    def circular_list_length(self):
        current_node = self.head
        if current_node is None:
            return 0

        count = 1
        current_node = current_node.get_next_node()
        # Dövri əlaqəli listdə yenidən head node-a gedib çıxmışıq ya yox, onu yoxlayırıq.
        while current_node != self.head:
            current_node = current_node.get_next_node()
            count = count + 1

        return count

    def print_data_circular_list(self):
        current_node = self.head
        if current_node is None:
            return 0

        current_node = current_node.get_next_node()
        print(current_node.get_data())
        while current_node != self.head:
            current_node = current_node.get_next_node()
            print(current_node.get_data())

    def insert_at_end(self, data):
        current_node = self.head
        new_node = Node()
        new_node.set_data(data)

        if self.head is None:
            self.head = new_node
            new_node.set_next_node(self.head)
        else:
            current_node = current_node.get_next_node()
            while current_node.get_next_node() != self.head:
                current_node.get_next_node()
            # Yeni node-u öz-özünə point edirik.
            new_node.set_next_node(new_node)
            # Yeni node-u head node-a yönləndiririk.
            new_node.set_next_node(self.head)
            # Hal-hazırkı(faktiki olaraq əvvəlki) node-u isə yeni node-a yönləndiririk.
            current_node.set_next_node(new_node)

    def insert_at_beginning(self, data):
        current_node = self.head
        new_node = Node()
        new_node.set_data(data)
        # Yeni node-u öz-özünə point edirik.
        new_node.set_next_node(new_node)

        if self.head is None:
            self.head = new_node
            new_node.set_next_node(self.head)
        else:
            current_node.get_next_node()
            while current_node.get_next_node() != self.head:
                current_node = current_node.get_next_node()
            # Yeni node-u head node-a yönləndiririk.
            new_node.set_next_node(self.head)
            # Yeni node-u yeni head edirik
            self.head = new_node
            # Hal-hazırkı tapılan node-u isə yeni head-ə yönləndiririk və yaxud yeni head-ə
            # current_node.set_next_node(new_node)
            current_node.set_next_node(self.head)


if __name__ == '__main__':
    obj = CircularLinkedList()
    obj.insert_at_end(44)
    obj.insert_at_end(3)
    obj.insert_at_end(99)
    obj.insert_at_beginning(101)
    obj.insert_at_beginning(6)
    print("Printing list length -> {}".format(obj.circular_list_length()))
    obj.print_data_circular_list()
