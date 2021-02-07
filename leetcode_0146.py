class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = []     # Store the key
        self.k_v_dict = {}


    def get(self, key: int) -> int:
        if key in self.k_v_dict:
            self.cache.remove(key)
            self.cache += [key]
            return self.k_v_dict[key]
        else:
            return -1 


    def put(self, key: int, value: int) -> None:
        if key in self.k_v_dict:
            self.k_v_dict[key] = value
            self.cache.remove(key)
            self.cache += [key]
        else:
            if len(self.cache) < self.capacity:
                self.cache += [key]
                self.k_v_dict[key] = value
            else:
                poped_key = self.cache.pop(0)
                del self.k_v_dict[poped_key]
                self.k_v_dict[key] = value
                self.cache += [key]



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
