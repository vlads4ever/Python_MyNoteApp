from abc import ABCMeta, abstractmethod


class AbstractAdapter(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def save(obj, path: str):
        pass

    @staticmethod
    @abstractmethod
    def load(path):
        pass
