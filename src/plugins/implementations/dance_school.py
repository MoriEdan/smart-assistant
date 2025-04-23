from typing import Dict, Any
from ..plugin_base import PluginBase

class DanceSchoolPlugin(PluginBase):
    """Plugin for handling dance school-related tasks."""
    
    def __init__(self, config: Dict[str, Any]):
        super().__init__(config)
        self.dance_classes = {
            'salsa': [
                {'level': 'Beginner', 'schedule': 'Monday 19:00', 'instructor': 'Maria', 'price': '30€'},
                {'level': 'Intermediate', 'schedule': 'Wednesday 20:00', 'instructor': 'Carlos', 'price': '35€'},
                {'level': 'Advanced', 'schedule': 'Friday 21:00', 'instructor': 'Juan', 'price': '40€'}
            ],
            'bachata': [
                {'level': 'Beginner', 'schedule': 'Tuesday 19:00', 'instructor': 'Ana', 'price': '30€'},
                {'level': 'Intermediate', 'schedule': 'Thursday 20:00', 'instructor': 'Miguel', 'price': '35€'}
            ],
            'tango': [
                {'level': 'Beginner', 'schedule': 'Wednesday 18:00', 'instructor': 'Diego', 'price': '40€'},
                {'level': 'Advanced', 'schedule': 'Saturday 15:00', 'instructor': 'Elena', 'price': '45€'}
            ]
        }
    
    async def initialize(self) -> None:
        """Initialize the plugin."""
        # In a real implementation, you might want to load data from a database
        pass
    
    async def process(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        """Process dance school-related requests."""
        action = input_data.get('action')
        
        if action == 'list_classes':
            dance_type = input_data.get('dance_type', '').lower()
            if dance_type in self.dance_classes:
                return {
                    'success': True,
                    'classes': self.dance_classes[dance_type]
                }
            else:
                return {
                    'success': False,
                    'error': f'No classes available for {dance_type}'
                }
        
        elif action == 'register':
            dance_type = input_data.get('dance_type', '').lower()
            level = input_data.get('level')
            name = input_data.get('name')
            email = input_data.get('email')
            
            if dance_type not in self.dance_classes:
                return {
                    'success': False,
                    'error': f'Invalid dance type: {dance_type}'
                }
            
            class_info = next((c for c in self.dance_classes[dance_type] if c['level'].lower() == level.lower()), None)
            if not class_info:
                return {
                    'success': False,
                    'error': f'No {level} level class available for {dance_type}'
                }
            
            # In a real implementation, you would save the registration to a database
            return {
                'success': True,
                'registration': {
                    'dance_type': dance_type,
                    'class': class_info,
                    'student': {
                        'name': name,
                        'email': email
                    }
                }
            }
        
        elif action == 'schedule_private':
            dance_type = input_data.get('dance_type', '').lower()
            instructor = input_data.get('instructor')
            date = input_data.get('date')
            duration = input_data.get('duration', '1 hour')
            
            if dance_type not in self.dance_classes:
                return {
                    'success': False,
                    'error': f'Invalid dance type: {dance_type}'
                }
            
            # In a real implementation, you would check instructor availability
            return {
                'success': True,
                'private_lesson': {
                    'dance_type': dance_type,
                    'instructor': instructor,
                    'date': date,
                    'duration': duration,
                    'price': '60€'  # Base price for private lessons
                }
            }
        
        else:
            return {
                'success': False,
                'error': f'Unsupported action: {action}'
            }
    
    async def cleanup(self) -> None:
        """Clean up plugin resources."""
        pass 