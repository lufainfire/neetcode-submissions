class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        
        

    def get(self, key: int) -> int:
        if key in self.cache:
            val = self.cache.pop(key)
            self.cache[key] = val
            return val
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        
            #delete least recently used key I need to keep track of usage or at least least used in O(1)
        
        if key in self.cache:
            self.cache.pop(key)

        elif len(self.cache) >= self.capacity:
            bad = next(iter(self.cache))
            del self.cache[bad]
        
        self.cache[key] = value
        
        

        


        #1,2,3  -> 1,{2,3,4} -> 1,2,3,4,1

        
