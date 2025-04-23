from abc import ABC, abstractmethod
from typing import Any, Dict

class PluginBase(ABC):
    """Base class for all plugins in the system."""
    
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.name = self.__class__.__name__
    
    @abstractmethod
    async def initialize(self) -> None:
        """Initialize the plugin with necessary resources."""
        pass
    
    @abstractmethod
    async def process(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        """Process the input data and return the result."""
        pass
    
    @abstractmethod
    async def cleanup(self) -> None:
        """Clean up any resources used by the plugin."""
        pass
    
    def get_name(self) -> str:
        """Return the name of the plugin."""
        return self.name 