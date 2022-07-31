# 힙과 다르게 리스트를 이용해서 구현하지 않음
class Node:
    """이진 탐색 트리 노드"""
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left_child = None
        self.right_child = None

def print_inorder(node):
    """주어진 노드를 in-order로 출력해주는 함수"""
    if node is not None:
        print_inorder(node.left_child)
        print(node.data)
        print_inorder(node.right_child)

class BinarySearchTree:
    """이진 탐색 트리 클래스"""
    def __init__(self):
        self.root = None

    @staticmethod
    def find_min(node):
        """(부분)이진 탐색 트리의 가장 작은 노드 리턴"""
        # 코드를 쓰세요
        temp = node
        while temp.left_child != None:
            temp = temp.left_child
        return temp

    def search(self, data):
        """이진 탐색 트리 탐색 메소드, 찾는 데이터를 갖는 노드가 없으면 None을 리턴한다"""
        temp = self.root  # 탐색용 변수, root 노드로 초기화

        # 원하는 데이터를 갖는 노드를 찾을 때까지 돈다
        while temp is not None:
            # 원하는 데이터를 갖는 노드를 찾으면 리턴
            if data == temp.data:
                return temp
            # 원하는 데이터가 노드의 데이터보다 크면 오른쪽 자식 노드로 간다
            if data > temp.data:
                temp = temp.right_child
            # 원하는 데이터가 노드의 데이터보다 작으면 왼쪽 자식 노드로 간다
            else:
                temp = temp.left_child

        return None # 원하는 데이터가 트리에 없으면 None 리턴


    def insert(self, data):
        """이진 탐색 트리 삽입 메소드"""
        new_node = Node(data)  # 삽입할 데이터를 갖는 노드 생성

        # 트리가 비었으면 새로운 노드를 root 노드로 만든다
        if self.root is None:
            self.root = new_node
            return

        # 코드를 쓰세요
        temp = self.root  # 저장하려는 위치를 찾기 위해 사용할 변수. root 노드로 초기화한다

        # 원하는 위치를 찾아간다
        while temp is not None:
            if data > temp.data:  # 삽입하려는 데이터가 현재 노드 데이터보다 크다면
                # 오른쪽 자식이 없으면 새로운 노드를 현재 노드 오른쪽 자식으로 만듦
                if temp.right_child is None:
                    new_node.parent = temp
                    temp.right_child = new_node
                    return
                # 오른쪽 자식이 있으면 오른쪽 자식으로 간다
                else:
                    temp = temp.right_child
            else:  # 삽입하려는 데이터가 현재 노드 데이터보다 작다면
                # 왼쪽 자식이 없으면 새로운 노드를 현재 노드 왼쪽 자식으로 만듦
                if temp.left_child is None:
                    new_node.parent = temp
                    temp.left_child = new_node
                    return
                # 왼쪽 자식이 있다면 왼쪽 자식으로 간다
                else:
                    temp = temp.left_child
        

    def delete(self, data):
        """이진 탐색 트리 삭제 메소드"""
        node_to_delete = self.search(data)  # 삭제할 노드를 가지고 온다
        parent_node = node_to_delete.parent  # 삭제할 노드의 부모 노드

        # 경우 1: 지우려는 노드가 leaf 노드일 때
        if node_to_delete.left_child is None and node_to_delete.right_child is None:
            if self.root is node_to_delete:
                self.root = None
            else:  # 일반적인 경우
                if node_to_delete is parent_node.left_child: 
                    parent_node.left_child = None
                else:
                    parent_node.right_child = None

        # 경우 2: 지우려는 노드가 자식이 하나인 노드일 때:
        elif ((node_to_delete.left_child == None and node_to_delete.right_child != None) or\
             (node_to_delete.right_child == None and node_to_delete.left_child != None)):
            if node_to_delete == self.root:
                if node_to_delete.right_child == None:
                    self.root = node_to_delete.left_child
                    self.root.parent = None
                else:
                    self.root = node_to_delete.right_child
                    self.root.parent = None
            elif parent_node.right_child == node_to_delete:
                if node_to_delete.right_child == None:
                    parent_node.right_child = node_to_delete.left_child
                    node_to_delete.left_child.parent = parent_node
                else:
                    parent_node.right_child = node_to_delete.right_child
                    node_to_delete.right_child.parent = parent_node 
            else:
                if node_to_delete.left_child == None:
                    parent_node.left_child = node_to_delete.right_child
                    node_to_delete.right_child.parent = parent_node
                else:
                    parent_node.left_child = node_to_delete.left_child
                    node_to_delete.left_child.parent = parent_node 
        # 경우 3: 지우려는 노드가 2개의 자식이 있을 때
        else:
            successor = self.find_min(node_to_delete.right_child)
            self.delete(successor.data)
            node_to_delete.data = successor.data
            


    def print_sorted_tree(self):
        """이진 탐색 트리 내의 데이터를 정렬된 순서로 출력해주는 메소드"""
        print_inorder(self.root)  # root 노드를 in-order로 출력한다


# 시간복잡도(평균적)
# 데이터 삽입: O(h)
# 데이터 탐색: O(h)
# 데이터 삭제: O(h)

#트리가 편향되어 있지 않다면 평균적으로 O(lg(n)), 최악의 경우 O(n)

"""
딕셔너리를 구현할 수 있음.

딕셔너리라고 해도 순서를 저장해야할 때 
해시테이블보다는 이진탐색트리를 사용함.
ex) key로 정렬하기

"""