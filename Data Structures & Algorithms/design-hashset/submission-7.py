class Node:
    def __init__(self, index=0, key=0, next=None):
        self.index = index
        self.key = key
        self.next = next

class MyHashSet:
    
    def __init__(self):
        self.LinkedList = [Node() for i in range(10000)]

    def uniquely_identify_node(self, key):
        return key % len(self.LinkedList)

    def add(self, key: int) -> None:
        index = self.uniquely_identify_node(key)
        curr_node = self.LinkedList[index]

        while curr_node.next:
            if curr_node.next.key == key:
                return
            curr_node = curr_node.next
        
        curr_node.next = Node(index, key)

    def remove(self, key: int) -> None:
        index = self.uniquely_identify_node(key)
        curr_node = self.LinkedList[index]
        
        while curr_node.next:
            if curr_node.next.key == key:
                curr_node.next = curr_node.next.next
                return
            curr_node = curr_node.next

    def contains(self, key: int) -> bool:
        index = self.uniquely_identify_node(key)
        curr_node = self.LinkedList[index]

        while curr_node.next:
            if curr_node.next.key == key:
                return True
            
            curr_node = curr_node.next
        return False
