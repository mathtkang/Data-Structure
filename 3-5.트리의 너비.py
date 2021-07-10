# class Tree:
#     def __init__(self, i, l, r) :
#         self.index = i
#         self.left = l
#         self.right = r
#         self.depth = -1

#     def setDepth(self, d) :
#         self.depth = d

#     def addNode(self, i, l, r) :
#         if self.index == None or self.index == i :
#             self.index = i
#             self.left = Tree(l, None, None) if l != None else None
#             self.right = Tree(r, None, None) if r != None else None
#             return True

#         else :
#             flag = False

#             if self.left != None :
#                 flag = self.left.addNode(i, l, r)

#             if flag == False and self.right != None :
#                 flag = self.right.addNode(i, l, r)

#             return flag


def inorder(tree, depth):
    result = []

    if tree.left != None:
        result += inorder(tree.left, depth + 1)

    tree.setDepth(depth)  # 재귀 : 루트노드로부터 거리가 1 멀어짐
    result.append(tree)

    if tree.right != None:
        result += inorder(tree.right, depth + 1)

    return result


def getWidth(myTree):
    '''
    myTree의 너비가 가장 넓은 레벨과 그 레벨의 너비를 반환하는 함수를 작성하세요.
    가장 넓은 레벨 l과 그 레벨의 너비 w를 튜플로 반환해야 합니다.

    반환값 형식 : (l, w)
    '''
    result = inorder(myTree, 1)
    n = len(result)

    # 정점의 개수는 1000개 이하이다. (입력조건)
    # 깊이의 최댓값은 1000

    # left[i] = 깊이가 i인 모든 노드들 중에서, 가장 왼쪽에 있는 노드의 행
    # right[i] = 깊이가 i인 모든 노드들 중에서, 가장 오른쪽에 있는 노드의 행

    # 어떤 깊이의 너비는 right[i] - left[i]

    left = [1001 for i in range(1001)]
    right = [-1 for i in range(1001)]
    maxDepth = 0

    for i in range(n):
        d = result[i].depth

        left[d] = min(left[d], i)
        right[d] = max(right[d], i)

        maxDepth = max(maxDepth, d)

    ansDepth = 0
    ans = 0

    for i in range(1, maxDepth+1):
        temp = right[i] - left[i] + 1

        if ans < temp:
            ansDepth = i
            ans = temp

    return (ansDepth, ans)
