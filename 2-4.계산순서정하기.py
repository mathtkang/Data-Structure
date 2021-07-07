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


def find_order(p):
    '''
    괄호 p가 주어질 때, 각 괄호가 몇 번째로 계산되어야 하는 괄호인지를 list로 반환합니다.

    예를 들어, p='(()())' 일 경우, [3, 1, 1, 2, 2, 3] 을 반환합니다.
    '''
    s = Stack()

    result = [0] * len(p)

    cnt = 1

    for i in range(len(p)):
        if p[i] == "(":
            s.push(i)
        else:
            index = s.top()
            s.pop()

            result[index] = cnt
            result[i] = cnt

            cnt += 1

    return result
