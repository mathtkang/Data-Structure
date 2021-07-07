'''
orderManager 클래스를 완성하세요.
'''


class orderManager:
    '''
    주문을 처리하는 class를 작성합니다.
    '''

    def __init__(self):
        '''
        이 부분은 고치지 마세요.
        '''
        self.data = []  # 각각 주문에 대한 정보가 들어감

    def addOrder(self, orderId):  # 주문번호 orderId를 추가합니다.
        self.data.append(orderId)

    def removeOrder(self, orderId):  # 주문번호 orderId를 제거합니다.
        self.data.remove(orderId)

    def getOrder(self, orderId):
        '''
        주문번호 orderId가 몇 번째로 처리될지를 반환합니다.

        만약 주문번호 orderId가 존재하지 않으면 -1을 반환합니다. 
        '''
        for i in range(len(self.data)):
            if self.data[i] == orderId:
                return (i+1)

        return -1


#from orderManager import orderManager

def main():
    '''
    이 부분은 수정하지 마세요.
    '''

    line = [int(v) for v in input().split()]
    m = line[0]

    manager = orderManager()

    for i in range(m):
        line = [int(v) for v in input().split()]

        if line[0] == 1:
            manager.addOrder(line[1])

        elif line[0] == 2:
            manager.removeOrder(line[1])

        elif line[0] == 3:
            myOrder = manager.getOrder(line[1])

            if myOrder == -1:
                print("-1")
            else:
                print(str(manager.getOrder(line[1])))


if __name__ == "__main__":
    main()
