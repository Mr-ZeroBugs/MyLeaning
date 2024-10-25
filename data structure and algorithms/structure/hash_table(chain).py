class HashTable:
    def __init__(self):
        self.max = 10
        self.arr = [[] for _ in range(self.max)] 

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.max

    def __setitem__(self, key, val):
        h = self.get_hash(key)
        found = False
        # ตรวจว่าคีย์มีอยู่ในลิงก์ลิสต์ที่ตำแหน่ง h หรือไม่
        for idx, element in enumerate(self.arr[h]):
            if element[0] == key:
                self.arr[h][idx] = (key, val)  # update value if exist
                found = True
                break
        if not found:
            self.arr[h].append((key, val))  # if not, create new one

    def __getitem__(self, key):
        h = self.get_hash(key)
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]  # คืนค่า value ของคีย์ที่ตรงกัน
        return None  # ไม่พบคีย์

    def __delitem__(self, key):
        h = self.get_hash(key)
        for idx, element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][idx]  # ลบคู่คีย์-ค่าออกจากลิงก์ลิสต์
                return

# ตัวอย่างการใช้งาน
t = HashTable()

# เพิ่มข้อมูล
t["test"] = 7
t["test2"] = 8
t["test"] = 10  # อัพเดตค่าของ "test"

# ดึงข้อมูล
print(t["test"])   #  10
print(t["test2"])  #  8
print(t["missing"])  # NOne cuz never define

del t["test"]
print(t["test"])   # None cuz deleted

print(t.arr)
