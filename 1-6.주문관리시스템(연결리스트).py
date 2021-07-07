'''
1. LinkedListElement 클래스를 완성하세요.
2. orderManager 클래스를 완성하세요.
'''


class LinkedListElement:
    def __init__(self, data, myPrev, myNext):  # 정점이 2개인 것을 2중 연결리스트 라 한다
        self.data = data
        self.myPrev = myPrev
        self.myNext = myNext


class orderManager:
    def __init__(self):
        self.start = None
        self.end = None

    def addOrder(self, orderId):
        o = LinkedListElement(orderId, None, None)

        if self.start == None and self.end == None:
            self.start = o
            self.end = o
        else:
            # 그렇지 않다면 맨 마지막에 o를 넣어줘야 하는거니까
            self.end.myNext = o
            o.myPrev = self.end  # ??

            self.end = o

    def removeOrder(self, orderId):

        if self.start == None and self.end == None:
            return

        # 현재 위치
        current = self.start
        # 맨 처음 노드부터 하나씩 다음노드를 따라가면서
        # orderId와 current를 비교해주고 일치하면 제거해주면 됨

        # prevElem    current    nextElem
        #   []          []          []
        while current != None:
            if current.data == orderId:
                prevElem = current.myPrev
                nextElem = current.myNext

                # 현 위치를 기준으로 이전노드와 다음노드를 연결해주면 가운데노드를 삭제해준 것과 동일한 의미
                if prevElem != None:
                    prevElem.myNext = nextElem

                if nextElem != None:
                    nextElem.myPrev = prevElem

                # 맨 마지막 노드를 지운 경우 .end를 다시 갱신해줘야함
                if current == self.end:
                    self.end = prevElem

                # 맨 처음 노드를 지운 경우 .start를 다시 갱신해줘야함
                if current == self.start:
                    self.start = nextElem

            current = current.myNext  # (while문은 계속 도는 중) 다음 노드로 넘어가도록

    def getOrder(self, orderId):
        # 몇 번째 인지
        cnt = 0

        if self.start == None and self.end == None:
            return -1

        current = self.start

        while current != None:
            if current.data == orderId:
                return cnt + 1

            current = current.myNext
            cnt = cnt + 1

        return -1


# hard version (1-7)
'''
1. LinkedListElement 클래스를 완성하세요.
2. orderManager 클래스를 완성하세요.
'''


class LinkedListElement:
    def __init__(self, data, myPrev, myNext):
        self.data = data
        self.myPrev = myPrev
        self.myNext = myNext


class orderManager:
    def __init__(self):
        self.start = None
        self.end = None
        self.elems = {}  # 주문번호들을 저장하는 딕셔너리

    def addOrder(self, orderId):
        elem = LinkedListElement(orderId, None, None)

        self.elems[orderId] = elem

        if self.start == None and self.end == None:
            self.start = elem
            self.end = elem
        else:
            self.end.myNext = elem
            elem.myPrev = self.end
            self.end = elem

    def removeOrder(self, orderId):
        if self.start == None and self.end == None:
            return

        # 이전에는 지우기 위해 while문으로 계속 돌았는데, 이제는 딕셔너리를 통해 지워야할 요소를 바로 찾아냄
        cur = self.elems[orderId]

        if self.start == cur and self.end == cur:
            self.start = None
            self.end = None
        elif self.start == cur:
            self.start = cur.myNext
            # cur가 가리키는 다음 노드의 이전 노드를 None으로 해줌 -> 더이상 cur를 가리키고 있는 노드가 없음
            (cur.myNext).myPrev = None
        elif self.end == cur:
            self.end = cur.myPrev
            # cur이전 정점인 cur.myPrev가 현재는 myNext를 cur로 들고있었는데 이제는 들고있지 않겠다(None)
            (cur.myPrev).myNext = None
        else:
            cur.myPrev.myNext = cur.myNext
            cur.myNext.myPrev = cur.myPrev

    def getOrder(self, orderId):
        cnt = 1
        cur = self.start

        while cur != None:
            if cur.data == orderId:
                return cnt
            cur = cur.myNext
            cnt = cnt + 1
        return -1


# main()함수 없음
