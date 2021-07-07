# STACK클래스 생성
class Stack:
    def __init__(self):
        self.myStack = []

    def push(self, n):
        self.myStack.append(n)

    def pop(self):
        if self.empty() == 1:
            return
        else:
            self.myStack.pop()

    def size(self):
        return len(self.myStack)

    def empty(self):
        if self.size() == 0:
            return 1
        else:
            return 0

    def top(self):
        if self.empty() == 1:
            return -1
        else:
            return self.myStack[-1]


def checkParen(p):  # 괄호 문자열 p의 쌍이 맞으면 "YES", 아니면  "NO"를 반환
    s = Stack()
    for c in p:
        if c == '(':
            s.push(c)
        else:
            if s.empty() == 1:
                return "NO"
            s.pop()

    if s.empty() == 1:
        return "YES"
    else:
        return "NO"

    return "NO"
