
#HashMap
#Format Of Records

class AlgoHashTable:

    def __name__(self, size):
        self.size = size
        #self.hash_table = [[] for _ in range(self.size)]
        #self.hash_table = self.create_buckets()

    #def create_buckets(self):
    #    return [[] for _ in range(self.size)]

    def set_val(self, key, value):
        pass

    def get_val(self, key):
        pass

    def __str__(self):
        #return "Hello!"
        #return "".join(str(item) for item in self.hash_table)
hash_table = AlgoHashTable(256)
print(hash_table)




'''
*************************************************************************************
*************************************************************************************
*************************************************************************************

class AlgoHashTable:

    def __name__(self, size):
        self.size = size
        self.hash_table = [[] for _ in range(self.size)]
        #self.hash_table = self.create_buckets()

    #def create_buckets(self):
    #    return [[] for _ in range(self.size)]

    def set_val(self, key, value):
        pass

    def get_val(self, key):
        pass

    def __str__(self):
        return "".join(str(item) for item in self.hash_table)

hash_table = AlgoHashTable(256)
print(hash_table)





*************************************************************************************
*************************************************************************************
*************************************************************************************


class AlgoHashTable:

    def __init__(self, size):
        self.size = size
        self.hash_table = [[] for _ in range(self.size)]
        #print(self.hash_table)

    def __str__(self):
        return "".join(str(item) for item in self.hash_table)


hash_table = AlgoHashTable(256)
print(hash_table)



*************************************************************************************
*************************************************************************************
*************************************************************************************
#placing two key value pair in one list/location

class AlgoHashTable:

    def __init__(self, size):
        self.size = size
        self.hash_table = self.create_buckets()

    def create_buckets(self):
        return [[] for _ in range(self.size)]

    def set_val(self,key,value):
        hashed_key = 10 #hash(key)%self.size
        bucket = self.hash_table[hashed_key]
        bucket.append((key,value))


    def __str__(self):
        return "".join(str(item) for item in self.hash_table)


hash_table = AlgoHashTable(256)
print(hash_table)
hash_table.set_val('mashrur@example.com', 'some value')
hash_table.set_val('johndoe@example.com', 'some other value')
print(hash_table)

** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** *
** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** *
** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** *

# edit an item in the key/value pair like the way it is implemented in the dictionary DataStructure

class AlgoHashTable:

    def __init__(self, size):
        self.size = size
        self.hash_table = self.create_buckets()

    def create_buckets(self):
        return [[] for _ in range(self.size)]

    def set_val(self, key, value):
        hashed_key = 10  # hash(key)%self.size
        bucket = self.hash_table[hashed_key]
        bucket.append((key, value))

    def __str__(self):
        return "".join(str(item) for item in self.hash_table)


hash_table = AlgoHashTable(256)
print(hash_table)
hash_table.set_val('mashrur@example.com', 'some value')
hash_table.set_val('johndoe@example.com', 'some other value')
print(hash_table)



::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

the key must be an int or a str and it cannot be a list because it cannot be changed.







::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

'''
class AlgoHashTable:

    def __init__(self, size):
        self.size = size
        #self.hash_table = [[] for _ in range(self.size)]
        #print(self.hash_table)
        self.hash_table = self.create_buckets()

    def create_buckets(self):
        return [[] for _ in range(self.size)]

    def set_val(self, key, value):
        hashed_key = hash(key)%self.size
        bucket = self.hash_table[hashed_key]
        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_value = record
            if record_key == key:
                found_key = True
                break
        if found_key:
            bucket[index] = (key, value)
        else:
            bucket.append((key, value))

        bucket.append((key,value))

    def get_val(self, key):
        pass

    def __str__(self):
        #pass
        #return "Hello!"
        return "".join(str(item) for item in self.hash_table)

hash_table = AlgoHashTable(256)
print(hash_table)
hash_table.set_val('tegaslink@gmail.com','some value')
hash_table.set_val('JohnDoe@gmail.com','some other value')
print(hash_table)







records = [ ('mashrur@example.com','Hello World'),
            ('JohnDoe@example.com','Hello to you too'),
            ('Janedoe@example.com', 'Python is awesome')
          ]

for record in records:
    key, value = record    #This unpackes the tuple into key and value
    print(key, value)

for index, record in enumerate(records):
    key, value = record
    print(index,key,value,)

print(records[index])


for index, record in enumerate(records):
    key, value = record
    if key == 'JohnDoe@example.com':
        break
    print(index,key,value,)

print(records[index])