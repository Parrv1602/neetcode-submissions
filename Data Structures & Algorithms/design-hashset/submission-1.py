class MyHashSet:

    def __init__(self):
        self.hashlist = []

    def add(self, key: int) -> None:
        if key not in self.hashlist:
            self.hashlist.append(key)

    def remove(self, key: int) -> None:
        if key not in self.hashlist:
            pass
        else:
            self.hashlist.remove(key)

    def contains(self, key: int) -> bool:
        for element in self.hashlist:
            if key == element:
                return True
        
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)