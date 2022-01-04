

class Stack:
    def __init__(self, s):
        self.stack_size = s
        self.array = self.stack_size * [None]
        self.colected = self.stack_size * [False]
        self.stacked_elements = 0

    def size(self):
        return self.stacked_elements
    
    def empty(self):
        if self.stacked_elements == 0:
            return True
        else:
            return False

    def push(self, element):
        if self.stacked_elements < self.stack_size:
            if element < (self.stack_size - 1):
                if self.colected[element] == False:
                    self.array[self.stacked_elements] = element
                    self.colected[element] = True
                    self.stacked_elements += 1

    def pop(self):
        if self.stacked_elements > 0:
            buff = self.array[self.stacked_elements-1]
            self.colected[(int)(buff)] = False
            self.stacked_elements -= 1
            return buff


    def print(self):
        for i in range(0, self.stacked_elements):     
            print(self.array[i])


import unittest

class TestStack(unittest.TestCase):
    def setUp(self):
        self.s5 = Stack(10)

    def test_initialization(self):
        self.assertEqual(self.s5.size(), 0)

    
    def test_simple_push(self):
        s1 = Stack(20)
        for i in range(10):
            s1.push(i)
        self.assertEqual(s1.size(), 10)

    
    def test_simple_pop(self):
        s1 = Stack(5)
        s1.push(2)
        s1.push(3)
        self.assertEqual(s1.pop(), 3)
        self.assertEqual(s1.pop(), 2)
    
    def test_full_push(self):
        s1 = Stack(7)
        s1.push(4)
        s1.push(4)
        self.assertEqual(s1.size(), 1)

        s1.pop
        s1.push(2)
        self.assertEqual(s1.pop(), 2)
    
    def test_simple_is_empty(self):
        s1 = Stack(2)
        s1.push(10)
        self.assertTrue(s1.empty())
        s1.push(1)
        s1.pop
        self.assertTrue(s1.empty)
        


if __name__ == '__main__':
    unittest.main()