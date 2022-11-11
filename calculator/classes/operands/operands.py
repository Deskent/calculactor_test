from classes.operands.base_operand import BaseOperand
from calculator.decorators.decorators import check_is_zero


class Summary(BaseOperand):
    def _calculate_element(self, elem: int | float) -> int | float:
        return sum((self.result, elem))


class Subtraction(BaseOperand):
    def _calculate_element(self, elem: int | float) -> int | float:
        return sum((self.result, -elem))


class Multiplication(BaseOperand):
    def _calculate_element(self, elem: int | float) -> int | float:
        return self.result * elem


class Pow(BaseOperand):
    def _calculate_element(self, elem: int | float) -> int | float:
        return pow(self.result, elem)


class Division(BaseOperand):

    @check_is_zero
    def _calculate_element(self, elem: int | float) -> int | float:
        return self.result / elem


class IntegerDivision(Division):

    @check_is_zero
    def _calculate_element(self, elem: int | float) -> int | float:
        return self.result // elem


class Modulo(Division):
    @check_is_zero
    def _calculate_element(self, elem: int | float) -> int | float:
        return self.result % elem
