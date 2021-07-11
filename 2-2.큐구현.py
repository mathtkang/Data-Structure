'''
Queue 클래스를 구현하세요.
'''


class Queue:
    '''
    List를 이용하여 다음의 method들을 작성하세요.
    '''

    def __init__(self):
        '''
        큐 myQueue을 만듭니다.
        '''
        self.myQueue = []

    def push(self, n):
        '''
        queue에  정수 n을 넣습니다.
        '''
        self.myQueue.append(n)

    def pop(self):
        '''
        queue에서 가장 앞에 있는 정수를 제거합니다. 만약 queue에 들어있는 값이 없을 경우에는 아무 일도 하지 않습니다. 
        '''
        if self.empty() == 1:
            return

        del self.myQueue[0]

    def size(self):
        '''
        queue에 들어 있는 정수의 개수를 return 합니다.
        '''
        return len(self.myQueue)

    def empty(self):
        '''
        queue이 비어있다면 1, 아니면 0을 return 합니다.
        '''
        if self.size() == 0:
            return 1
        else:
            return 0

    def front(self):
        '''
        queue의 가장 앞에 있는 정수를 return 합니다. 만약 queue에 들어있는 값이 없을 경우에는 -1을 return 합니다.
        '''
        if self.empty() == 1:
            return -1

        return self.myQueue[0]

    def back(self):
        '''
        queue의 가장 뒤에 있는 정수를 return 합니다. 만약 queue에 들어있는 값이 없을 경우에는 -1을 return 합니다.
        '''
        if self.empty() == 1:
            return -1

        return self.myQueue[-1]


# Queue 클래스 구현 ver.2
'''
class Queue:
    def __init__(self) :
        self.myQueue = []

    def push(self, n) :
        self.myQueue.append(n)

    def pop(self) :
        if len(self.myQueue) == 0:
            return -1
        else :
            result = self.myQueue[0]
            del self.myQueue[0]
            
    def size(self) : 
        return len(self.myQueue)

    def empty(self) :
        if len(self.myQueue) == 0:
            return 1
        else :
            return 0

    def front(self) :
        if len(self.Queue) == 0:
            return -1
        else:
            return self.myQueue[0]
        

    def back(self) :
        if len(self.myQueue) == 0:
            return -1
        else:
            return self.myQueue[len(self.myQueue)-1]
'''
