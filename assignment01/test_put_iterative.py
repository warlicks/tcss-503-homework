from RedBlackBST import RedBlackBST


def test_insert_root_gt():
    """Test node is placed correctly when key is greater than root."""
    a = RedBlackBST()
    a.insert_i(5, 5)
    new_node = a.RedBlackNode(8, 8)

    parent_node = a._insertion_search(new_node)
    a._put_i(parent_node, new_node)

    assert a.root.right == new_node
    assert a.root.right.is_red


def test_insert_root_lt():
    """Test node is placed correctly when key is less than root."""
    a = RedBlackBST()
    a.insert_i(5, 5)
    new_node = a.RedBlackNode(2, 2)

    parent_node = a._insertion_search(new_node)
    a._put_i(parent_node, new_node)

    assert a.root.left == new_node
    assert a.root.left.is_red


def test_insert_root_eq():
    """Test node value is updated if keys are the same."""
    a = RedBlackBST()
    a.insert_i(5, 5)
    new_node = a.RedBlackNode(5, 2)

    parent_node = a._insertion_search(new_node)
    a._put_i(parent_node, new_node)

    assert a.root.value == 2


def test_deeper_lt_insert():
    """test insertion of 4 with following tree.
         5
        /
       2
    Should end up to right of 2.

    This is really testing that search and put work together correctly when
    more than just the root.
    """
    a = RedBlackBST()
    a.insert_i(5, 5)
    a.root.left = a.RedBlackNode(2, 2)
    new_node = a.RedBlackNode(4, 4)

    parent_node = a._insertion_search(new_node)
    a._put_i(parent_node, new_node)

    assert a.root.left.right == new_node
    assert a.root.left.right.is_red


def test_deeper_lt_insert():
    """test insertion of 1 with following tree.
         5
        /
       2
    Should end up to left of 2.

    This is really testing that search and put work together correctly when
    more than just the root.
    """
    a = RedBlackBST()
    a.insert_i(5, 5)
    a.root.left = a.RedBlackNode(2, 2)
    new_node = a.RedBlackNode(1, 1)

    parent_node = a._insertion_search(new_node)
    a._put_i(parent_node, new_node)

    assert a.root.left.left == new_node
    assert a.root.left.left.is_red
