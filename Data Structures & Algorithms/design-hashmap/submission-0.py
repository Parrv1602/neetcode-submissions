class ListNode:
    #Key value kept minus 1 incase input is searching an empty linked list
    def __init__(self, key=-1, val=-1, next=None):
        self.key = key
        self.val = val
        self.next = next

class MyHashMap:
    #map function in python "maps" keys to values and allocates 
    def __init__(self):
        #An array containing dummy nodes. Dummy nodes are just starting points for the linked list.
        self.LinkedListarray =[ListNode() for i in range(1000)]

    def find_key(self, key):
        return key % len(self.LinkedListarray) #Number of values stored in the Linked List array

    def put(self, key: int, value: int) -> None:
        #Finding the appropriate linked list stored in the LinkedListArray using the key and find_key()
        #Because linked lists don't start from the key itself, it starts from a dummy node
        curr = self.LinkedListarray[self.find_key(key)]
        #Since each linked list starts with a dummy node, start looping from the next node
        while curr.next:
            if curr.next.key == key:
                curr.next.val = value
                return #returns nothing "Null"
            curr = curr.next 
        
        #If curr.next is null (for example, an empty linked list) then the key, value should be appended
        curr.next = ListNode(key, value)
        

    def get(self, key: int) -> int:
        #We want to skip the dummy node so we start from .next
        curr = self.LinkedListarray[self.find_key(key)].next
        while curr:
            if curr.key == key:
                return curr.val
            curr = curr.next
        return -1

    def remove(self, key: int) -> None:
        #In a linked list, you set the pointer to skip a certain element that you want to delete
        curr = self.LinkedListarray[self.find_key(key)]
        while curr.next:
            if curr.next.key == key:
                curr.next = curr.next.next
                return 
            curr = curr.next
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)