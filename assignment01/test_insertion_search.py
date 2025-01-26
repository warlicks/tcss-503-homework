from RedBlackBST import RedBlackBST


def test_insert_search_root():
    """Test that the root is returned when it's the only value in tree"""
    a = RedBlackBST()
    a.insert_i(5, 5)

    assert a._insertion_search(a.RedBlackNode(4, 4)).key == 5


def test_insert_search_left():
    """Test that the root is with 2 values
      5
     /
    4
    """
    # Manually build the tree so can test w/o insertion function working.
    a = RedBlackBST()
    a.insert_i(5, 5)
    a.root.left = a.RedBlackNode(4, 4)

    assert a._insertion_search(a.RedBlackNode(6, 6)).key == 5
    assert a._insertion_search(a.RedBlackNode(2, 2)).key == 4


def test_insert_search_right():
    """Test that the root is with 2 values
      5
       \
        6
    If we search where to place 8, we should get 6.
    If we search where to put 4 we should get 5
    """
    # Manually build the tree so can test w/o insertion function working.
    a = RedBlackBST()
    a.insert_i(5, 5)
    a.root.right = a.RedBlackNode(6, 6)

    assert a._insertion_search(a.RedBlackNode(8, 8)).key == 6
    assert a._insertion_search(a.RedBlackNode(4, 4)).key == 5


def test_deeper_insert_search_left():
    """Test height 3 on left.
       5
      / \
     4   6
    /
    2
    If we search where to place 3, we should get 2 node
    """
    # Manually build the tree so can test w/o insertion function working.
    a = RedBlackBST()
    a.insert_i(5, 5)
    a.root.right = a.RedBlackNode(6, 6)
    a.root.left = a.RedBlackNode(4, 4)
    a.root.left.left = a.RedBlackNode(2, 2)

    assert a._insertion_search(a.RedBlackNode(3, 3)).key == 2


def test_deeper_insert_search_right():
    """Test search with tree 3 deep.
        5
       / \
      4   6
     /     \
    2       8
    If we search where to place 3, we should get 2 node
    """
    # Manually build the tree so can test w/o insertion function working.
    a = RedBlackBST()
    a.insert_i(5, 5)
    a.root.right = a.RedBlackNode(6, 6)
    a.root.right.right = a.RedBlackNode(8, 8)
    a.root.left = a.RedBlackNode(4, 4)
    a.root.left.left = a.RedBlackNode(2, 2)

    assert a._insertion_search(a.RedBlackNode(7, 7)).key == 8


def test_deeper_still_insert_search_left():
    """Test Tree with height 4
         5
        / \
       4   6
      /
     2
      \
       3
    If we search where to place 1, we should get 2 node
    """
    # Manually build the tree so can test w/o insertion function working.
    a = RedBlackBST()
    a.insert_i(5, 5)
    a.root.right = a.RedBlackNode(6, 6)
    a.root.left = a.RedBlackNode(4, 4)
    a.root.left.left = a.RedBlackNode(2, 2)
    a.root.left.left.right = a.RedBlackNode(3, 3)

    assert a._insertion_search(a.RedBlackNode(1, 1)).key == 2
