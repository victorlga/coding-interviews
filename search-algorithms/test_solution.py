from contextlib import contextmanager
from functools import wraps
from io import StringIO
import sys
import solution


# SETUP

# Decorate functions

def count_calls(func):
    @wraps(func)
    def decorator(*args, **kwargs):
        decorator.calls += 1
        return func(*args, **kwargs)
    
    decorator.calls = 0

    return decorator

solution.pre_order_recursive = count_calls(solution.pre_order_recursive)
solution.pre_order_iterative = count_calls(solution.pre_order_iterative)
solution.in_order_recursive = count_calls(solution.in_order_recursive)
solution.post_order_recursive = count_calls(solution.post_order_recursive)
solution.breadth_first = count_calls(solution.breadth_first)
solution.graph_depth_first_iterative = count_calls(solution.graph_depth_first_iterative)
solution.graph_depth_first_recursive = count_calls(solution.graph_depth_first_recursive)
solution.graph_breadth_first = count_calls(solution.graph_breadth_first)


# INITIALIZATION FUNCTIONS

def build_perfect_tree():
    r'''
    Builds the following tree:

               __________0__________
              /                     \
         ____1____               ____2____
        /         \             /         \
      _3_         _4_         _5_         _6_
     /   \       /   \       /   \       /   \
    7     8     9    10    11    12    13    14
    '''
    return solution.Tree(list(range(15)))


def build_unbalanced_tree():
    r'''
    Builds the following tree:

      ______________________0______________________
     /                                             \
    1__________                           __________2__________
               \                         /                     \
                3____                   4____                   5____
                     \                       \                       \
                     _6_                     _7_                     _8
                    /   \                   /   \                   /
                   9    10                11    12                13
    '''
    description = [
                                                                0,
                                    1,                                                       2,
                   None,                            3,                         4,                         5,
           None,           None,           None,          6,          None,          7,           None,          8,
        None, None,     None, None,     None, None,     9, 10,     None, None,     11, 12,     None, None,     13
    ]
    return solution.Tree(description)


def build_full_graph():
    '''
    Builds the following graph (this is the adjacency matrix - 1 = True, 0 = False):
    '''
    adjacency = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    ]
    return solution.Graph(adjacency)


def build_sparse_graph():
    '''
    Builds the following graph (this is the adjacency matrix - 1 = True, 0 = False):
    '''
    adjacency = [
       # 1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 1
        [0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 2
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 3
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 4
        [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 5
        [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],  # 6
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 7
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],  # 8
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],  # 9
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],  # 10
        [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],  # 11
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],  # 12
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],  # 13
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],  # 14
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],  # 15
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 16
    ]
    return solution.Graph(adjacency)

# TEST TOOLS

@contextmanager
def stored_stdout():
    old = sys.stdout
    new = StringIO()
    try:
        sys.stdout = new
        yield new
    finally:
        sys.stdout = old


def assert_recursive(func, recursive):
    if recursive:
        assert func.calls > 1, 'Function should be recursive.'
    else:
        assert func.calls == 1, 'Function should be iterative. Called {0} times.'.format(func.calls)


def apply_test(func, expected, recursive, *func_args):
    func.calls = 0
    with stored_stdout() as stdout:
        func(*func_args)
    printed = []
    tokens = stdout.getvalue().strip().split()
    for t in tokens:
        try:
            printed.append(int(t))
        except ValueError:
            print(f'Could not convert "{t}" to int')

    assert_recursive(func, recursive)
    assert printed == expected, f'Expected order: {expected}. Printed order: {printed}'


def apply_test_tree(func, expected, with_perfect_tree, recursive):
    if with_perfect_tree:
        tree = build_perfect_tree()
    else:
        tree = build_unbalanced_tree()
    apply_test(func, expected, recursive, tree.root)


def apply_test_graph(func, expected, with_full_graph, recursive):
    if with_full_graph:
        graph = build_full_graph()
    else:
        graph = build_sparse_graph()
    apply_test(func, expected, recursive, graph.nodes[0])



# PRE-ORDER

def test_pre_order_recursive_perfect_tree():
    expected = [0, 1, 3, 7, 8, 4, 9, 10, 2, 5, 11, 12, 6, 13, 14]
    apply_test_tree(solution.pre_order_recursive, expected, True, True)


def test_pre_order_recursive_unbalanced_tree():
    expected = [0, 1, 3, 6, 9, 10, 2, 4, 7, 11, 12, 5, 8, 13]
    apply_test_tree(solution.pre_order_recursive, expected, False, True)


def test_pre_order_iterative_perfect_tree():
    expected = [0, 1, 3, 7, 8, 4, 9, 10, 2, 5, 11, 12, 6, 13, 14]
    apply_test_tree(solution.pre_order_iterative, expected, True, False)


def test_pre_order_iterative_unbalanced_tree():
    expected = [0, 1, 3, 6, 9, 10, 2, 4, 7, 11, 12, 5, 8, 13]
    apply_test_tree(solution.pre_order_iterative, expected, False, False)


# IN-ORDER

def test_in_order_recursive_perfect_tree():
    expected = [7, 3, 8, 1, 9, 4, 10, 0, 11, 5, 12, 2, 13, 6, 14]
    apply_test_tree(solution.in_order_recursive, expected, True, True)


def test_in_order_recursive_unbalanced_tree():
    expected = [1, 3, 9, 6, 10, 0, 4, 11, 7, 12, 2, 5, 13, 8]
    apply_test_tree(solution.in_order_recursive, expected, False, True)


# POST-ORDER

def test_post_order_recursive_perfect_tree():
    expected = [7, 8, 3, 9, 10, 4, 1, 11, 12, 5, 13, 14, 6, 2, 0]
    apply_test_tree(solution.post_order_recursive, expected, True, True)


def test_post_order_recursive_unbalanced_tree():
    expected = [9, 10, 6, 3, 1, 11, 12, 7, 4, 13, 8, 5, 2, 0]
    apply_test_tree(solution.post_order_recursive, expected, False, True)


# BREADTH FIRST

def test_breadth_first_perfect_tree():
    expected = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    apply_test_tree(solution.breadth_first, expected, True, False)


def test_breadth_first_unbalanced_tree():
    expected = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    apply_test_tree(solution.breadth_first, expected, False, False)


# DEPTH FIRST GRAPH

def test_depth_first_full_graph_recursive():
    expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    apply_test_graph(solution.graph_depth_first_recursive, expected, True, True)


def test_depth_first_sparse_graph_recursive():
    expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    apply_test_graph(solution.graph_depth_first_recursive, expected, False, True)


def test_depth_first_full_graph_iterative():
    expected = [1, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2]
    apply_test_graph(solution.graph_depth_first_iterative, expected, True, False)


def test_depth_first_sparse_graph_iterative():
    expected = [1, 2, 5, 6, 8, 9, 10, 12, 13, 16, 14, 15, 11, 7, 3, 4]
    apply_test_graph(solution.graph_depth_first_iterative, expected, False, False)


# BREADTH FIRST GRAPH

def test_breadth_first_full_graph():
    expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    apply_test_graph(solution.graph_breadth_first, expected, True, False)


def test_breadth_first_sparse_graph():
    expected = [1, 2, 3, 5, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16, 15]
    apply_test_graph(solution.graph_breadth_first, expected, False, False)
