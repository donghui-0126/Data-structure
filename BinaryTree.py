class Node:
    """이진 트리 노드 클래스"""

    def __init__(self, data):
        """데이터와 두 자식 노드에 대한 레퍼런스"""
        self.data = data
        self.left_child = None
        self.right_child = None

"""노드 인스턴스 생성"""
root = Node(2)
B = Node(3)
C = Node(5)
D = Node(7)
E = Node(11)

#루트 노드에서 자식 노드 지정
root.left_child = B
root.right_child = C

#D E 를 노드 B의 자식 노드로 지정
B.left_child = D
B.right_child = E