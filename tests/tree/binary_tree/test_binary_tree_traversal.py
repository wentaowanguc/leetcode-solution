from solutions.tree.binary_tree import BinaryTreeNode

import pytest

@pytest.fixture
def single_node_tree():
    root = BinaryTreeNode(1)
    return root

@pytest.fixture
def tree_with_left_child():
    root = BinaryTreeNode(1)
    root.left = BinaryTreeNode(2)
    return root

@pytest.fixture
def tree_with_right_child():
    root = BinaryTreeNode(1)
    root.right = BinaryTreeNode(2)
    return root

@pytest.fixture
def tree_with_both_children():
    root = BinaryTreeNode(1)
    root.left = BinaryTreeNode(2)
    root.right = BinaryTreeNode(3)
    return root

@pytest.fixture
def empty_tree():
    return None


def test_empty_tree_traversal(empty_tree):
    assert BinaryTreeNode.pre_order_traversal(empty_tree) == []
    assert BinaryTreeNode.post_order_traversal(empty_tree) == []
    assert BinaryTreeNode.in_order_traversal(empty_tree) == []


def test_single_node_tree_traversal(single_node_tree):
    assert BinaryTreeNode.pre_order_traversal(single_node_tree) == [1]
    assert BinaryTreeNode.post_order_traversal(single_node_tree) == [1]
    assert BinaryTreeNode.in_order_traversal(single_node_tree) == [1]


def test_tree_with_left_child_traversal(tree_with_left_child):
    assert BinaryTreeNode.pre_order_traversal(tree_with_left_child) == [1, 2]
    assert BinaryTreeNode.post_order_traversal(tree_with_left_child) == [2, 1]
    assert BinaryTreeNode.in_order_traversal(tree_with_left_child) == [2, 1]


def test_tree_with_right_child_traversal(tree_with_right_child):
    assert BinaryTreeNode.pre_order_traversal(tree_with_right_child) == [1, 2]
    assert BinaryTreeNode.post_order_traversal(tree_with_right_child) == [2, 1]
    assert BinaryTreeNode.in_order_traversal(tree_with_right_child) == [1, 2]


def test_tree_with_both_children_traversal(tree_with_both_children):
    assert BinaryTreeNode.pre_order_traversal(tree_with_both_children) == [1, 2, 3]
    assert BinaryTreeNode.post_order_traversal(tree_with_both_children) == [2, 3, 1]
    assert BinaryTreeNode.in_order_traversal(tree_with_both_children) == [2, 1, 3]