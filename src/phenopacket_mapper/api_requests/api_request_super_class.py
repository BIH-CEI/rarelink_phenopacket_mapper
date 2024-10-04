from abc import ABC, abstractmethod

from phenopacket_mapper.data_standards import Coding


class APIRequestSuperClass(ABC):

    @abstractmethod
    def get(self, concept_id) -> Coding:
        pass
