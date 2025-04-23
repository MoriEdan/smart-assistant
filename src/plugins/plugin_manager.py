import importlib
import os
from typing import Dict, List, Type
from .plugin_base import PluginBase

class PluginManager:
    """Manages the loading and execution of plugins."""
    
    def __init__(self, config: Dict):
        self.config = config
        self.plugins: Dict[str, PluginBase] = {}
        self.plugins_dir = config.get('plugins', {}).get('directory', 'src/plugins/implementations')
    
    async def load_plugins(self) -> None:
        """Load all available plugins from the implementations directory."""
        if not os.path.exists(self.plugins_dir):
            return
        
        for filename in os.listdir(self.plugins_dir):
            if filename.endswith('.py') and not filename.startswith('_'):
                module_name = filename[:-3]
                try:
                    module = importlib.import_module(f'src.plugins.implementations.{module_name}')
                    for item_name in dir(module):
                        item = getattr(module, item_name)
                        if (isinstance(item, type) and 
                            issubclass(item, PluginBase) and 
                            item != PluginBase):
                            plugin_instance = item(self.config)
                            await plugin_instance.initialize()
                            self.plugins[plugin_instance.get_name()] = plugin_instance
                except Exception as e:
                    print(f"Error loading plugin {module_name}: {str(e)}")
    
    async def process_with_plugin(self, plugin_name: str, input_data: Dict) -> Dict:
        """Process input data using a specific plugin."""
        if plugin_name not in self.plugins:
            raise ValueError(f"Plugin {plugin_name} not found")
        
        return await self.plugins[plugin_name].process(input_data)
    
    async def cleanup(self) -> None:
        """Clean up all loaded plugins."""
        for plugin in self.plugins.values():
            await plugin.cleanup()
        self.plugins.clear()
    
    def get_available_plugins(self) -> List[str]:
        """Return a list of available plugin names."""
        return list(self.plugins.keys()) 