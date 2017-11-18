# Öz məxsusi exception-larımızı hazırlayırıq
class Error(Exception):
    pass


class StackOverFlow(Error):
    def __init__(self, message):
        self.message = message


class StackUnderFlow(Error):
    def __init__(self, message):
        self.message = message


class ArrayStack:

    def __init__(self, limit=10):
        self.stk = []
        self.limit = limit

    def is_empty(self):
        return len(self.stk) <= 0

    def push(self, item):
        if len(self.stk) >= self.limit:
            raise StackOverFlow("Stack overflow aşkarlandı!")
        else:
            self.stk.append(item)
            print("Stack after push -> {}".format(self.stk))

    def pop(self):
        if len(self.stk) <= 0:
            raise StackUnderFlow("Stack underflow aşkarlandı!")
        else:
            # Python list-də built-in olan pop() metodunu çağırırıq.
            return self.stk.pop()

    def peek(self):
        if len(self.stk) <= 0:
            raise StackUnderFlow("Stack underflow aşkarlandı!")
        else:
            # List slicing
            return self.stk[-1]

    def size(self):
        return len(self.stk)


# if __name__ == "__main__":
#     try:
#         our_stack = ArrayStack(limit=5)
#         our_stack.pop()
#
#     except (StackUnderFlow, StackOverFlow) as err:
#         print("{}: {}".format(err.__class__.__name__, err))
#     else:
#         print("Stack əməliyyatları uğurla yerinə yetirildi...")