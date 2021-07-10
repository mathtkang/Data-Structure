'''
BFS 함수를 구현하세요.
'''
from queue import Queue


def BFS(tree):
    '''
    tree를 너비 우선 탐색으로 순회하여 리스트로 반환하는 함수를 작성하세요.
    '''
    q = Queue()
    q.put(tree)

    result = []

    # q에 뭔가 들어있다면 계속 반복을 한다.
    # -> 더 이상 방문할 노드가 없을 때 종료한다.
    while len(q.queue) > 0:
        cur = q.get()
        if cur == None:
            continue

        result.append(cur.index)  # 방문

        q.put(cur.left)
        q.put(cur.right)

    return result
