def print_indices_and_elements(elements) -> None:
    for i, e in enumerate(elements):
        print(i, e)


def get_even_numbers_between(start: int, end: int) -> list[int]:
    return [ n for n in range(start, end+1) if n % 2 == 0 ]


def get_char_set_from(s: str) -> set[str]:
    return { c for c in s if c.isalpha() }


def get_perfect_squares_between(start: int, end: int) -> dict[int,int]:
    return { n: int(n**0.5) for n in range(start, end) if (n**0.5).is_integer() }


def filter_even_from(numbers: list[int]) -> list[int]:
    return [ n for n in numbers if n % 2 == 0 ]


def get_number_or_minus_one(n: int) -> int:
    return n if n % 2 == 0 else -1


def transform_multiples_of_5(numbers: list[int]) -> list[int]:
    return [ -1 if n % 2 != 0 else n for n in numbers if n % 5 == 0 ]


def str_lengths(strings: list[str]) -> list[int]:
    return [ len(s) for s in strings ]


def get_fibonacci_type(version: int) -> str:
    return 'generator' if version == 1 else 'list'


def difference_between_fibonacci1_and_fibonacci2() -> str:
    return """  fibonacci1 is a generator, which means it yields values one at a time and does not store the entire sequence in memory.
                fibonacci2, on the other hand, computes all Fibonacci numbers up to n and stores them in a list.
                While fibonacci1 saves memory by generating values lazily, fibonacci2 allows random access to all computed values.
            """



class SkipIterator:
    def __init__(self, elements):
        self.elements = elements
        self.i = -2
    
    def __iter__(self):
        return self

    def __next__(self):
        self.i += 2
        if self.i >= len(self.elements):
            raise StopIteration()
        return self.elements[self.i]

        

def my_avg(e1: float, e2: float, *others: tuple[float]) -> float:
    total = e1 + e2 + sum(others)
    count = 2 + len(others)
    return total / count


def keys_with_different_value() -> list[int]:
    a = dict(zip(range(10), range(10)))
    b = dict(zip(range(5, 15), range(15, 25)))
    return sorted([ k for k in set(a) & set(b) if a.get(k) != b.get(k) ])


def print_out_in(*numbers) -> None:
    while len(numbers) > 1:
        a, *numbers, b = numbers
        print(a, b)

    if numbers:
        print(*numbers)


def append_range(start: int, end: int, step: int=1, to: list[int]=None):
    # You may add code here
    if to is None:
        to = []
    # Don't change the code below
    for i in range(start, end, step):
        to.append(i)
    return to


global_var = 10

def global_var_func1(n: int):
    for i in range(n):
        print(global_var)


def global_var_func2(n: int):
    global global_var
    for i in range(n):
        global_var += i
        print(global_var)


def value_is_None(value):
    return value is None