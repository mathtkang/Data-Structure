# from beads import processBeads
def main():
    n = int(input())
    myList = []

    for i in range(n):
        myList.append([int(v) for v in input().split()])

    print(*processBeads(myList))


if __name__ == "__main__":
    main()


####

# 연결리스트가 갖고있는 하나의 정점
class LinkedListElement:
    def __init__(self, val, ptr):
        self.value = val  # 정수
        self.myNext = ptr  # 또다른 Element


class LinkedListPipe:
    def __init__(self):  # 리스트 myPipe를 만듭니다. 이는 구슬의 배치를 저장합니다.
        # 연결 리스트의 시작 점점과 끝 정점을 가리키는 것이 각각 start, end
        # 얘들을 None으로 초기화
        self.start = None
        self.end = None
        # 마치 my_list = [] 처럼 공간 확보

    def addLeft(self, n):  # 파이프의 왼쪽으로 구슬 n을 삽입합니다.
        if self.start == None and self.end == None:
            elem = LinkedListElement(n, None)

            self.start = elem
            self.end = elem
        else:
            elem = LinkedListElement(n, self.start)  # 기존에 있던 시작점 의미

            self.start = elem  # 새로운 값으로 바뀜

    def addRight(self, n):  # 파이프의 오른쪽으로 구슬 n을 삽입합니다.
        if self.start == None and self.end == None:
            elem = LinkedListElement(n, None)

            self.start = elem
            self.end = elem
        else:
            elem = LinkedListElement(n, None)  # 구슬이 맨 끝에 오는 거니까 None

            self.end.myNext = elem  # 기존에 존재하는 self.end의 myNext에 새로 만들어진 구슬을 넣는다는 말
            self.end = elem  # 링크드리스트의 마지막노드

    def getBeads(self):  # 파이프의 배치를 list로 반환합니다.
        result = []

        # 현재 노드 나타냄
        current = self.start

        while current != None:
            result.append(current.value)  # 구슬의 번호
            current = current.myNext  # 구슬 번호 갱신 (다음값을 가리키도록 함)

        return result


def processBeads(myInput):
    '''
    구슬을 파이프에 넣는 행위가 myInput으로 주어질 때, 구슬의 최종 배치를 리스트로 반환하는 함수를 작성하세요.
    myInput[i][0] : i번째에 넣는 구슬의 번호
    myInput[i][1] : i번째에 넣는 방향
    예를 들어, 예제의 경우 
    myInput[0][0] = 1, myInput[0][1] = 0,
    myInput[1][0] = 2, myInput[1][1] = 1,
    myInput[2][0] = 3, myInput[2][1] = 0
    입니다.
    '''
    myPipe = LinkedListPipe()

    for bead, direction in myInput:
        if direction == 0:
            myPipe.addLeft(bead)
        elif direction == 1:
            myPipe.addRight(bead)

    return myPipe.getBeads()


# 배열과 연결리스트
# 자료구조상 추상적자료형 이라는건 똑같은데, 어떤 방식으로 코드를 짜느냐에 따라서 동작이 달라지는거임
