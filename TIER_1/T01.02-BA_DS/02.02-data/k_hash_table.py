class HashTable:
    def __init__(self):
        self.table = {}

    def add(self, key):
        hash_value = hash(key)
        self.table[hash_value] = key


    def __repr__(self):
        return str(self.table)

# key1 = "example"
# hash_value1 = hash(key1)
# print(hash_value1)  # -4049593035154628903
# hash_table[hash_value1] = key1

# key2 = "another example"
# hash_value2 = hash(key2)
# print(hash_value2)  # 5109324920784817575
# hash_table[hash_value2] = key2

hash_table=HashTable()
hash_table.add("example")
hash_table.add("another example")

print(hash_table)  # {5109324920784817575: 'another example', -4049593035154628903: 'example'}
hash_table.add("example")
print(hash_table)  # {5109324920784817575: 'another example', -4049593035154628903: 'example'}