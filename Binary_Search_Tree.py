class Binary_Search_Tree:
  # TODO.I have provided the public method skeletons. You will need
  # to add private methods to support the recursive algorithms
  # discussed in class

  class __BST_Node:
    # TODO The Node class is private. You may add any attributes and
    # methods you need. Recall that attributes in an inner class 
    # must be public to be reachable from the the methods.

    def __init__(self, value):
      self.value = value
      # TODO complete Node initialization

      self.left = None
      self.right = None
      self.height=1

  def __init__(self):
    self.__root = None
    # TODO complete initialization

  def current_node_height(self, current_node):
    if current_node is None:
        return 0
    elif current_node.right is None and current_node.left is None:
      return 1
    elif current_node.right is None and current_node.left is not None:
      return current_node.left.height+1
    elif current_node.left is None and current_node.right is not None:
      return current_node.right.height+1
    else:
      return max(current_node.left.height,current_node.right.height)+1

  def insert_element(self, value):
    # Insert the value specified into the tree at the correct
    # location based on "less is left; greater is right" binary
    # search tree ordering. If the value is already contained in
    # the tree, raise a ValueError. Your solution must be recursive.
    # This will involve the introduction of additional private
    # methods to support the recursion control variable.
    #pass # TODO replace pass with your implementation

    new_node=self.__BST_Node(value)
    if self.get_height() == 0:
      self.__root = new_node
    else: # This implies the height is NOT None which means the tree is populated
      self.__root = self.__recursive_insert_element(self.__root, value) # new_node is either the left or right of the current_node   


  def __recursive_insert_element(self, current_node, value):
    if current_node is None:
        new_node=self.__BST_Node(value)
        return new_node
    if value==current_node.value:
      raise ValueError
    if value<current_node.value:
        current_node.left=self.__recursive_insert_element(current_node.left, value)
    if value>current_node.value:
        current_node.right=self.__recursive_insert_element(current_node.right, value)
    current_node.height=self.current_node_height(current_node)
    # return current_node
    return self.__balance(current_node)

  def remove_element(self, value):
    # Remove the value specified from the tree, raising a ValueError
    # if the value isn't found. When a replacement value is necessary,
    # select the minimum value to the from the right as this element's
    # replacement. Take note of when to move a node reference and when
    # to replace the value in a node instead. It is not necessary to
    # return the value (though it would reasonable to do so in some 
    # implementations). Your solution must be recursive. 
    # This will involve the introduction of additional private
    # methods to support the recursion control variable.
    #pass # TODO replace pass with your implementation
    if self.__root==None:
      raise ValueError("Cannot remove something from nothing")
    else:
      self.__root=self.__recursive_remove_element(self.__root, value)

  def __recursive_remove_element(self, current_node, value):
    if current_node is None:
      raise ValueError
    elif current_node.value==value:
      if current_node.right is None and current_node.left is None:
        return None
      elif current_node.right is None and current_node.left is not None:
        return current_node.left
      elif current_node.left is None and current_node.right is not None:
        return current_node.right
      elif current_node.left is not None and current_node.right is not None:
        smallest_node=self.__find_min_node(current_node.right)
        current_node.value=smallest_node.value
        current_node.right=self.__recursive_remove_element(current_node.right, smallest_node.value)
    elif current_node.value>value:
      current_node.left=self.__recursive_remove_element(current_node.left, value)
    elif current_node.value<value:
      current_node.right=self.__recursive_remove_element(current_node.right, value)
    current_node.height=self.current_node_height(current_node)
    # return current_node
    return self.__balance(current_node)

  def __find_min_node(self, subroot):
    if subroot.left is None:
      return subroot
    else:
      return self.__find_min_node(subroot.left)

  def in_order(self):
    # Construct and return a string representing the in-order
    # traversal of the tree. Empty trees should be printed as [ ].
    # Trees with one value should be printed as [ 4 ]. Trees with more
    # than one value should be printed as [ 4, 7 ]. Note the spacing.
    # Your solution must be recursive. This will involve the introduction
    # of additional private methods to support the recursion control 
    # variable.
    #pass # TODO replace pass with your implementation
    
    root=self.__root
    if self.get_height() == 0:
      return "[ ]"
    return '[ ' + str(self.__in_order_recursion(root))[1:-1] + ' ]'

  def __in_order_recursion(self, current_root):
    list = []
    if current_root is not None:
        list = self.__in_order_recursion(current_root.left) 
        list.append(current_root.value)
        list += self.__in_order_recursion(current_root.right)
    return list

  def pre_order(self):
    # Construct and return a string representing the pre-order
    # traversal of the tree. Empty trees should be printed as [ ].
    # Trees with one value should be printed in as [ 4 ]. Trees with
    # more than one value should be printed as [ 4, 7 ]. Note the spacing.
    # Your solution must be recursive. This will involve the introduction
    # of additional private methods to support the recursion control 
    # variable.
    #pass # TODO replace pass with your implementation

    root=self.__root
    if self.get_height() == 0:
      return "[ ]"
    return '[ ' + str(self.__pre_order_recursion(root))[1:-1] + ' ]'

  def __pre_order_recursion(self, current_root):
    list = []
    if current_root is not None:
        list.append(current_root.value)
        list += self.__pre_order_recursion(current_root.left)
        list += self.__pre_order_recursion(current_root.right)
    return list

  def post_order(self):
    # Construct an return a string representing the post-order
    # traversal of the tree. Empty trees should be printed as [ ].
    # Trees with one value should be printed in as [ 4 ]. Trees with
    # more than one value should be printed as [ 4, 7 ]. Note the spacing.
    # Your solution must be recursive. This will involve the introduction
    # of additional private methods to support the recursion control 
    # variable.
    #pass # TODO replace pass with your implementation

    root=self.__root
    if self.get_height() == 0:
      return "[ ]"
    return '[ ' + str(self.__post_order_recursion(root))[1:-1] + ' ]'

  def __post_order_recursion(self, current_root):
    list = []
    if current_root is not None:
        list += self.__post_order_recursion(current_root.left)
        list += self.__post_order_recursion(current_root.right)
        list.append(current_root.value)
    return list

  def to_list(self):
    root=self.__root
    return self.__to_list_recursion(root)

  def __to_list_recursion(self, current_root):
    list = []
    if current_root is not None:
        list = self.__to_list_recursion(current_root.left) 
        list.append(current_root.value)
        list += self.__to_list_recursion(current_root.right)
    return list
    
  def get_height(self):
    # return an integer that represents the height of the tree.
    # assume that an empty tree has height 0 and a tree with one
    # node has height 1. This method must operate in constant time.
    #pass # TODO replace pass with your implementation

    if self.__root is None:
      return 0
    else:
      return self.__root.height

  def __str__(self):
    return self.in_order()

  def __balance(self, subroot):
    balance_subroot = self.__getBal(subroot)
    balance_subroot_left = self.__getBal(subroot.left)
    balance_subroot_right= self.__getBal(subroot.right)

    if subroot is None:
      return None
    elif balance_subroot==0 or balance_subroot==-1 or balance_subroot==1:
      return subroot
    elif balance_subroot==-2:
      if balance_subroot_left<=0:
        subroot=self.__rRotate(subroot)
        return subroot
      elif balance_subroot_left>0:
        subroot.left=self.__lRotate(subroot.left)
        subroot=self.__rRotate(subroot)
        return subroot
    elif balance_subroot==2:
      if balance_subroot_right>=0:
        subroot=self.__lRotate(subroot)
        return subroot
      elif balance_subroot_right<0:
        subroot.right=self.__rRotate(subroot.right)
        subroot=self.__lRotate(subroot)
        return subroot

  def __lRotate(self, subroot):

    y = subroot.right
    floater = y.left

    y.left=subroot
    y.left.right=floater

    y.left.height = self.current_node_height(y.left)

    y.height = self.current_node_height(y)

    return y

  def __rRotate(self, subroot):

    y = subroot.left
    floater = y.right

    y.right = subroot
    y.right.left = floater

    y.right.height = self.current_node_height(y.right)
    
    y.height = self.current_node_height(y)

    return y

  def __getBal(self, root):
    if root is None:
      return 0

    return self.current_node_height(root.right) - self.current_node_height(root.left)

if __name__ == '__main__':
  bst = Binary_Search_Tree()
  pass
 