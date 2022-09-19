#stack - linear data structure, O(1), LIFO(last in first out), push,pop, 

class Stack(object):

    # constructor
    def __init__(self) -> None:
        self.stack = []
        self.index = 0

    # checking if stack is empty
    def isEmpty(self):
        return self.stack == []

    # pushing element to stack
    def push(self, data):
        self.stack.insert(self.index, data)
        self.index += 1
        return f'{data} pushed to stack'

    # removing element from stack
    def pop(self):
        self.index = -1
        data = self.stack.pop(self.index)
        return '{} popped from stack'.format(data)

    # checking stack size
    def stackSize(self):
        return len(self.stack)


if __name__ == '__main__':
    s = Stack()
    print(s.isEmpty())
    print(s.push(23))
    print(s.stackSize())
    print(s.push(3))
    print(s.stackSize())
    print(s.push(123))
    print(s.stackSize())
    print(s.push(22223))
    print(s.stackSize())
    print(s.pop())
    print(s.stackSize())
    print(s.pop())
    print(s.stackSize())
    print(s.push(23))
    print(s.stackSize())
