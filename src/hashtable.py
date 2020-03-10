# '''
# Linked List hash table key/value pair
# '''


class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''

    def __init__(self, capacity):
        self.count = 0
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
        self.count += 1
        if self.count >= self.capacity:
            self.resize()
        index = self._hash_mod(key)
        new_node = LinkedPair(key, value)
        node = self.storage[index]
        if node is None:
            self.storage[index] = new_node
            return new_node.value

        # handle collision
        # iterate to end of array
        prev = node
        key_exists = False
        while node is not None:
            prev = node
            if node.key == key:
                key_exists = True
                break
            node = node.next
        if key_exists:
            node.value = value
        else:
            prev.next = new_node
        return new_node.value

    def remove(self, key):
        '''
        Remove the value stored with the given key.
        Print a warning if the key is not found.
        Fill this in.
        '''
        index = self._hash_mod(key)
        node = self.storage[index]
        prev = None
        while node is not None and node.key != key:
            prev = node
            node = node.next
        if node is None:
            return None
        else:
            self.count -= 1
            value = node.value
            if prev is None:
                self.storage[index] = None
            else:
                prev.next = prev.next.next
            return value

    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.
        Returns None if the key is not found.
        Fill this in.
        '''
        index = self._hash_mod(key)
        node = self.storage[index]
        while node is not None and node.key != key:
            node = node.next
        if node is not None:
            return node.value
        else:
            return None

    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.
        Fill this in.
        '''
        if self.count >= self.capacity:
            oldStorage = self.storage
            oldCount = self.count
            self.count = 0
            self.capacity *= 2
            self.storage = [None] * self.capacity
            for i in range(0, oldCount):
                bucket = oldStorage[i]
                if bucket is not None:
                    while bucket is not None:
                        self.insert(bucket.key, bucket.value)
                        bucket = bucket.next


if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
