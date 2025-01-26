from RedBlackBST import RedBlackBST


def test_color_flip_small():
    """Test that 2 red flip
        5
       / \
     red red
     /     \
    4       8
    """
    # Manually build the tree so can test w/o insertion function working.
    a = RedBlackBST()
    a.insert_i(5, 5)
    a.root.left = a.RedBlackNode(4, 4)
    a.root.right = a.RedBlackNode(8, 8)

    parent_node = a.root
    a._tree_correction(parent_node)

    assert a.root.left.is_red == False
    assert a.root.right.is_red == False
    assert a.root.is_red == False


def test_simple_rotate_left():
    """Test very basic rotate left.

    A tree with just root node and insert value greater than root.
    """

    a = RedBlackBST()
    a.insert_i("C", "C")
    a.root.right = a.RedBlackNode("F", "F")
    a.root.right.parent = a.root

    parent_node = a.root
    a._tree_correction(parent_node)

    assert a.root.key == "F"
    assert a.root.is_red == False
    assert a.root.parent is None
    assert a.root.right is None

    assert a.root.left.key == "C"
    assert a.root.left.is_red
    assert a.root.left.left is None
    assert a.root.left.right is None
    assert a.root.left.parent == a.root


def test_very_simple_rotate_right():
    """Basic Right rotation
    Test when a tree only has the root and one left red link. Both nodes insert
    a value less than.
    Start:
           C
          / RED
         B
        / RED
       A
    Expected:
            B
           / \
          A   C
    """

    a = RedBlackBST()
    a.insert_i("C", "C")
    a.root.left = a.RedBlackNode("B", "B")
    a.root.left.left = a.RedBlackNode("A", "A")
    # Manually Set Parents
    a.root.left.parent = a.root
    a.root.left.left.parent = a.RedBlackNode("B", "B")

    # To test just the rotation aspect I'm setting the root as the parent node.
    # The root node is where we detect two left links. In reality we would check
    # B and then move up the tree to the root. I'll test this in the next test.
    parent_node = a.root

    a._tree_correction(parent_node)

    assert a.root.key == "B"
    assert a.root.parent is None
    assert not a.root.is_red
    assert a.root.left.key == "A"
    assert a.root.right.key == "C"

    assert a.root.left.parent.key == "B"
    assert not a.root.left.is_red
    assert a.root.left.left is None
    assert a.root.left.right is None

    assert a.root.right.parent.key == "B"
    assert not a.root.right.is_red
    assert a.root.right.left is None
    assert a.root.right.right is None
