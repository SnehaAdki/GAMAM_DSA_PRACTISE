# DP
# https://leetcode.com/problems/lru-cache/?source=submission-ac
# 146. LRU Cache
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

# Implement the LRUCache class:

# LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
# int get(int key) Return the value of the key if the key exists, otherwise return -1.
# void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
# The functions get and put must each run in O(1) average time complexity.

 

# Example 1:

# Input
# ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
# [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
# Output
# [null, null, null, 1, null, -1, null, -1, 3, 4]

# Explanation
# LRUCache lRUCache = new LRUCache(2);
# lRUCache.put(1, 1); // cache is {1=1}
# lRUCache.put(2, 2); // cache is {1=1, 2=2}
# lRUCache.get(1);    // return 1
# lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
# lRUCache.get(2);    // returns -1 (not found)
# lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
# lRUCache.get(1);    // return -1 (not found)
# lRUCache.get(3);    // return 3
# lRUCache.get(4);    // return 4



class Node():
    def __init__(self,key,val):
        self.prev = None
        self.next = None
        self.key = key
        self.val = val

class LRU():
    def __init__(self,capacity):
        self.capacity = capacity
        self.hash_map = {}
        self.head = Node(-1,-1)
        self.tail = Node(-1,-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self,node):
        prev,later = node.prev,node.next
        prev.next = node.next
        later.prev = node.prev

    def get(self,key):
        if key in self.hash_map.keys():
            self.remove(self.hash_map[key])
            self.insert(self.hash_map[key])
            node = self.hash_map[key]
            return node.val
        return -1

    def insert(self,node):
        prev,later = self.head,self.head.next
        prev.next = later.prev = node
        node.next = later
        node.prev = prev
        

    def put(self,key,val):
        if key in self.hash_map:
            self.remove(self.hash_map[key])
        self.hash_map[key] = Node(key,val)
        self.insert(self.hash_map[key])

        if self.capacity < len(self.hash_map):
            lru = self.tail.prev
            self.remove(lru)
            del self.hash_map[lru.key]
