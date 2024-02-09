def hashFunction(inp):
    total = 0
    
    for i in inp:
        total += ord(i)
    
    total = total % 2345
    return total
    

class HashMap:
    def __init__(self):
        self.arr = [None] * 2345
    
    def getter(self, key):
        idx = hashFunction(key)
        return self.arr[idx]
    
    def setter(self, key, value):
        idx = hashFunction(key)
        self.arr[idx] = value
        

# custom   
print("Custom dictionary")
hm = HashMap()
hm.setter('karthick', 23)
hm.setter('sathish', 34)
hm.setter('vijay', 45)

hm.setter('suresh', 70)
print(hm.arr)




    
