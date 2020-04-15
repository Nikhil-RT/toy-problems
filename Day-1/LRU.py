class LRU:

    def __init__(self,size):
        self.size = size
        self.directory = {}
        self.lru = {}

    def put(self,key,data):

        if (key not in self.directory and len(self.directory) == self.size):
            last = min(self.lru.keys(), key = lambda i:self.lru[i])
            self.lru.pop(last)
            self.directory.pop(last)
        self.directory[key] = data
        self.lru[key] = 1
        
        return "Success"

    def get(self,key):
        if key in self.directory:
            self.lru[key] = self.lru[key] + 1
            return self.directory[key]
        else:
            print ("Not Found")

    def get_cache(self):
        return self.directory