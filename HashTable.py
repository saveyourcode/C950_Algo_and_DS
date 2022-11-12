
start_empty = "EMPTY_SINCE_START"
removal_empty = "EMPTY_AFTER_REMOVAL"

# The object that is stored in the hash table; it contains the package id and the package object
class KV_Pair:

    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return f"{self.key}, {self.value}"

# O(n)
# Contains the methods of the linear probing hash table class
class LinearProbingHashTable:

    def __init__(self, initial_capacity=40):
        self.table = initial_capacity * [KV_Pair("EMPTY_SINCE_START", None)]

    # O(n) time complexity
    # Attempts to insert a package into the hash table list at the index derived from hashing the package
    # id and if that index is occupied each subsequent index is checked until an empty index is found.
    def insert(self, package_id, package):
        bucket = hash(package_id) % len(self.table)
        buckets_probed = 0
        while buckets_probed < len(self.table):
            if self.table[bucket].key == start_empty or self.table[bucket] == removal_empty:
                self.table[bucket] = KV_Pair(package_id, package)
                return True

        bucket = (bucket + 1) % len(self.table)
        buckets_probed += 1

        return False

    # O(n)
    # Searches the hash table at the index derived from hashing the package id and then checks each
    # subsequent index if the package id of the first checked index doesn't match and then deletes the
    # hash table entry when the matching id is found.
    def remove(self, package_id):
        bucket = hash(package_id) % len(self.table)
        buckets_probed = 0
        while self.table[bucket].key is not start_empty and buckets_probed < len(self.table):
            if self.table[bucket].key == package_id:
                self.table[bucket].key = removal_empty
                return True

            bucket = (bucket + 1) % len(self.table)
            buckets_probed += 1

        return False

    # O(n)
    # Searches the hash table at the index derived from hashing the package id and then checks each
    # subsequent index if the package id of the first checked index doesn't match and then returns the
    # package when the matching id is found.
    def search(self, package_id):
        bucket = hash(package_id) % len(self.table)
        buckets_probed = 0
        while self.table[bucket].key is not start_empty and buckets_probed < len(self.table):
            if self.table[bucket].key == package_id:
                return self.table[bucket].value

            bucket = (bucket + 1) % len(self.table)
            buckets_probed += 1

        return False



