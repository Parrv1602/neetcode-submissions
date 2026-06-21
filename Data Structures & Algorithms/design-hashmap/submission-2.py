class ListNode:
    def __init__(self, key=-1, val=-1, next=None):
        self.key = key
        self.val = val
        self.next = next

class MyHashMap:
    #map function in python "maps" keys to values and allocates 
    def __init__(self):
        self.hashmap = [ListNode() for i in range(1000)]

    def get_key(self, key):
        '''
        Uniquely identifies a linked list via the remainder because a user may add a key which is, for example, 
        100000. Since there are only 1000 linked lists, dividing the key by the number of values gives a 
        value that is used to identify that linked list. 
        '''
        return key % len(self.hashmap)

    def put(self, key: int, value: int) -> None:
       current_node = self.hashmap[self.get_key(key)]
       #Skip dummy node
       '''
       A linked list will have a key, value in the node.
       You get the current node (the unique identifier for a linked list in the hashmap)
       A value is put in the next node in the LinkedList rather than the current node, so 
       that's why .next is used.

       '''
       while current_node.next:
        if current_node.next.key == key:
            current_node.next.val = value
            return #returns None to skip going through other linked lists unnecessarily
        current_node = current_node.next

       #If key doesn't exist, then create a new linked list instance
       current_node.next = ListNode(key, value)

    def get(self, key: int) -> int:
        current_node =  self.hashmap[self.get_key(key)].next
        '''
        Want to skip the dummy node.
        Since we want to retrieve the value of the linked list node that corresponds with that key,
        then we don't want to compare using current_node.next
        '''
        while current_node:
            if current_node.key == key:
                return current_node.val
            current_node = current_node.next

        return -1
     

    def remove(self, key: int) -> None:
        current_node = self.hashmap[self.get_key(key)]
        '''
        In a linked list, if next node's key is the key the user wants to remove,
        then the current node's next will be redirect to the next next node.
        '''
        while current_node.next:
            if current_node.next.key == key:
                current_node.next = current_node.next.next
                return
            current_node = current_node.next
        

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)