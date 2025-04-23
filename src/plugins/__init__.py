"""
Plugin system for the Smart AI Assistant.
"""

from .plugin_base import PluginBase
from .plugin_manager import PluginManager

__all__ = [
    'PluginBase',
    'PluginManager'
] 