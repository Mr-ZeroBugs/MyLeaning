class HashTable:
    def __init__(self):
        self.max = 100
        self.arr = [None for i in range(self.max)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.max

    def __setitem__(self, key, val):
        h = self.get_hash(key)
        while self.arr[h] is not None and self.arr[h][0] != key:  #open address used to manage when hash is created redundantly. like assuming abc and xyz both give us the same hash
            h = (h + 1) % self.max
        self.arr[h] = (key, val)  # tuple (key, value)

    def __getitem__(self, key):
        h = self.get_hash(key)
        while self.arr[h] is not None:
            if self.arr[h][0] == key:
                return self.arr[h][1] 
            h = (h + 1) % self.max
        return None

t = HashTable()

t["test"] = 7
t["test"] = 8
print(t["test"])