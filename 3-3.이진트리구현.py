# 어떤 트리의 루트 노드를 갖고 있다.
class Tree:
    def __init__(self, i, l, r):
        self.index = i
        self.left = l
        self.right = r

    # 재귀적으로 동작한다.
    # 새로운 노드가 현재 노드의 자식으로 추가되어야 하는 경우 -> 바로 추가
    # 그렇지 않다면, 자기 자식 중에 새로운 노드를 받을 수 있는 노드 탐색 -> 재귀 알고리즘

    def addNode(self, i, l, r):
        '''
        트리 내의 정점 i에 대하여 왼쪽자식을 l, 오른쪽 자식을 r로
        설정해주는 함수를 작성하세요.
        '''
        if self.index == None or self.index == i:
            self.index = i
            self.left = Tree(l, None, None) if l != None else None
            self.right = Tree(r, None, None) if r != None else None

            return True

        else:
            flag = False

            if self.left != None:
                flag = self.left.addNode(i, l, r)

            if flag == False and self.right != None:
                flag = self.right.addNode(i, l, r)

            return flag
