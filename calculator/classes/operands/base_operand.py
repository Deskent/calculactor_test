from abc import abstractmethod, ABC


class BaseOperand(ABC):
    """Base class for math operands

    Attributes

        operand: str

    """

    def __init__(self, operand: str) -> None:
        self.__operand: str = operand
        self.__data: tuple = tuple()
        self.__result: int | float = 0

    def __str__(self) -> str:
        expression = f' {self.operand} '.join(map(str, self.data))

        return f'{expression} = {self.result}'

    def __call__(self, *args) -> float:
        if not args:
            raise ValueError('Must be one parameter at least')
        self.data: tuple = args
        self.result: int | float = args[0]
        self._calculate()

        return self.result

    def _calculate(self) -> None:
        """Calculate operations for all elements in args"""

        for elem in self.data[1:]:
            if not isinstance(elem, (int, float)):
                raise TypeError('Arguments must be digits: float or int')
            self.result = self._calculate_element(elem)

    @abstractmethod
    def _calculate_element(self, elem: int | float) -> int | float:
        raise NotImplementedError

    @property
    def operand(self) -> str:
        return self.__operand

    @property
    def result(self) -> int | float:
        return self.__result

    @result.setter
    def result(self, value: int | float) -> None:
        self.__result = value

    @property
    def data(self) -> tuple[int | float]:
        return self.__data

    @data.setter
    def data(self, data: tuple[int | float]) -> None:
        self.__data = data
