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


class LinkedListQueue:
    def __init__(self, head=None):
        self.front = None
        self.rear = None
        self.head = head

    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.get_next_node()
        return count

    def en_queue(self, data):
        # Listin sonuna node daxil edirik
        print("Növbəyə daxil edirik...")
        new_node = Node()
        new_node.set_data(data)
        if self.size() == 0:
            self.head = new_node
            # List-də heç bir element olmadığı üçün front və rear eyni yerdədirlər.
            self.front = self.head
            self.rear = self.front
        else:
            current = self.head
            while current.get_next_node() is not None:
                current = current.get_next_node()

            current.set_next_node(new_node)
            # Rear-i burda sonuncu node edirik
            self.rear = current.get_next_node()

    def de_queue(self):
        # Listin əvvəlindən node silirik
        if self.size() == 0:
            print("Növbə boşdur...")
        else:
            print("Növbədən çıxardırıq...")
            # Müvəqqəti node
            temp = self.head
            # Head node-u əvvəlki head-dən sonrakı node-a mənimsədirik.
            # Bununla da faktiki olaraq, əvvəlki head-i arxada qoyuruq.
            self.head = self.head.get_next_node()
            # Həmçinin front-u da yeni head-ə bərabər edirik, faktiki olaraq irəli sürüşdürürük.
            self.front = self.head
            # Müvəqqəti node-u silirik.
            del(temp)

    def queue_rear(self):
        if self.rear is None:
            print("Növbə boşdur...")
        else:
            return self.rear.get_data()

    def queue_front(self):
        if self.front is None:
            print("Növbə boşdur...")
        else:
            return self.front.get_data()


if __name__ == "__main__":
    obj = LinkedListQueue()
    obj.en_queue(56)
    obj.en_queue(44)
    obj.en_queue(85)
    obj.en_queue(66)
    print("Növbənin uzunluğu: ", obj.size())
    obj.en_queue(99)
    obj.en_queue(111)
    obj.de_queue()
    obj.de_queue()
    obj.en_queue(222)
    print("Növbənin uzunluğu: ", obj.size())
    print("Növbənin ilk elementi: ", obj.queue_front())
    print("Növbənin son elementi: ", obj.queue_rear())