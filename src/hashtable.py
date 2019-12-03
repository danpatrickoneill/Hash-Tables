# '''
# Linked List hash table key/value pair
# '''


class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def __str__(self):
        return f'{self.key}: {self.value}'


class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''

    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity

    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)

    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass

    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity

    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        index = self._hash_mod(key)
        current_node = self.storage[index]
        if current_node is None:
            self.storage[index] = LinkedPair(key, value)
        else:
            prev_node = None
            while current_node:
                if current_node.key == key:
                    current_node.value = value
                    return
                prev_node = current_node
                current_node = current_node.next
            prev_node.next = LinkedPair(key, value)

    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        if self.storage[index] is None:
            print("Key not found")
        else:
            current_node = self.storage[index]
            while current_node:

                if current_node.key == key:
                    current_node.value = None
                    return
                current_node = current_node.next
        print("Key not found")
        return

    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        if self.storage[index] is None:
            return None
        else:
            current_node = self.storage[index]

            while current_node:
                print("Line 109: ", current_node, current_node.next)
                if current_node.key == key:
                    return current_node.value
                current_node = current_node.next
            return None

    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        new_hash = HashTable(self.capacity * 2)
        for elem in self.storage:
            while elem:
                new_hash.insert(elem.key, elem.value)
                elem = elem.next
        self.capacity, self.storage = new_hash.capacity, new_hash.storage


if __name__ == "__main__":
    # ht = HashTable(2)

    # ht.insert("line_1", "Tiny hash table")
    # ht.insert("line_2", "Filled beyond capacity")
    # ht.insert("line_3", "Linked list saves the day!")

    # print("")

    # # Test storing beyond capacity
    # print(ht.retrieve("line_1"))
    # print(ht.retrieve("line_2"))
    # print(ht.retrieve("line_3"))

    # # Test resizing
    # old_capacity = len(ht.storage)
    # ht.resize()
    # new_capacity = len(ht.storage)

    # print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # # Test if data intact after resizing
    # print(ht.retrieve("line_1"))
    # print(ht.retrieve("line_2"))
    # print(ht.retrieve("line_3"))

    # print("")

    ht = HashTable(8)

    ht.insert("key-0", "val-0")
    ht.insert("key-1", "val-1")
    ht.insert("key-2", "val-2")
    ht.insert("key-3", "val-3")
    ht.insert("key-4", "val-4")
    ht.insert("key-5", "val-5")
    ht.insert("key-6", "val-6")
    ht.insert("key-7", "val-7")
    ht.insert("key-8", "val-8")
    ht.insert("key-9", "val-9")

    ht.insert("key-0", "new-val-0")
    ht.insert("key-1", "new-val-1")
    ht.insert("key-2", "new-val-2")
    ht.insert("key-3", "new-val-3")
    ht.insert("key-4", "new-val-4")
    ht.insert("key-5", "new-val-5")
    ht.insert("key-6", "new-val-6")
    ht.insert("key-7", "new-val-7")
    ht.insert("key-8", "new-val-8")
    ht.insert("key-9", "new-val-9")

    print(ht.retrieve("key-0"))
    print(ht.retrieve("key-1"))
    print(ht.retrieve("key-2"))
    print(ht.retrieve("key-3"))
    print(ht.retrieve("key-4"))
    print(ht.retrieve("key-5"))
    print(ht.retrieve("key-6"))
    print(ht.retrieve("key-7"))
    print(ht.retrieve("key-8"))
    print(ht.retrieve("key-9"))
