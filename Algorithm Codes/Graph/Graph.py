from abc import ABC, abstractmethod
#Abstract Class
class Graph(ABC):
    @abstractmethod
    def add_edge(self, edge):
        pass
    
    @abstractmethod
    def remove_edge(self, edge):
        pass

