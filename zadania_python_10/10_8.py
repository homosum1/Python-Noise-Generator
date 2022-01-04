from random import randrange
from types import resolve_bases
from typing import List

class RandomQueue:
    class EmptyQueue(Exception):
        def __init__(self, mess="Queue is empty!"):
            self.message = mess
            super().__init__(self.message)
        
    class FullQueue(Exception):
        def __init__(self, mess="Queue is full!"):
            self.message = mess
            super().__init__(self.message)
    
    class Node:
        def __init__(self, dat = None):
            self.next_free_index = -1
            self.data = dat

    def __init__(self, s):
        self.queue_size = s
        self.array = self.queue_size * [None]

        self.queued_elements = 0
        self.first_free_index = 0
        self.last_free_index = self.queue_size-1

        self.initialize()
      
    def initialize(self):
        for i in range(0,self.queue_size):
            self.array[i] = self.Node()
            
        for i in range(0,self.queue_size-1):
            self.array[i].next_free_index = i+1
        


    def insert(self, element):
        if self.queued_elements < self.queue_size:
            #print("first free: " + str(self.first_free_index))
            index = self.array[self.first_free_index].next_free_index
            self.array[self.first_free_index] = self.Node(element)
            self.first_free_index = index
    
            self.queued_elements += 1
        else:
            raise self.FullQueue()


    # zwraca losowy element
    def remove(self):
        if self.queued_elements > 0:
            random_num = randrange(self.queue_size)
            while self.array[random_num].data == None:
                # print("val: " + str(self.array[random_num].data) + " index: " + str(random_num) )
                random_num = randrange(self.queue_size)
            
            # test
            if self.queued_elements != self.queue_size:
              
                self.array[self.last_free_index].next_free_index = random_num
                self.last_free_index = random_num
            
            else:
                self.first_free_index = random_num
                self.last_free_index = random_num

            self.queued_elements -= 1
            
            value = self.array[random_num].data
            self.array[random_num].data = None
            self.array[random_num].next_free_index = -1

            return value
        else:
            raise self.EmptyQueue() 

    def is_empty(self):
        if self.queued_elements == 0:
            return True
        else:
            return False

    def is_full(self):
        if self.queued_elements == self.queue_size:
            return True
        else:
            return False

    def clear(self):
        self.queued_elements = 0
        self.tail = 0

    def size(self):
        return self.queued_elements
    
    def print(self):
        print("\nvalues:")
        for i in range(0, self.queue_size):
            print(self.array[i].data)

    def print_free_indexes(self):
        print("\nnext free indexes:")
        for i in range(0, self.queue_size):
            print(self.array[i].next_free_index)
        print("first free index: " + str(self.first_free_index))


import unittest

class TestStack(unittest.TestCase):
    
    def test_insert(self):
        rq1 = RandomQueue(10)

        rq1.insert(10)
        self.assertEqual(rq1.size(), 1)

        for i in range (9):
            rq1.insert(i)
        
        self.assertEqual(rq1.size(), 10)
    
    def test_remove(self):
        rq2 = RandomQueue(5)
        
        for i in range (5):
            rq2.insert(i)
        
        rq2.print()
        print("removed: " + str(rq2.remove()))
        self.assertEqual(rq2.size(), 4)
        print("removed: " + str(rq2.remove()))
        self.assertEqual(rq2.size(), 3)
        rq2.print()
        rq2.print_free_indexes()
        rq2.insert(30)
        rq2.print()
        rq2.print_free_indexes()
        rq2.insert(50)
        rq2.print()
        results = []
        for i in range(4):
            results.append(rq2.remove())

        self.assertEqual(len(results), 4)

    def test_is_empty_full(self):
        rq3 = RandomQueue(3)
        rq3.insert(1)
        rq3.print()
        rq3.remove()
        self.assertTrue(rq3.is_empty())
        self.assertFalse(rq3.is_full())


if __name__ == '__main__':
    unittest.main()