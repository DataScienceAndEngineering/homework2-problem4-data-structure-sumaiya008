# coding: utf-8
import unittest
from hw2linklisted import LinkedList

class TestLinkList(unittest.TestCase):
    def test_empty_construct(self):
        "This tests the LinkList __init__ empty constructor"
        self.llist = LinkedList()
        self.assertEqual(self.llist.count,0)
        self.assertEqual(self.llist.head,None)

    def test_single_construct(self):
        "This tests the LinkList __init__ single argument constructor"
        self.llist = LinkedList(88)
        self.assertEqual(self.llist.count,1)
        self.assertEqual(self.llist.head.value,88)
        self.assertEqual(self.llist.head.next,None)
        
    def test_multiple_construct(self):
        "This tests the LinkList __init__ multiple argument constructor"
        self.llist = LinkedList(0,88,2)
        self.assertEqual(self.llist.count,3)
        self.assertEqual(self.llist.head.value,0)
        self.assertEqual(self.llist.head.next.value,88)
        self.assertEqual(self.llist.head.next.next.value,2)
        
    def test_prepend(self):
        "This tests the LinkList prepend method"
        self.llist = LinkedList()
        self.assertEqual(self.llist.head, None)
        self.assertEqual(self.llist.count, 0)
        self.llist.prepend(88)
        self.assertEqual(self.llist.head.value,88)
        self.assertEqual(self.llist.count,1)
        self.llist.prepend(100)
        self.assertEqual(self.llist.head.value,100)
        self.assertEqual(self.llist.count,2)        
   
    def test_getitem(self):
        "This tests the LinkList __getitem__ method"
        self.llist = LinkedList(798,9,200)
        self.assertEqual(self.llist[0],798)
        self.assertEqual(self.llist[1],9)
        self.assertEqual(self.llist[2],200)
        with self.assertRaises(Exception):
            self.llist[3]
        
    def test_insert_value_at(self):
        self.llist = LinkedList(798,9,200)
        self.llist.insert_value_at(99,0)
        self.assertEqual(self.llist[0],99)
        self.assertEqual(self.llist[1],798)
        self.assertEqual(self.llist[2],9)
        self.assertEqual(self.llist[3],200)
        self.llist.insert_value_at(77,3)
        self.assertEqual(self.llist[1],798)
        self.assertEqual(self.llist[2],9)
        self.assertEqual(self.llist[3],77)
        self.assertEqual(self.llist[4],200)
        self.llist.insert_value_at(8,5)
        self.assertEqual(self.llist[1],798)
        self.assertEqual(self.llist[2],9)
        self.assertEqual(self.llist[3],77)
        self.assertEqual(self.llist[4],200)        
        self.assertEqual(self.llist[5],8)
        with self.assertRaises(Exception):
            self.llist.insert_value_at(2,7)

    def test_delete_at(self):
        self.llist = LinkedList(798,9,200)
        self.assertEqual(self.llist.delete_at(1),True)
        self.assertEqual(self.llist.count,2)
        self.assertEqual(self.llist[0],798)
        self.assertEqual(self.llist[1],200)
        with self.assertRaises(Exception):
            self.llist.delete_at(2)
    
    def test_remove_first(self):
        self.llist = LinkedList(798,9,200)
        self.assertEqual(self.llist.remove_first(200),True)
        self.assertEqual(self.llist.count,2)
        self.assertEqual(self.llist[1],9) 
        self.assertEqual(self.llist.remove_first(10),False)
        self.assertEqual(self.llist.count,2)
        
    def test_pop(self):
        self.llist = LinkedList(798,9,200)
        self.assertEqual(self.llist.pop(),798)
        self.assertEqual(list(self.llist),[9,200])
        self.assertEqual(self.llist.pop(),9)
        self.assertEqual(list(self.llist),[200])        
        self.assertEqual(self.llist.pop(),200)
        self.assertEqual(list(self.llist),[])       
        with self.assertRaises(Exception):
            self.llist.pop()
            
    def test_iter(self):
        self.llist = LinkedList()
        self.assertEqual(list(self.llist),[])
        self.llist = LinkedList(67,88,42)
        self.assertEqual(list(self.llist),[67,88,42])

    def test_len(self):
        self.llist = LinkedList()
        self.assertEqual(len(self.llist),0)
        self.llist = LinkedList(8)
        self.assertEqual(len(self.llist),1)
        self.llist = LinkedList(7,15)
        self.assertEqual(len(self.llist),2)
        self.llist = LinkedList(15,37,43,51)
        self.assertEqual(len(self.llist),4)
    
    def test_repr(self):
        self.llist = LinkedList(15,37,43,51)
        self.assertEqual(str(self.llist),'LinkedList(15,37,43,51)')
        
