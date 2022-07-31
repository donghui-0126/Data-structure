def swap(tree, index_1, index_2):
    """완전 이진 트리의 노드 index_1과 노드 index_2의 위치를 바꿔준다"""
    temp = tree[index_1]
    tree[index_1] = tree[index_2]
    tree[index_2] = temp


def heapify(tree, index, tree_size):
    """
    heapify 함수
    3개의 노드중에서 제일 큰 노드를 구해서 그 노드와 바꿔가면서 재귀적으로 실행됨.
    결론적으로는 제일 큰 노드가 index노드와 바뀌게 됨
    """

    # 왼쪽 자식 노드의 인덱스와 오른쪽 자식 노드의 인덱스를 계산
    left_child_index = 2 * index
    right_child_index = 2 * index + 1
    
    largest = index


    #3개의 노드중에서 가장 큰 값을 구해서 index를 largest에 저장
    if 0 < left_child_index < tree_size and tree[largest] <tree[left_child_index]:
        largest = left_child_index
    if 0 < right_child_index < tree_size and tree[largest] < tree[right_child_index]:
        largest = right_child_index
    
    if largest != index:
        swap(tree, index, largest)
        heapify(tree, largest, tree_size)
# 실행 코드
tree = [None, 15, 5, 12, 14, 9, 10, 6, 2, 11, 1]  # heapify하려고 하는 완전 이진 트리
heapify(tree, 2, len(tree))
print(tree) 

#heapify 시간 복잡도: O(lg(n))
"""
맨 뒤 인덱스부터 역순으로 heapify를 호출하면 힙이 된다.
"""
# heapify를 이용해서 힙 만들기의 시간 복잡도: O(nlg(n))