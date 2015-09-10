"""Check if the decorator works as it is supposed to."""
import returns


def test_wrapping_return_value_with_namedtuple():
    """Check if `custom_namedtuple` wraps a function to return a namedtuple with specified name."""
    namedtuple_name = 'TwoFields'

    @returns.namedtuple('field0', 'field1', name=namedtuple_name)
    def func(arg1, arg2):
        return arg1, arg2

    args = object(), object()
    return_value = func(*args)

    assert isinstance(return_value, tuple)
    assert type(return_value) is not tuple, 'The return value must not be a plain tuple.'
    assert type(return_value).__name__ == namedtuple_name
    assert len(return_value) == 2
    assert return_value.field0 is args[0]
    assert return_value.field1 is args[1]


def test_multiple_tuple_lengths():
    """Check if it is possible to return tuples of multiple lengths."""
    @returns.namedtuple('f1', 'f2', 'f3', name='ThreeArgs')
    def func_3_args(arg1, arg2, arg3):
        return arg1, arg2, arg3

    assert func_3_args(1, 2, 3) == (1, 2, 3)

    @returns.namedtuple('f1', 'f2', 'f3', 'f4', 'f5', name='FiveArgs')
    def func_5_args(arg1, arg2, arg3, arg4, arg5):
        return arg1, arg2, arg3, arg4, arg5

    assert func_5_args(1, 2, 3, 4, 11) == (1, 2, 3, 4, 11)


def test_default_namedtuple_name():
    """Check when the name is not given, a fallback one is creared from the function name."""
    @returns.namedtuple('f0', 'f1')
    def some_function():
        return 1, 33

    assert type(some_function()).__name__ == 'SomeFunction'
