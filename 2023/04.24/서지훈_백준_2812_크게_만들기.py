class Stack:
    def __init__(self):
        self.stack = []
        self.size = 0

    def push(self, num):
        self.stack.append(num)
        self.size += 1

    def pop(self):
        if self.size == 0:
            print("Pop Error - empty stack!")
        else:
            val = self.stack[self.size-1]
            self.stack.pop(self.size-1)
            self.size -= 1
            return val

    def peek(self):
        if self.size == 0:
            print("Peek Error - empty stack!")
        else:
            return self.stack[self.size-1]

    def size(self):
        return self.size

    def is_empty(self):
        if self.size == 0:
            return True
        return False

    def print_stack(self, n, k):
        for i in range(n - k):
            print(self.stack[i], end='')


N, K = map(int, input().split())
k = K
number = input()

stack = Stack()  # 파이썬은 스택 미존재, 별도 구현

for n in number:  # 숫자 순회
    if stack.is_empty():
        stack.push(n)

    elif not stack.is_empty() and int(stack.peek()) >= int(n):
        stack.push(n)

    else:
        while not stack.is_empty() and K > 0 and int(stack.peek()) < int(n):
            stack.pop()
            K -= 1
        stack.push(n)

stack.print_stack(N, k)