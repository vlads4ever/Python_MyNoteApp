from abc import ABCMeta, abstractmethod


class AbstractNote(metaclass=ABCMeta):
    @abstractmethod
    def get_id_note(self):
        pass

    @abstractmethod
    def get_header(self):
        pass

    @abstractmethod
    def get_body(self):
        pass

    @abstractmethod
    def get_creation_time(self):
        pass

    @abstractmethod
    def set_header(self, header_note: str):
        pass

    @abstractmethod
    def set_body(self, body_note: list):
        pass

    @abstractmethod
    def time_renew(self):
        pass
