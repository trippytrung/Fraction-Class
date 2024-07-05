import unittest
from Binary_Search_Tree import *


class BSTTester(unittest.TestCase):
  
  def setUp(self):
    self.__BST = Binary_Search_Tree()

  def test_remove_from_empty_tree(self):
    with self.assertRaises(ValueError):
      self.__BST.remove_element(50)
    self.assertEqual('[ ]', str(self.__BST))

  def test_remove_nonexistant_from_tree(self):
    with self.assertRaises(ValueError):
      self.__BST.insert_element(50)
      self.__BST.remove_element(49)
    self.assertEqual("[ 50 ]", str(self.__BST))

  def test_insert_duplicate_int0_tree(self):
    with self.assertRaises(ValueError):
      self.__BST.insert_element(50)
      self.__BST.insert_element(50)
    self.assertEqual("[ 50 ]", str(self.__BST))

  def test_to_list(self):
    self.__BST.insert_element(50)
    self.__BST.insert_element(70)
    self.__BST.insert_element(10)
    self.__BST.insert_element(20)
    self.__BST.insert_element(90)
    self.assertEqual([10, 20, 50, 70, 90], self.__BST.to_list())

    
#--------------------------

  def test_empty_tree(self):
    self.assertEqual('[ ]', str(self.__BST), 'Empty list should print as "[ ]"')
    self.assertEqual(0, self.__BST.get_height())
    self.assertEqual("[ ]", self.__BST.in_order())
    self.assertEqual("[ ]", self.__BST.pre_order())
    self.assertEqual("[ ]", self.__BST.post_order())

  def test_one_tree(self):
    self.__BST.insert_element(50)
    self.assertEqual('[ 50 ]', str(self.__BST))
    self.assertEqual(1, self.__BST.get_height())
    self.assertEqual("[ 50 ]", self.__BST.in_order())
    self.assertEqual("[ 50 ]", self.__BST.pre_order())
    self.assertEqual("[ 50 ]", self.__BST.post_order())

  def test_oneMinusOne_tree(self):
    self.__BST.insert_element(50)
    self.__BST.remove_element(50)
    self.assertEqual('[ ]', str(self.__BST))
    self.assertEqual(0, self.__BST.get_height())
    self.assertEqual("[ ]", self.__BST.in_order())
    self.assertEqual("[ ]", self.__BST.pre_order())
    self.assertEqual("[ ]", self.__BST.post_order())

  def test_twoA_tree(self):
    self.__BST.insert_element(50)
    self.__BST.insert_element(30)
    self.assertEqual('[ 30, 50 ]', str(self.__BST))
    self.assertEqual(2, self.__BST.get_height())
    self.assertEqual("[ 30, 50 ]", self.__BST.in_order())
    self.assertEqual("[ 50, 30 ]", self.__BST.pre_order())
    self.assertEqual("[ 30, 50 ]", self.__BST.post_order())

  def test_twoB_tree(self):
    self.__BST.insert_element(30)
    self.__BST.insert_element(50)
    self.assertEqual('[ 30, 50 ]', str(self.__BST))
    self.assertEqual(2, self.__BST.get_height())
    self.assertEqual("[ 30, 50 ]", self.__BST.in_order())
    self.assertEqual("[ 30, 50 ]", self.__BST.pre_order())
    self.assertEqual("[ 50, 30 ]", self.__BST.post_order())

  def test_twoMinusOneA_tree(self):
    self.__BST.insert_element(50)
    self.__BST.insert_element(70)
    self.__BST.remove_element(70)
    self.assertEqual('[ 50 ]', str(self.__BST))
    self.assertEqual(1, self.__BST.get_height())
    self.assertEqual("[ 50 ]", self.__BST.in_order())
    self.assertEqual("[ 50 ]", self.__BST.pre_order())
    self.assertEqual("[ 50 ]", self.__BST.post_order())

  def test_twoMinusOneB_tree(self):
    self.__BST.insert_element(50)
    self.__BST.insert_element(70)
    self.__BST.remove_element(50)
    self.assertEqual('[ 70 ]', str(self.__BST))
    self.assertEqual(1, self.__BST.get_height())
    self.assertEqual("[ 70 ]", self.__BST.in_order())
    self.assertEqual("[ 70 ]", self.__BST.pre_order())
    self.assertEqual("[ 70 ]", self.__BST.post_order())

  def test_twoMinusOneC_tree(self):
    self.__BST.insert_element(50)
    self.__BST.insert_element(30)
    self.__BST.remove_element(30)
    self.assertEqual('[ 50 ]', str(self.__BST))
    self.assertEqual(1, self.__BST.get_height())
    self.assertEqual("[ 50 ]", self.__BST.in_order())
    self.assertEqual("[ 50 ]", self.__BST.pre_order())
    self.assertEqual("[ 50 ]", self.__BST.post_order())

  def test_twoMinusOneD_tree(self):
    self.__BST.insert_element(50)
    self.__BST.insert_element(30)
    self.__BST.remove_element(50)
    self.assertEqual('[ 30 ]', str(self.__BST))
    self.assertEqual(1, self.__BST.get_height())
    self.assertEqual("[ 30 ]", self.__BST.in_order())
    self.assertEqual("[ 30 ]", self.__BST.pre_order())
    self.assertEqual("[ 30 ]", self.__BST.post_order())
#---------------------
  def test_threeA_tree(self):
    self.__BST.insert_element(70)
    self.__BST.insert_element(50)
    self.__BST.insert_element(30)
    self.assertEqual('[ 30, 50, 70 ]', str(self.__BST))
    self.assertEqual(2, self.__BST.get_height())
    self.assertEqual("[ 30, 50, 70 ]", self.__BST.in_order())
    self.assertEqual("[ 50, 30, 70 ]", self.__BST.pre_order())
    self.assertEqual("[ 30, 70, 50 ]", self.__BST.post_order())

  def test_threeB_tree(self):
    self.__BST.insert_element(70)
    self.__BST.insert_element(30)
    self.__BST.insert_element(50)
    self.assertEqual('[ 30, 50, 70 ]', str(self.__BST))
    self.assertEqual(2, self.__BST.get_height())
    self.assertEqual("[ 30, 50, 70 ]", self.__BST.in_order())
    self.assertEqual("[ 50, 30, 70 ]", self.__BST.pre_order())
    self.assertEqual("[ 30, 70, 50 ]", self.__BST.post_order())

  def test_threeC_tree(self):
    self.__BST.insert_element(50)
    self.__BST.insert_element(30)
    self.__BST.insert_element(70)
    self.assertEqual('[ 30, 50, 70 ]', str(self.__BST))
    self.assertEqual(2, self.__BST.get_height())
    self.assertEqual("[ 30, 50, 70 ]", self.__BST.in_order())
    self.assertEqual("[ 50, 30, 70 ]", self.__BST.pre_order())
    self.assertEqual("[ 30, 70, 50 ]", self.__BST.post_order())

  def test_threeD_tree(self):
    self.__BST.insert_element(50)
    self.__BST.insert_element(70)
    self.__BST.insert_element(30)
    self.assertEqual('[ 30, 50, 70 ]', str(self.__BST))
    self.assertEqual(2, self.__BST.get_height())
    self.assertEqual("[ 30, 50, 70 ]", self.__BST.in_order())
    self.assertEqual("[ 50, 30, 70 ]", self.__BST.pre_order())
    self.assertEqual("[ 30, 70, 50 ]", self.__BST.post_order())

  def test_threeE_tree(self):
    self.__BST.insert_element(30)
    self.__BST.insert_element(50)
    self.__BST.insert_element(70)
    self.assertEqual('[ 30, 50, 70 ]', str(self.__BST))
    self.assertEqual(2, self.__BST.get_height())
    self.assertEqual("[ 30, 50, 70 ]", self.__BST.in_order())
    self.assertEqual("[ 50, 30, 70 ]", self.__BST.pre_order())
    self.assertEqual("[ 30, 70, 50 ]", self.__BST.post_order())

  def test_threeF_tree(self):
    self.__BST.insert_element(30)
    self.__BST.insert_element(70)
    self.__BST.insert_element(50)
    self.assertEqual('[ 30, 50, 70 ]', str(self.__BST))
    self.assertEqual(2, self.__BST.get_height())
    self.assertEqual("[ 30, 50, 70 ]", self.__BST.in_order())
    self.assertEqual("[ 50, 30, 70 ]", self.__BST.pre_order())
    self.assertEqual("[ 30, 70, 50 ]", self.__BST.post_order())

#-------------------------

  def test_fiveA_tree(self):
    self.__BST.insert_element(50)
    self.__BST.insert_element(30)
    self.__BST.insert_element(70)
    self.__BST.insert_element(20)
    self.__BST.insert_element(10)
    self.assertEqual('[ 10, 20, 30, 50, 70 ]', str(self.__BST))
    self.assertEqual(3, self.__BST.get_height())
    self.assertEqual("[ 10, 20, 30, 50, 70 ]", self.__BST.in_order())
    self.assertEqual("[ 50, 20, 10, 30, 70 ]", self.__BST.pre_order())
    self.assertEqual("[ 10, 30, 20, 70, 50 ]", self.__BST.post_order())

  def test_fiveB_tree(self):
    self.__BST.insert_element(50)
    self.__BST.insert_element(30)
    self.__BST.insert_element(70)
    self.__BST.insert_element(10)
    self.__BST.insert_element(20)
    self.assertEqual('[ 10, 20, 30, 50, 70 ]', str(self.__BST))
    self.assertEqual(3, self.__BST.get_height())
    self.assertEqual("[ 10, 20, 30, 50, 70 ]", self.__BST.in_order())
    self.assertEqual("[ 50, 20, 10, 30, 70 ]", self.__BST.pre_order())
    self.assertEqual("[ 10, 30, 20, 70, 50 ]", self.__BST.post_order())

  def test_fiveC_tree(self):
    self.__BST.insert_element(50)
    self.__BST.insert_element(30)
    self.__BST.insert_element(70)
    self.__BST.insert_element(80)
    self.__BST.insert_element(90)
    self.assertEqual('[ 30, 50, 70, 80, 90 ]', str(self.__BST))
    self.assertEqual(3, self.__BST.get_height())
    self.assertEqual("[ 30, 50, 70, 80, 90 ]", self.__BST.in_order())
    self.assertEqual("[ 50, 30, 80, 70, 90 ]", self.__BST.pre_order())
    self.assertEqual("[ 30, 70, 90, 80, 50 ]", self.__BST.post_order())

  def test_fiveD_tree(self):
    self.__BST.insert_element(50)
    self.__BST.insert_element(30)
    self.__BST.insert_element(70)
    self.__BST.insert_element(90)
    self.__BST.insert_element(80)
    self.assertEqual('[ 30, 50, 70, 80, 90 ]', str(self.__BST))
    self.assertEqual(3, self.__BST.get_height())
    self.assertEqual("[ 30, 50, 70, 80, 90 ]", self.__BST.in_order())
    self.assertEqual("[ 50, 30, 80, 70, 90 ]", self.__BST.pre_order())
    self.assertEqual("[ 30, 70, 90, 80, 50 ]", self.__BST.post_order())

#------------------------------

  def test_sixA_tree(self):
    self.__BST.insert_element(50)
    self.__BST.insert_element(30)
    self.__BST.insert_element(70)
    self.__BST.insert_element(20)
    self.__BST.insert_element(40)
    self.__BST.insert_element(10)
    self.assertEqual('[ 10, 20, 30, 40, 50, 70 ]', str(self.__BST))
    self.assertEqual(3, self.__BST.get_height())
    self.assertEqual("[ 10, 20, 30, 40, 50, 70 ]", self.__BST.in_order())
    self.assertEqual("[ 30, 20, 10, 50, 40, 70 ]", self.__BST.pre_order())
    self.assertEqual("[ 10, 20, 40, 70, 50, 30 ]", self.__BST.post_order())

  def test_sixB_tree(self):
    self.__BST.insert_element(50)
    self.__BST.insert_element(30)
    self.__BST.insert_element(70)
    self.__BST.insert_element(60)
    self.__BST.insert_element(80)
    self.__BST.insert_element(90)
    self.assertEqual('[ 30, 50, 60, 70, 80, 90 ]', str(self.__BST))
    self.assertEqual(3, self.__BST.get_height())
    self.assertEqual("[ 30, 50, 60, 70, 80, 90 ]", self.__BST.in_order())
    self.assertEqual("[ 70, 50, 30, 60, 80, 90 ]", self.__BST.pre_order())
    self.assertEqual("[ 30, 60, 50, 90, 80, 70 ]", self.__BST.post_order())

  def test_sixC_tree(self):
    self.__BST.insert_element(50)
    self.__BST.insert_element(30)
    self.__BST.insert_element(70)
    self.__BST.insert_element(20)
    self.__BST.insert_element(40)
    self.__BST.insert_element(35)
    self.assertEqual('[ 20, 30, 35, 40, 50, 70 ]', str(self.__BST))
    self.assertEqual(3, self.__BST.get_height())
    self.assertEqual("[ 20, 30, 35, 40, 50, 70 ]", self.__BST.in_order())
    self.assertEqual("[ 40, 30, 20, 35, 50, 70 ]", self.__BST.pre_order())
    self.assertEqual("[ 20, 35, 30, 70, 50, 40 ]", self.__BST.post_order())

#6.10-6.12 is bad

  def test_sixMinusOneA_tree(self):
    self.__BST.insert_element(60)
    self.__BST.insert_element(50)
    self.__BST.insert_element(70)
    self.__BST.insert_element(30)
    self.__BST.insert_element(65)
    self.__BST.insert_element(80)
    self.__BST.remove_element(80)
    self.assertEqual('[ 30, 50, 60, 65, 70 ]', str(self.__BST))
    self.assertEqual(3, self.__BST.get_height())
    self.assertEqual("[ 30, 50, 60, 65, 70 ]", self.__BST.in_order())
    self.assertEqual("[ 60, 50, 30, 70, 65 ]", self.__BST.pre_order())
    self.assertEqual("[ 30, 50, 65, 70, 60 ]", self.__BST.post_order())

  def test_sixMinusThreeA_tree(self):
    self.__BST.insert_element(60)
    self.__BST.insert_element(50)
    self.__BST.insert_element(70)
    self.__BST.insert_element(30)
    self.__BST.insert_element(65)
    self.__BST.insert_element(80)
    self.__BST.remove_element(80)
    self.__BST.remove_element(50)
    self.__BST.remove_element(30)
    self.assertEqual('[ 60, 65, 70 ]', str(self.__BST))
    self.assertEqual(2, self.__BST.get_height())
    self.assertEqual("[ 60, 65, 70 ]", self.__BST.in_order())
    self.assertEqual("[ 65, 60, 70 ]", self.__BST.pre_order())
    self.assertEqual("[ 60, 70, 65 ]", self.__BST.post_order())

  def test_sixMinusOneB_tree(self):
    self.__BST.insert_element(60)
    self.__BST.insert_element(50)
    self.__BST.insert_element(70)
    self.__BST.insert_element(30)
    self.__BST.insert_element(55)
    self.__BST.insert_element(80)
    self.__BST.remove_element(30)
    self.__BST.remove_element(70)
    self.__BST.remove_element(80)
    self.assertEqual('[ 50, 55, 60 ]', str(self.__BST))
    self.assertEqual(2, self.__BST.get_height())
    self.assertEqual("[ 50, 55, 60 ]", self.__BST.in_order())
    self.assertEqual("[ 55, 50, 60 ]", self.__BST.pre_order())
    self.assertEqual("[ 50, 60, 55 ]", self.__BST.post_order())

  def test_sixMinusOneC_tree(self):
    self.__BST.insert_element(60)
    self.__BST.insert_element(50)
    self.__BST.insert_element(70)
    self.__BST.insert_element(30)
    self.__BST.insert_element(65)
    self.__BST.insert_element(80)
    self.__BST.remove_element(65)
    self.__BST.remove_element(50)
    self.__BST.remove_element(30)
    self.assertEqual('[ 60, 70, 80 ]', str(self.__BST))
    self.assertEqual(2, self.__BST.get_height())
    self.assertEqual("[ 60, 70, 80 ]", self.__BST.in_order())
    self.assertEqual("[ 70, 60, 80 ]", self.__BST.pre_order())
    self.assertEqual("[ 60, 80, 70 ]", self.__BST.post_order())

  def test_sixMinusOneD_tree(self):
    self.__BST.insert_element(60)
    self.__BST.insert_element(50)
    self.__BST.insert_element(70)
    self.__BST.insert_element(30)
    self.__BST.insert_element(55)
    self.__BST.insert_element(80)
    self.__BST.remove_element(55)
    self.__BST.remove_element(70)
    self.__BST.remove_element(80)
    self.assertEqual('[ 30, 50, 60 ]', str(self.__BST))
    self.assertEqual(2, self.__BST.get_height())
    self.assertEqual("[ 30, 50, 60 ]", self.__BST.in_order())
    self.assertEqual("[ 50, 30, 60 ]", self.__BST.pre_order())
    self.assertEqual("[ 30, 60, 50 ]", self.__BST.post_order())

  def test_sixMinusOneB_tree(self):
    self.__BST.insert_element(60)
    self.__BST.insert_element(50)
    self.__BST.insert_element(70)
    self.__BST.insert_element(30)
    self.__BST.insert_element(55)
    self.__BST.insert_element(80)
    self.__BST.remove_element(60)
    self.assertEqual('[ 30, 50, 55, 70, 80 ]', str(self.__BST))
    self.assertEqual(3, self.__BST.get_height())
    self.assertEqual("[ 30, 50, 55, 70, 80 ]", self.__BST.in_order())
    self.assertEqual("[ 70, 50, 30, 55, 80 ]", self.__BST.pre_order())
    self.assertEqual("[ 30, 55, 50, 80, 70 ]", self.__BST.post_order())

  def test_sixMinusTwoA_tree(self):
    self.__BST.insert_element(60)
    self.__BST.insert_element(50)
    self.__BST.insert_element(70)
    self.__BST.insert_element(30)
    self.__BST.insert_element(55)
    self.__BST.insert_element(80)
    self.__BST.remove_element(60)
    self.__BST.remove_element(70)
    self.assertEqual('[ 30, 50, 55, 80 ]', str(self.__BST))
    self.assertEqual(3, self.__BST.get_height())
    self.assertEqual("[ 30, 50, 55, 80 ]", self.__BST.in_order())
    self.assertEqual("[ 50, 30, 80, 55 ]", self.__BST.pre_order())
    self.assertEqual("[ 30, 55, 80, 50 ]", self.__BST.post_order())


 


if __name__ == '__main__':
  unittest.main()