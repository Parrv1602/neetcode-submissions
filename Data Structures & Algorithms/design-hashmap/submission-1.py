'''
Question: Create a hashmap where there is a key and a value. Multiple values can be assigned to the same
key. 

Since at most 1000 keys will exist in the hashmap, create an array of size 1000.
Now, the 1000 size array can represent the entire hashmap, but what can represent the individual keys 
in the hashmap? Just values in the array where the index represents the keys won't work because each time
a "put" function is used, the previous value associated with the key will get deleted.

Instead, create arrays within a larger array using a for loop ("mini arrays").
'''

class LinkedList:
    def __init__(self, key= -1, val = -1, next=None):
        self.key = key
        self.val = val
        self.next = next


class MyHashMap:
    #map function in python "maps" keys to values and allocates 
    def __init__(self):
        #Creates 1000 instances of LinkedList() objects, each with key, val, and next attributes
        #Each LinkedList() 
        self.hashmap = [LinkedList() for i in range(1000)]

    def get_key(self, key):
        return key % len(self.hashmap)
        '''
        Why Modulo?
        Because an index will be between 0-999 (max of 1000 keys).
        But a user may input a key of 1001, which cannot be mapped even if there is space in the array.
        So, you find the remainder of the key. An input of any key (even those greater than 1000) will
        return a value that is between 0-999
        '''

    def put(self, key: int, value: int) -> None:
        current_node = self.hashmap[self.get_key(key)]
        while current_node.next:
            if current_node.next.key == key:
                current_node.next.val = value
                return 
            current_node = current_node.next
        
        current_node.next = LinkedList(key, value)
        

        #If the linked list is empty, then there is not current_node.next, so set the current.next value to LinkedList
        #So that the new node in the linked list can inherit the attributes of the LinkedList class

    def get(self, key: int) -> int:
        current_node = self.hashmap[self.get_key(key)].next #Avoid searching the dummy node
        while current_node:
            if current_node.key == key:
                return current_node.val
            current_node = current_node.next
        return -1


    def remove(self, key: int) -> None:
        '''
        You cannot "remove" nodes from a linked list, instead you redirect the current node's next to the 
        next next's node and ignore the next node.
        '''
        current_node = self.hashmap[self.get_key(key)]
        while current_node.next:
            if current_node.next.key == key:
                current_node.next = current_node.next.next
                #Blank return statements are important because it tells program to stop the while loop and function
                #If the condition didn't return None to stop the loop, it would go on until end of linked list
                #and remove unintended values
                return
            current_node = current_node.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)