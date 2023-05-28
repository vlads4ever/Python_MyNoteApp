from abc import ABCMeta, abstractmethod


class AbstractNote(metaclass=ABCMeta):
    @abstractmethod
    def get_header_note(self):
        pass

    @abstractmethod
    def get_body_note(self):
        pass
