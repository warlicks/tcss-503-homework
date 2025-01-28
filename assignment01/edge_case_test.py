from RedBlackBST import RedBlackBST


def test_empty_tree():
    a = RedBlackBST()
    assert a.search(10) is None


def test_methods_same():
    """Test that we get the same output with iterative as recursive."""
    a = RedBlackBST()
    b = RedBlackBST()

    for i in ["E", "A", "B", "C", "G", "D"]:
        a.insert_i(i, i)
        b.insert_r(i, i)

    assert a.root.key == b.root.key
    assert a.root.left.key == b.root.left.key
    assert a.root.left.is_red == b.root.left.is_red

    assert a.root.right.key == b.root.right.key
    assert a.root.right.is_red == b.root.right.is_red

    assert a.root.left.right.key == b.root.left.right.key
    assert a.root.left.right.is_red == b.root.left.right.is_red

    assert a.root.left.right.left.key == b.root.left.right.left.key
    assert a.root.left.right.left.is_red == b.root.left.right.left.is_red

    assert a.root.left.left.key == b.root.left.left.key
    assert a.root.left.left.is_red == b.root.left.left.is_red
