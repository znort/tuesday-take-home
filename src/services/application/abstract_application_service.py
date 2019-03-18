from abc import ABC, abstractmethod


class AbstractApplicationService(ABC):
    # YOU ARE NOT REQUIRED TO MODIFY THIS CLASS
    def __init__(self, router):
        self.register_routes(router)

    @abstractmethod
    def register_routes(self, router):
        pass
