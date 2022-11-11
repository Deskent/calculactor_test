from classes.operands import *


class Calculator:
    """Factory for getting instance using calculate operation

    Methods
        get

        add

        update

        delete
    """

    __OPERANDS: dict[str, BaseOperand] = {
        '+': Summary,
        '-': Subtraction,
        '*': Multiplication,
        '**': Pow,
        '/': Division,
        '//': IntegerDivision,
        '%': Modulo
    }

    @classmethod
    def get(cls, command: str) -> BaseOperand:
        """Return instance for operand"""

        operand: BaseOperand = cls.__OPERANDS.get(command)
        if not operand:
            raise KeyError(f'Operation {command} not supported')

        return operand(command)

    @classmethod
    def add(cls, operand: str, operator: BaseOperand) -> None:
        """Add operand and its operator to operands storage"""

        if operand in cls.__OPERANDS:
            raise KeyError(f'Operand {operand} exists')
        cls.__OPERANDS[operand] = operator

    @classmethod
    def update(cls, operand: str, operator: BaseOperand) -> None:
        """Update operand with operator"""

        cls.__OPERANDS.update({operand: operator})

    @classmethod
    def delete(cls, operand: str) -> None:
        """Delete operand from storage"""

        if operand in cls.__OPERANDS:
            del cls.__OPERANDS[operand]
