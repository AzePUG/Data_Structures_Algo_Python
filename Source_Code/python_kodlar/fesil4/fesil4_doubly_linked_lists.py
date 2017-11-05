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
    def get_prev_node(self):
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

    def insert_at_end(self, data):
        new_node = Node(data, next_node=None, prev_node=None)

        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            current = self.head
            # Sonuncu node-u tapırıq
            while current.get_next_node() is not None:
                current = current.get_next_node()
            # Hal-hazırkı sonuncu node üçün next pointeri yeni node edirik.
            current.set_next_node(new_node)
            # Yeni node-un əvvəlki pointerini hal-hazırkı(while-da tapılan) node edirik.
            new_node.set_prev_node(current)
            # Yeni node-un next pointerini NULL-a yönləndiririk.
            new_node.set_next_node(None)
            self.tail = new_node

    def list_size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.get_next_node()
        return count

    def insert_at_pos(self, pos, data):
        if pos > self.list_size() or pos < 0:
            print("Pozisiya səhvdir, None qaytarıram..")
            return None
        else:
            # Əgər pozisiya 0 verilibsə və yaxud head node None-dırsa, əvvələ daxil et.
            if pos == 0 or self.head is None:
                print("Əvvələ daxil etmə...")
                self.insert_at_beginning(data)
            elif pos == self.list_size():
                print("Ən sona daxil etmə...")
                self.insert_at_end(data)
            elif pos > 0:
                print("Verilmiş pozisiyaya daxil etmə...")
                new_node = Node()
                new_node.set_data(data)

                count = 0
                current = self.head
                # Verilmiş pozisiyadan bir əvvəlki node-u tapırıq, yəni pozisional node-u
                while count < (pos - 1):
                    count += 1
                    current = current.get_next_node()
                # Yeni node-un next pointerini, pozisional node-dan növbəti node-a yönləndiririk.
                new_node.set_next_node(current.get_next_node())
                # Yeni node-un əvvəlki pointerini, hal-hazırkı node-a yönləndiririk.
                new_node.set_prev_node(current)
                # Pozisional node-dan(hal-hazırkı node) sonrakı node-un previous pointerini new_node-a yönləndiririk.
                current.get_next_node().set_prev_node(new_node)
                # Pozisional node-un next pointerini new_node-a yönləndiririk.
                current.set_next_node(new_node)

    def delete_first_node(self):
        if self.list_size() == 0:
            print("List boşdur...")
        else:
            # Müvəqqəti node
            temp = self.head
            # Head node-u əvvəlki head-dən sonrakı node-a mənimsədirik.
            # Bununla da faktiki olaraq, əvvəlki head-i arxada qoyuruq.
            self.head = self.head.get_next_node()
            # Yeni head və yaxud yeni node-umuzun sol(previous) node-a pointeri None edirik.
            self.head.set_prev_node(None)
            # Müvəqqəti node-u silirik.
            del(temp)
