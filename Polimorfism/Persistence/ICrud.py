from abc import ABC, abstractmethod


class ICrud (ABC):

    @abstractmethod
    def to_get_by(self, ** kwargs):
        raise NotImplementedError
