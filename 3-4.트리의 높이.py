'''
getHeight 함수를 작성하세요.
(재귀 이용해서 구현)
'''


def getHeight(myTree):
    '''
    myTree의 높이를 반환하는 함수를 작성하세요.
    '''
    # 루트 노드를 포함해서, 왼쪽 서브트리와 오른쪽 서브트리를 모두 포함.
    # 왼쪽 서브트리의 높이를 구해보고,
    # 오른쪽 서브트리의 높이를 구해보고,
    # 두 높이를 비교해본다.
    # 더 높은 서브트리의 높이 + 1 (루트 노드)

    if myTree == None:
        return 0
    else:
        return 1 + max(getHeight(myTree.left), getHeight(myTree.right))
