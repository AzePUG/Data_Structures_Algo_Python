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
                    current = current.get_next_node()
                    count += 1
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

    def delete_last_node(self):
        if self.list_size() == 0:
            print("List boşdur...")
        else:
            # Head node-dan başlayırıq
            current_node = self.head
            # Sonuncu  node-u aşkarlayırıq
            while current_node.get_next_node() is not None:
                current_node = current_node.get_next_node()
            # Sonuncu node-dan bir əvvəlki node-u tapırıq
            previous_node = current_node.get_prev_node()
            # Bir əvvəlki node-un növbəti
            previous_node.set_next_node(None)
            # current node-u silirik
            del(current_node)

    def traverse_and_print(self):
        if self.list_size() == 0:
            print("List boşdur...")
        elif self.list_size() == 1:
            print(self.head.data)
        else:
            # Head node-dan başlayırıq
            current_node = self.head
            print(current_node.get_data())
            while True:
                current_node = current_node.get_next_node()
                if current_node is None:
                    break
                print(current_node.get_data())

    def delete_from_list_by_data(self, data):
        # Burada, current, tapılan node-u, data-ya əsasən silirik.
        current_node = self.head
        found = False

        # current_node None olsa dayan, found True olsa dayan
        while current_node and found is False:
            if current_node.get_data() == data:
                found = True
            else:
                current_node = current_node.get_next_node()

        if current_node is None:
            # Fərqlilik məqsədilə Exception-dan istifadə edirik
            raise ValueError("Data listdə tapılmadı...")
        if current_node.get_prev_node() is None:
            # Bu o deməkdir ki, axtarılan data elə 1ci(head) node-da tapılıb.
            # Bu zaman head-i sadəcə növbəti node-a işarəliyirik.
            # Əslində bu hal, list-in əvvəlindən node silməyə bərabərdir.
            self.head = current_node.get_next_node()
        else:
            # Əvvəlki node-un next pointerini, hal-hazırkı(current) node-un next node-una yönləndiririk.
            current_previous_node = current_node.get_prev_node()
            current_previous_node.set_next_node(current_node.get_next_node())
            # Sonrakı node-un əvvəlki pointerini isə hal-hazırkı(current) node-un əvvəlki node-una yönləndiririk.
            current_next_node = current_node.get_next_node()
            current_next_node.set_prev_node(current_node.get_prev_node())

    def delete_at_position(self, pos):
        count = 0
        current_node = self.head

        if pos > self.list_size() or pos < 0:
            print("Pozisiya səhvdir, None qaytarıram..")
            return None
        elif pos == 0:
            # Bu o deməkdir ki, listin əvvəlindən node silirik.
            self.delete_first_node()
        elif pos == self.list_size():
            # Bu o deməkdir ki, listin sonundan node silirik.
            self.delete_last_node()
        else:
            # Əgər listin axırına çatmamışıqsa və count verilmiş pozisiyadan kiçikdirsə, davam elə
            while (current_node.get_next_node() is not None) or count < pos:
                    count = count + 1
                    if count == pos:
                        # Əgər verilmiş pozisiyaya çatdıqsa, əvvəlki node-un next pointer-ini, indiki node-un next pointerinə yönləndiririk.
                        current_previous_node = current_node.get_prev_node()
                        current_previous_node.set_next_node(current_node.get_next_node())

                        # Sonrakı node-un əvvəlki pointerini isə hal-hazırkı(current) node-un əvvəlki node-una yönləndiririk.
                        current_next_node = current_node.get_next_node()
                        current_next_node.set_prev_node(current_node.get_prev_node())
                        return
                    else:
                        # Əgər hələ pozisiyaya çatmamışıqsa, o zaman davam edirik.
                        current_node = current_node.get_next_node()
