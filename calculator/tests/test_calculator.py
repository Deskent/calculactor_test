import pytest
from classes.calculator import Calculator


@pytest.mark.parametrize('arguments, result', [
    ((10, 5), 5),
    ((10, 3, 2), 5),
])
def test_subtraction(arguments, result):
    spam = Calculator.get('-')
    assert spam(*arguments) == result


@pytest.mark.parametrize('arguments, result', [
    ((2, 3), 5),
    ((2, 3, 5), 10),
])
def test_summa(arguments, result):
    spam = Calculator.get('+')
    assert spam(*arguments) == result


@pytest.mark.parametrize('arguments, result', [
    ((2, 3), 6),
    ((2, 3, 4), 24),
])
def test_multiplication(arguments, result):
    spam = Calculator.get('*')
    assert spam(*arguments) == result


@pytest.mark.parametrize('arguments, result', [
    ((2, 3), 8),
    ((2, 2, 2), 16),
])
def test_pow(arguments, result):
    spam = Calculator.get('**')
    assert spam(*arguments) == result


@pytest.mark.parametrize('arguments, result', [
    ((10, 2), 5),
    ((20, 2, 2), 5),
])
def test_division(arguments, result):
    spam = Calculator.get('/')
    assert spam(*arguments) == result


@pytest.mark.parametrize('arguments, result', [
    ((10, 2), 5),
    ((20, 2, 2), 5),
])
def test_integer_division(arguments, result):
    spam = Calculator.get('//')
    assert spam(*arguments) == result


@pytest.mark.parametrize('arguments, result', [
    ((10, 2), 0),
    ((15, 2, 2), 1),
])
def test_modulo(arguments, result):
    spam = Calculator.get('%')
    assert spam(*arguments) == result


@pytest.mark.parametrize('operands', ['/', '//', '%'])
def test_division_zero(operands):
    spam = Calculator.get(operands)
    with pytest.raises(ZeroDivisionError):
        assert spam(10, 0)


def test_no_digit():
    spam = Calculator.get('+')
    with pytest.raises(TypeError):
        assert spam('5', 3)


def test_wrong_operation():
    with pytest.raises(KeyError):
        assert Calculator.get('(')

