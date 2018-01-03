class _Node(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next_node = None

    def __str__(self):
        return "'{}': '{}'".format(self.key, self.value)


# a simple hashing algorithm with acceptable collision rate
def _djb2x_hash(string):
    hash = 5381
    byte_array = string.encode('utf-8')

    for byte in byte_array:
        # the modulus keeps it 32-bit, python ints don't overflow
        hash = ((hash * 33) ^ byte) % 0x100000000

    return hash


class HashTable(object):
    def __init__(self, capacity):
        self.bucket_array = [None for i in range(capacity)]
        self.capacity = capacity

    def insert(self, key, value):
        key_hash = _djb2x_hash(key)
        bucket_index = key_hash % self.capacity

        new_node = _Node(key, value)
        existing_node = self.bucket_array[bucket_index]

        if existing_node:
            last_node = None
            while existing_node:
                if existing_node.key == key:
                    # found existing key, replace value
                    existing_node.value = value
                    return
                last_node = existing_node
                existing_node = existing_node.next_node
            # if we get this far, we didn't find an existing key
            # so just append the new node to the end of the bucket
            last_node.next_node = new_node
        else:
            self.bucket_array[bucket_index] = new_node

    def lookup(self, key):
        key_hash = _djb2x_hash(key)
        bucket_index = key_hash % self.capacity

        existing_node = self.bucket_array[bucket_index]
        if existing_node:
            while existing_node:
                if existing_node.pair.key == key:
                    return existing_node.pair.value
                existing_node = existing_node.next_node

        return None

    def delete(self, key):
        key_hash = _djb2x_hash(key)
        bucket_index = key_hash % self.capacity

        existing_node = self.bucket_array[bucket_index]
        if existing_node:
            last_node = None
            while existing_node:
                if existing_node.key == key:
                    if last_node:
                        last_node.next_node = existing_node.next_node
                    else:
                        self.bucket_array[bucket_index] = existing_node.next_node
                last_node = existing_node
                existing_node = existing_node.next_node

    def debug_print(self):
        for i in range(self.capacity):
            node = self.bucket_array[i]
            print('Bucket {}'.format(i))
            if node:
                while node:
                    print('    {}'.format(node))
                    node = node.next_node
            else:
                print('    Empty')
