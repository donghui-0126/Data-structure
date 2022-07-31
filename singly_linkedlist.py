class Node:
    """링크드 리스트의 노드 클래스"""

    def __init__(self,data):
        self.data = data #노드가 저장하는 데이터
        self.next = None #다음 노드에 대한 레퍼런스

class Linkedlist:
    """링크드 리스트 클래스"""

    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        """링크드 리스트 추가 연산 메소드"""
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
    
    def insert_after(self, previous_node, data):
        """링크드 리스트 삽입 메소드"""
        new_Node = Node(data)
        if (previous_node == self.tail):
            self.tail.next = new_Node
            self.tail = new_Node
        else:
            new_Node.next = previous_node.next
            previous_node.next = new_Node

    def find_node_at(self, index):
        """링크드 리스트 접근 연산 메소드"""
        iterator = self.head

        for _ in range(index):
            iterator = iterator.next

        return iterator

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
            node_to_delete.next = node_to_delete.prev.next
            node_to_delete.prev = node_to_delete.next.prev
        

    def delete_after(self, previous_node):
        """링크드 리스트 삭제 메소드"""
        if previous_node.next is self.tail:
            previous_node.next = None
        else:
            previous_node.next = previous_node.next.next

    def __str__(self):
        iterator = self.head
        string = "|"
        while iterator != None:
            string += " {} |".format(iterator.data)
            iterator = iterator.next
        return string

# 새로운 링크드 리스트 생성
my_list = Linkedlist()

#링크드 리스트에 데이터 추가
my_list.append(2)
my_list.append(5)
my_list.append(7)
my_list.append(9)
my_list.append(11)

iterator = my_list.head
node_3 = my_list.find_node_at(2)
my_list.insert_after(node_3, 10)
print(my_list)

my_list.delete_after(node_3)

print(my_list)
