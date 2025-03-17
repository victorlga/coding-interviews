import ast
from contextlib import contextmanager
import inspect
from io import StringIO
import math
import random
import string
import sys
import solution


################################################################################
# TEST TOOLS
################################################################################
@contextmanager
def stored_stdout():
    old = sys.stdout
    new = StringIO()
    try:
        sys.stdout = new
        yield new
    finally:
        sys.stdout = old


def randlist(size, minval=-100, maxval=100):
    return [random.randint(minval, maxval) for _ in range(size)]


def randstr(size):
    return ''.join([random.choice(string.ascii_letters) for _ in range(size)])


# AST STUFF
def visit_source_ast(function, visit):
    source = inspect.getsource(function)
    function_ast = ast.parse(source)
    for node in ast.walk(function_ast):
        if visit(node):
            return True
    return False


def instance_visitor(expected_type):
    return lambda node: isinstance(node, expected_type)


def uses_subscript(function):
    return visit_source_ast(function, instance_visitor(ast.Subscript))


def uses_list_comp(function):
    return visit_source_ast(function, instance_visitor(ast.ListComp))


def uses_set_comp(function):
    return visit_source_ast(function, instance_visitor(ast.SetComp))


def uses_dict_comp(function):
    return visit_source_ast(function, instance_visitor(ast.DictComp))


def uses_ternary_if(function):
    return visit_source_ast(function, instance_visitor(ast.IfExp))


def uses_unpacking(function):
    return visit_source_ast(
        function,
        lambda node: isinstance(node, ast.Assign) and hasattr(node, 'targets') and type(node.targets[0]) in (ast.Tuple, ast.List)
    )


def uses_global(function, *var_names):
    return visit_source_ast(
        function,
        lambda node: isinstance(node, ast.Global) and all(var_name in node.names for var_name in var_names)
    )


def calls_function(function, function_name):
    return visit_source_ast(
        function,
        lambda node: isinstance(node, ast.Call) and hasattr(node.func, 'id') and node.func.id == function_name
    )


def count_lines(function):
    source = inspect.getsource(function)
    lines = [l.strip() for l in source.split('\n')]
    lines = [l for l in lines if l and not l.startswith('#')]
    return len(lines)


################################################################################
# TEST FUNCTIONS
################################################################################

def test_print_indices_and_elements():
    total = 10
    elements = randlist(total)
    with stored_stdout() as stdout:
        solution.print_indices_and_elements(elements)

    lines = [l.strip() for l in stdout.getvalue().split('\n') if l.strip()]
    assert len(lines) == total, f'There should be exactly one print per element. Expected: {total}. Got: {len(lines)}.'
    idx = 0
    for line in lines:
        expected = f'{idx} {elements[idx]}'
        assert line == expected, f'Wrong output. Expected: {expected}. Got: {line}.'
        idx += 1

    assert calls_function(solution.print_indices_and_elements, 'enumerate'), f'Did not call function enumerate'
    assert not uses_subscript(solution.print_indices_and_elements), f'Used subscript (e.g. elements[i]) to access elements'


def assert_get_even_numbers_works():
    start = random.randint(10, 100)
    end = start + random.randint(20, 50)
    even_numbers = solution.get_even_numbers_between(start, end)
    expected = []
    for n in range(start, end + 1):
        if n % 2 == 0:
            expected.append(n)

    assert expected == even_numbers, f'get_even_numbers returned the wrong list. Expected: {expected}. Got: {even_numbers}.'
    assert uses_list_comp(solution.get_even_numbers_between), 'get_even_numbers should be implemented using a list comprehension.'


def assert_get_char_set_works():
    s = randstr(random.randint(10, 30))
    char_set = solution.get_char_set_from(s)
    expected = set()
    for c in s:
        expected.add(c)

    assert expected == char_set, f'get_char_set returned the wrong set. Expected: {expected}. Got: {char_set}.'
    assert uses_set_comp(solution.get_char_set_from), 'get_char_set should be implemented using a set comprehension.'


def assert_get_perfect_squares_works():
    start = random.randint(10, 100)
    end = start + random.randint(1000, 2000)
    perfect_squares = solution.get_perfect_squares_between(start, end)
    expected = {}
    for i in range(int(math.sqrt(start)), int(math.sqrt(end)) + 1):
        if start <= i**2 <= end:
            expected[i**2] = i

    assert expected == perfect_squares, f'get_perfect_squares returned the wrong dict. Expected: {expected}. Got: {perfect_squares}.'
    assert uses_dict_comp(solution.get_perfect_squares_between), 'get_perfect_squares should be implemented using a dict comprehension.'


def test_comprehensions():
    assert_get_even_numbers_works()
    assert_get_char_set_works()
    assert_get_perfect_squares_works()


def test_filter_even():
    numbers = randlist(random.randint(50, 100))
    expected = []
    for n in numbers:
        if n % 2 == 0:
            expected.append(n)

    even = solution.filter_even_from(numbers.copy())
    assert expected == even, f'filter_even_from returned the wrong list for input {numbers}. Expected: {expected}. Got: {even}.'
    assert uses_list_comp(solution.filter_even_from), 'filter_even_from should be implemented using a list comprehension.'


def test_get_number_or_minus_one():
    even = random.randint(1000, 2000)
    odd = even + 1
    if even % 2 == 1:
        even, odd = odd, even

    arg_answers = [(even, even), (odd, -1)]
    for n, expected in arg_answers:
        ans = solution.get_number_or_minus_one(n)
        assert expected == ans, f'get_number_or_minus_one returned the wrong answer for n={n}. Expected: {expected}. Got: {ans}.'
    assert uses_ternary_if(solution.get_number_or_minus_one), f'get_number_or_minus_one should be implemented using the ternary if expression.'
    line_count = count_lines(solution.get_number_or_minus_one)
    assert line_count == 2, f'get_number_or_minus_one should be implemented using a single line. Used: {line_count - 1}.'


def test_transform_multiples_of_5():
    numbers = randlist(random.randint(50, 100))
    expected = []
    for n in numbers:
        if n % 5 == 0:
            if n % 2 == 0:
                expected.append(n)
            else:
                expected.append(-1)

    transformed = solution.transform_multiples_of_5(numbers.copy())
    assert expected == transformed, f'transform_multiples_of_5 returned the wrong answer for input {numbers}. Expected: {expected}. Got: {transformed}.'
    assert uses_ternary_if(solution.transform_multiples_of_5), f'transform_multiples_of_5 should be implemented using the ternary if expression.'
    assert uses_list_comp(solution.transform_multiples_of_5), f'transform_multiples_of_5 should be implemented using list comprehension.'
    line_count = count_lines(solution.transform_multiples_of_5)
    assert line_count == 2, f'transform_multiples_of_5 should be implemented using a single line. Used: {line_count - 1}.'


def test_str_lengths():
    expected = randlist(random.randint(50, 100), 5, 20)
    strings = [randstr(l) for l in expected]
    lengths = solution.str_lengths(strings)

    assert lengths == expected, f'str_lengths returned the wrong answer for list {strings}. Expected: {expected}. Got: {lengths}.'
    assert uses_list_comp(solution.str_lengths), f'str_lengths should be implemented using list comprehension.'


def test_get_fibonacci_type():
    assert 'generator' in solution.get_fibonacci_type(1), f'get_fibonacci_type(1) returned the wrong type for fibonacci1(6).'
    assert 'list' in solution.get_fibonacci_type(2), f'get_fibonacci_type(2) returned the wrong type for fibonacci2(6).'
    assert not calls_function(solution.get_fibonacci_type, 'type'), f'get_fibonacci_type should not use function type. You should run it outside the function and paste the result as the returned string.'


def test_difference_between_fibonacci1_and_fibonacci2():
    answer = solution.difference_between_fibonacci1_and_fibonacci2()
    assert type(answer) == str, f'difference_between_fibonacci1_and_fibonacci2 should return a string.'
    assert len(answer) > 20, f'difference_between_fibonacci1_and_fibonacci2 probably does not contain a good answer, since it is too short.'


def test_skip_iterator():
    numbers = randlist(random.randint(50, 100))
    iterator = solution.SkipIterator(numbers)
    result = list(iterator)
    expected = numbers[::2]

    assert expected == result


def test_my_avg():
    n = 5
    numbers = randlist(n)
    for i in range(2, n+1):
        elements = numbers[:i]
        expected = sum(elements) / i
        avg = solution.my_avg(*elements)
        assert expected == avg, f'my_avg returned the wrong answer for numbers {", ".join(elements)}. Expected: {expected}. Got: {avg}.'


def test_keys_with_different_value():
    a = dict(zip(range(10), range(10)))
    b = dict(zip(range(5, 15), range(15, 25)))
    c = {**a, **b}
    d = {**b, **a}
    expected = sorted([k for k, vc in c.items() if vc != d[k]])
    ans = solution.keys_with_different_value()
    assert expected == ans, 'keys_with_different_value returned the wrong answer.'


def test_print_out_in():
    n = random.randint(5, 50)
    if n % 2 == 1:
        n = n + 1
    even_pairs = randlist(n)
    odd_pairs = randlist(n + 1)

    inputs = [
        (even_pairs, [
            f'{even_pairs[i]} {even_pairs[n - i - 1]}'
            for i in range(n // 2)
        ]),
        (odd_pairs, [
            f'{odd_pairs[i]} {odd_pairs[n - i]}'
            for i in range(n // 2)
        ] + [f'{odd_pairs[n // 2]}']),
    ]

    for numbers, expected in inputs:
        with stored_stdout() as stdout:
            solution.print_out_in(*numbers)

        lines = [l.strip() for l in stdout.getvalue().split('\n') if l.strip()]
        numbers_str = ", ".join(str(i) for i in numbers)
        expected_str = "\n".join(expected)
        got_str = "\n".join(lines)
        msg = f'Wrong answer for numbers {numbers_str}.\nExpected:\n{expected_str}\nGot:{got_str}'
        assert expected == lines, msg

    assert uses_unpacking(solution.print_out_in), 'print_out_in should use tuple unpacking'


def test_append_range():
    start = random.randint(10, 20)

    for i in range(random.randint(5, 10)):
        end = start + i
        r1 = solution.append_range(start, end)
        r2 = solution.append_range(start, end, to=[])

        suffix = {1: 'st', 2: 'nd', 3: 'rd'}.get(i, 'th')
        assert r1 == r2, f'Results are different for append_range using start={start} and end={end} in the {i}{suffix} loop'

    signature = inspect.signature(solution.append_range)
    source = inspect.getsource(solution.append_range)
    assert len(signature.parameters) == 4, "You shouldn't modify the number of arguments or their names in append_range"
    assert 'to' in signature.parameters, "Couldn't find the parameter 'to' in append_range"
    assert 'for i in range(start, end, step):\n        to.append(i)\n    return to' in source, "Shouldn't modify the for loop in append_range"
    assert signature.parameters['to'].default is None, "The default value of argument 'to' should be None in append_range"


def test_global_var_func():
    assert inspect.getsource(solution.global_var_func1) == 'def global_var_func1(n: int):\n    for i in range(n):\n        print(global_var)\n', "You shouldn't modify the function global_var_func1"
    assert uses_global(solution.global_var_func2, 'global_var'), 'Problem is not fixed in function global_var_func2'


def test_value_is_None():
    class ComparableThing:
        def __eq__(self, other):
            return True

    assert not solution.value_is_None(ComparableThing()), "Function value_is_None didn't work for argument that is not None"
    assert solution.value_is_None(None), "Function value_is_None didn't work for argument None"
