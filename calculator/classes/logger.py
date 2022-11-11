import os.path


class Logger:
    """
    Singleton for logging

        Attributes
            filename: str = 'logger.log'
                Path to file for saving logs
    """

    __INSTANCE: 'Logger' = None
    __MAX_LINES_COUNT: int = 5

    def __new__(cls, *args, **kwargs) -> 'Logger':
        if cls.__INSTANCE is None:
            cls.__INSTANCE = super().__new__(cls)

        return cls.__INSTANCE

    def __init__(self, filename: str = 'logger.log'):
        self.filename: str = filename

    def __check_lines_count(self, message: str) -> None:
        """Checks lines in log file if file exists"""

        if not os.path.exists(self.filename):
            return None
        with open(self.filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        if len(lines) > self.__MAX_LINES_COUNT:
            print(message)

    def log(self, message: str) -> None:
        """Write message to file"""

        with open(self.filename, 'a', encoding='utf-8') as f_write:
            f_write.write(f'{message}\n')
        self.__check_lines_count(message)
