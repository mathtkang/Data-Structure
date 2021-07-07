class maxMachine:
    def __init__(self):
        # 객체가 처음 생성될때 자동으로 호출되는 함수
        self.numbers = []

    def addNumber(self, n):
        self.numbers.append(n)

    def removeNumber(self, n):
        self.numbers.remove(n)

    def getMax(self):
        return max(self.numbers)

####


def main():
    myMachine = maxMachine()
    n = int(input())

    for i in range(n):
        line = [int(v) for v in input().split()]
        if line[0] == 0:
            myMachine.addNumber(line[1])
        elif line[0] == 1:
            myMachine.removeNumber(line[1])
        elif line[0] == 2:
            print(myMachine.getMax())


if __name__ == "__main__":
    main()
