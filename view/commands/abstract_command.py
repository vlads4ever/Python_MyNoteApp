from abc import ABCMeta, abstractmethod


class AbstractCommand(metaclass=ABCMeta):
    @abstractmethod
    def get_description(self) -> str:
        pass

    @abstractmethod
    def execute(self):
        pass
