# from queue import Queue

# Queue 클래스 복붙 (위의 import 대신 직접 구현 큐 클래스)
class Queue:
    '''
    List를 이용하여 다음의 method들을 작성하세요.
    '''

    def __init__(self):
        self.myQueue = []

    def push(self, n):
        self.myQueue.append(n)

    def pop(self):
        if self.empty() == 1:
            return

        del self.myQueue[0]

    def size(self):
        return len(self.myQueue)

    def empty(self):
        if self.size() == 0:
            return 1
        else:
            return 0

    def front(self):
        if self.empty() == 1:
            return -1

        return self.myQueue[0]

    def back(self):
        if self.empty() == 1:
            return -1

        return self.myQueue[-1]


####여기서부터####

class orderInfo:  # 입력받는 주문에 대한 정보 저장
    def __init__(self, t, d, v):
        self.time = t
        self.duration = d
        self.vip = v


def selectQueue(normalQueue, vipQueue, time, orders):
    normalIndex = normalQueue.front()
    vipIndex = vipQueue.front()

    if vipIndex == -1:
        return normalQueue

    if normalIndex == -1:
        return vipQueue

    # 우리가 밀린 작업이 normal에도 없고 vip에도 없는 경우 -> 더 빨리 도착한 주문을 처리한다.
    if time < orders[normalIndex].time and time < orders[vipIndex].time:
        if orders[vipIndex].time <= orders[normalIndex].time:
            return vipQueue
        else:
            return normalQueue

    # 우리가 밀린 작업이 normal에만 있는 경우
    if time >= orders[normalIndex].time and time < orders[vipIndex].time:
        return normalQueue

    # 우리가 밀린 작업이 vip에만 있는 경우
    if time >= orders[vipIndex].time and time < orders[normalIndex].time:
        return vipQueue

    # 우리가 밀린 작업이 normal에도 있고 vip에도 있는 경우 -> vip를 반환
    return vipQueue


def processOrder(orders):  # 주문 정보가 주어질 때, 주문이 처리되는 순서를 반환합니다.
    result = []

    # 일반주문이랑 vip주문 두개의 큐 만듦
    normalQueue = Queue()
    vipQueue = Queue()

    jobEndTime = 0
    curTime = -1

    for i in range(len(orders)):
        curTime = orders[i].time

        if orders[i].vip == 0:
            normalQueue.push(i)
        else:
            vipQueue.push(i)

        while jobEndTime <= curTime and not(normalQueue.empty() == 1 and vipQueue.empty() == 1):
            # normalQueue 또는 vipQueue를 선택한다.
            targetQueue = selectQueue(
                normalQueue, vipQueue, jobEndTime, orders)

            # 우리가 처리할 주문 번호를 가져온다.
            index = targetQueue.front()

            # 주문을 처리한다. = jobEndTime을 증가시킨다.
            # jobEndTime > orders[index].time 인 경우 : 주문이 밀려있어서 이전 작업을 끝내자마자 바로 다음 작업을 시작한 경우
            # jobEndTime < orders[index].time 인 경우 : 주문이 밀려있지 않아서 이전 작업을 끝내고 여유가 있는 경우, 다음 작업이 들어온 시점에 처리를 한다.
            jobEndTime = max(
                jobEndTime, orders[index].time) + orders[index].duration

            result.append(index + 1)
            targetQueue.pop()

    # jobEndTime > curTime 인 경우 : 마지막까지 처리되지 않은 주문이 있을 수 있음
    # for문 밖에서 작성
    while not(normalQueue.empty() == 1 and vipQueue.empty() == 1):  # 위의 로직과 동일
        targetQueue = selectQueue(normalQueue, vipQueue, jobEndTime, orders)
        index = targetQueue.front()
        jobEndTime = max(
            jobEndTime, orders[index].time) + orders[index].duration

        result.append(index + 1)
        targetQueue.pop()

    return result
