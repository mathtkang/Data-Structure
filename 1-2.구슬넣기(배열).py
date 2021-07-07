#from beads import processBeads
def main():
    n = int(input())
    myList = []

    for i in range(n):
        myList.append([int(v) for v in input().split()])

    print(*processBeads(myList))


if __name__ == "__main__":
    main()


####
# 1. ListPipe 클래스를 완성하세요.
# 2. processBeads 함수를 완성하세요.

class ListPipe:
    def __init__(self):  # 리스트 myPipe를 만듭니다. 이는 구슬의 배치를 저장합니다.
        self.myPipe = []

    def addLeft(self, n):  # 파이프의 왼쪽으로 구슬 n을 삽입합니다.
        self.myPipe.insert(0, n)

    def addRight(self, n):  # 파이프의 오른쪽으로 구슬 n을 삽입합니다.
        self.myPipe.append(n)

    def getBeads(self):  # 파이프의 배치를 list로 반환합니다.
        return self.myPipe


def processBeads(myInput):  # 메인함수
    '''
    구슬을 파이프에 넣는 행위가 myInput으로 주어질 때, 구슬의 최종 배치를 리스트로 반환하는 함수를 작성하세요.
    myInput[i][0] : i번째에 넣는 구슬의 번호 (왼쪽)
    myInput[i][1] : i번째에 넣는 방향 (오른쪽)

    예를 들어, 예제의 경우 
    myInput[0][0] = 1, myInput[0][1] = 0,
    myInput[1][0] = 2, myInput[1][1] = 1,
    myInput[2][0] = 3, myInput[2][1] = 0
    입니다.
    '''
    myPipe = ListPipe()
    for bead, direction in myInput:
        if direction == 0:
            myPipe.addLeft(bead)
        elif direction == 1:
            myPipe.addRight(bead)

    result = myPipe.getBeads()

    return result
