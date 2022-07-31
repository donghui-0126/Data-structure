from types import new_class


class Node:
    """링크드 리스트 노드"""
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    """링크드 리스트"""
    def __init__(self):
        self.head = None
        self.tail = None
    
    def delete(self, node_to_delete):
        """더블리 링크드 리스트 삭제 연산 메소드"""
        # 코드를 쓰세요
        if (node_to_delete.next == None)\
        and(node_to_delete.prev == None):
            self.head = None
            self.tail = None
        
        elif (node_to_delete.next == None)\
        and(node_to_delete.prev != None):
            self.tail = node_to_delete.prev
            self.tail.next = None
        
        elif (node_to_delete.next != None)\
        and(node_to_delete.prev == None):
            self.head = node_to_delete.next
            self.head.prev = None
        
        else:
            node_to_delete.prev.next = node_to_delete.next
            node_to_delete.next.prev = node_to_delete.prev

    def append(self, data):
        """링크드 리스트 추가 연산 메소드"""
        new_node = Node(data)

        #링크드 리스트가 비어있는 경우
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def insert_after(self, data, previous_node):
        """링크드 리스트 삽입 연산 메소드 단, 링크드 리스트가 비어있지 않은 경우"""
        new_node = Node(data)
        if previous_node is self.tail:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        else:
            next_node = previous_node.next
            previous_node.next = new_node
            new_node.prev = previous_node
            new_node.next = next_node
            next_node.prev = new_node

    def find_node_at(self, index):
        """ 링크드 리스트 접근 연산 메소드. 파라미터 인덱스는 항상 있다고 가정한다"""
        iterator = self.head  # 링크드 리스트를 돌기 위해 필요한 노드 변수
        # index 번째 있는 노드로 간다
        for _ in range(index):
            iterator = iterator.next
        
        return iterator
    
    def find_node_with_data(self, data):
        """링크드 리스트에서 주어진 데이터를 갖고있는 노드를 리턴한다. 단, 해당 노드가 없으면 None을 리턴한다"""
        iterator = self.head  # 링크드 리스트를 돌기 위해 필요한 노드 변수
        
        while iterator is not None:
            if iterator.data == data:
                return iterator

            iterator = iterator.next

        return None

    def __str__(self):
        """링크드 리스트를 문자열로 표현해서 리턴하는 메소드"""
        res_str = "|"

        # 링크드 리스트 안에 모든 노드를 돌기 위한 변수. 일단 가장 앞 노드로 정의한다.
        iterator = self.head

        # 링크드 리스트 끝까지 돈다
        while iterator is not None:
            # 각 노드의 데이터를 리턴하는 문자열에 더해준다
            res_str += " {} |".format(iterator.data)
            iterator = iterator.next  # 다음 노드로 넘어간다

        return res_str


# 새로운 링크드 리스트 생성
my_list = LinkedList()

# 새로운 노드 4개 추가
my_list.append(2)
my_list.append(3)
my_list.append(5)
my_list.append(7)

print(my_list)

# 두 노드 사이에 있는 노드 삭제
node_at_index_2 = my_list.find_node_at(2)
my_list.delete(node_at_index_2)
print(my_list)

# 가장 앞 노드 삭제
head_node = my_list.head
print(my_list.delete(head_node))
print(my_list)

# 가장 뒤 노드 삭제
tail_node = my_list.tail
my_list.delete(tail_node)
print(my_list)

# 마지막 노드 삭제
last_node  = my_list.head
my_list.delete(last_node)
print(my_list)