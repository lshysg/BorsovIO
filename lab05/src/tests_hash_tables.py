from hash_table_chaining import HashTableChaining
from hash_table_open_addressing import HashTableOpenAddressing

print("=== Тест цепочек ===")
ht = HashTableChaining()
ht.insert("a", 1)
ht.insert("b", 2)
ht.insert("a", 3)
print(ht.get("a"))  # 3
print(ht.get("b"))  # 2

print("=== Тест линейного пробирования ===")
ht2 = HashTableOpenAddressing(method="linear")
ht2.insert("a", 10)
ht2.insert("b", 20)
print(ht2.get("a"))
print(ht2.get("b"))

print("=== Тест double hashing ===")
ht3 = HashTableOpenAddressing(method="double")
ht3.insert("hello", 100)
ht3.insert("world", 200)
print(ht3.get("hello"))
print(ht3.get("world"))
