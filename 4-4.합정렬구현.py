import heapq


class PriorityQueue:

    def __init__(self):
        self.data = []

    def push(self, value):
        heapq.heappush(self.data, value)

    def pop(self):
        if len(self.data) > 0:
            heapq.heappop(self.data)

    def top(self):
        if len(self.data) == 0:
            return -1
        else:
            return self.data[0]


def heapSort(items):
    '''
    items에 있는 원소를 heap sort하여 리스트로 반환하는 함수를 작성하세요.
    단, 이전에 작성하였던 priorityQueue를 이용하세요.
    '''

    result = []

    pq = PriorityQueue()

    for item in items:
        pq.push(item)

    for i in range(len(items)):
        result.append(pq.top())
        pq.pop()

    return result
