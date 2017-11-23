# Digər moduldan class-larımızı import edirik
from fesil6_list_stack import StackUnderFlow


class DynamicStack:
    def __init__(self, limit=10):
        self.stk = []
        self.limit = limit

    def is_empty(self):
        # Əgər python listin boşdursa, deməli stack boşdur bu zaman True qaytarırıq.
        return self.stk == []

    def push(self, item):
        if len(self.stk) >= self.limit:
            self.resize()
        self.stk.append(item)
        print("Stack after push -> {}".format(self.stk))

    def pop(self):
        if len(self.stk) == 0:
            raise StackUnderFlow("Stack underflow aşkarlandı!")
        else:
            # Python list-də built-in olan pop() metodunu çağırırıq.
            return self.stk.pop()

    def peek(self):
        if len(self.stk) == 0:
            raise StackUnderFlow("Stack underflow aşkarlandı!")
        else:
            # List slicing
            return self.stk[-1]

    def size(self):
        return len(self.stk)

    def delete_stack(self):
        # Stack-i silmək, faktiki olaraq python listi sıfırlamaqla əldə oluna bilər.
        self.stk = []

    def resize(self):
        # Python üçün resize əməliyyatı əslində, sadəcə limit-i 2-qat artırmaq deməkdir.
        # Belə ki, yeni array(list) yaradıb köhnəni ora kopyalamağa ehtiyac yoxdur, çünki onsuz da listin hər hansı limiti yoxdur.
        print("Resizing array...")
        self.limit = 2 * self.limit