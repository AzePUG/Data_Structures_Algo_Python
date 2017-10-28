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
            new_node.set_next_node(self.head)
            self.head = new_node

    def insert_at_end(self, data):
        new_node = Node()
        new_node.set_data(data)

        current = self.head
        while current.get_next_node() is not None:
            current = current.get_next_node()

        current.set_next_node(new_node)

    def insert_at_pos(self, pos, data):
        # Əgər düzgün pozisiya verilmirsə, None qaytar
        if pos > self.list_size() or pos < 0:
            print("Pozisiya səhvdir, None qaytarıram..")
            return None
        else:
            # Əgər pozisiya 0-dırsa, bu o deməkdir ki, biz listin əvvəlinə daxil etmək istəyirik
            if pos == 0:
                print("Əvvələ daxil etmə...")
                self.insert_at_beginning(data)
            # Əgər pozisiya list-in node sayına bərabərdirsə, bu o deməkdir ki, node-u listin sonuna daxil etmək lazımdır
            elif pos == self.list_size():
                print("Ən sona daxil etmə...")
                self.insert_at_end(data)
            else:
                print("Verilmiş pozisiyaya daxil etmə...")
                new_node = Node()
                new_node.set_data(data)
                count = 1
                current = self.head
                # Verilmiş pozisiyadan bir əvvəlki node-u tapırıq
                while count < (pos - 1):
                    count += 1
                    current = current.get_next_node()
                # Yeni node-un next pointerini, verilmiş pozisiyadan bir əvvəlki node-un point etdiyi node-a yönləndiririk.
                new_node.set_next_node(current.get_next_node())
                # Verilmiş pozisiyadan bir əvvəlki node-un next pointer-ini isə bizim daxil etmək istədiyimiz node-a yönləndiririk.
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
            # Müvəqqəti node-u silirik.
            del(temp)

    def delete_last_node(self):
        if self.list_size() == 0:
            print("List boşdur...")
        else:
            # Yuxarıda dediyimiz kimi 2 node haqqında məlumatı saxlamalıyıq
            current_node = self.head
            previous_node = self.head

            while current_node.get_next_node() is not None:
                previous_node = current_node
                current_node = current_node.get_next_node()

            previous_node.set_next_node(None)            
