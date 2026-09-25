class MyHashSet:

    def __init__(self):
        self.n = 1000
        self.hor_arr = [None] * (self.n + 1)
    
    def add(self, key: int) -> None:
        hor = key // self.n
        ver = key % self.n
        if not self.hor_arr[hor]:
            self.hor_arr[hor] = [None] * self.n
            self.hor_arr[hor][ver] = key
            return 
        self.hor_arr[hor][ver] = key
        return 

    def remove(self, key: int) -> None:
        if not self.contains(key):
            return 
        self.hor_arr[key // self.n][key % self.n] = None 
        return 

    def contains(self, key: int) -> bool:
        hor, ver = key // self.n, key % self.n
        if self.hor_arr[hor] is None or self.hor_arr[hor][ver] is None:
            return False 
        return True 

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)