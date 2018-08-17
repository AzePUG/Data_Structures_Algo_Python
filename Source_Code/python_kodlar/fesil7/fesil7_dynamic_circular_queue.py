class DynamicCircularQueue:

    def __init__(self, limit=5):
        self.que = []
        self.limit = limit
        self.front = -1 # Ön
        self.rear = -1  # Arxa, son

    def is_full(self):
        if self.front == 0 and self.rear == (self.limit - 1):
            return True
        elif self.front == self.rear + 1:
            return True
        return False

    def is_empty(self):
        return self.front == -1

    def en_queue(self, data):
        if self.is_full():
            print("Növbə doludur, ikiqat artırıram...")
            self.limit = self.limit * 2
        else:
            if self.front == -1:
                self.front = 0
            # REAR-i artırırıq, irəli çəkirik.
            self.rear = (self.rear + 1) % self.limit
            self.que.append(data)
            print("EnQueue-dən sonra, növbə, ", self.que)
        print("FRONT -> ", self.front)
        print("REAR -> ", self.rear)

    def de_queue(self):
        if self.is_empty():
            print("Növbə boşdur...")
        else:
            # Python list element silindikdən sonra, listi özü yenidən indexlədiyi üçün.
            # Həmişə pop(0) olaraq çağırmaq lazımdır. pop(self.front) düzgün nəticə vermir.
            data = self.que.pop(0)
            # Əgər bərabərdilərsə o zaman cəmi 1 elementi var, bu səbəbdən sildikdən sonra resetləyirik.
            if self.front == self.rear:
                self.front = -1
                self.rear = -1
            else:
                # FRONT-u artırırıq, irəli çəkirik.
                self.front = (self.front + 1) % self.limit

            print("Silinən element - ", data)
            print("FRONT -> ", self.front)
            print("REAR -> ", self.rear)

    def size(self):
        return len(self.que)


if __name__ == "__main__":
    obj = DynamicCircularQueue(limit=5)
    obj.en_queue(56)
    obj.en_queue(44)
    obj.en_queue(85)
    obj.en_queue(66)
    obj.en_queue(99)
    obj.en_queue(111)
    obj.en_queue(222)

