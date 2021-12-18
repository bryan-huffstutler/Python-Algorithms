class HashTable:
    def __init__(self) -> None:
        self.size = 10
        self.slots = [None] * self.size 
        self.data = [None] * self.size

    def getKeys(self):
        return self.slots
    
    def getValues(self):
        return self.data
    
    def hashfunction(self,key):
        return key % self.size
    
    def rehash(self,key):
        return key // self.size
    
    def put(self,key,data):
        # Insert your code here to store key and data 
        hash = self.hashfunction(key)
        if self.data[hash] == None:
            self.data[hash] = data
            self.slots[hash] = key
        else:
            # Update Handling
            if self.slots[hash] == key:
                self.data[hash] = data
            # Collision Handling
            else:
                hash = self.rehash(key)
                if self.data[hash] == None:
                    self.data[hash] = data
                    self.slots[hash] = key
                else:
                    return None
        
    def get(self,key):
        # Insert your code here to get data by key
        hashValue = self.hashfunction(key)
        return self.data[hashValue]
    
    def __getitem__ (self,key):
        return self.get(key)

    def __setitem__ (self,key,data):
        self.put(key,data)


# Store remaining input data
H = HashTable()
H[69] = 'A'
H[66] = 'B'
H[80] = 'C'
H[35] = 'D'
H[18] = 'E'
H[52] = 'F'
H[89] = 'G'
H[70] = 'H'
H[12] = 'I'

# print the slot values
print(H.getKeys())

# print the data values
print(H.getValues())

# print the value for key 52
print(H[52])