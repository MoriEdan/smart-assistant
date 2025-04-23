from typing import Dict, Any
from ..plugin_base import PluginBase

class TourismAgencyPlugin(PluginBase):
    """Plugin for handling tourism-related tasks."""
    
    def __init__(self, config: Dict[str, Any]):
        super().__init__(config)
        self.tours = {
            'istanbul': [
                {'name': 'Historical Tour', 'duration': '4 hours', 'price': '100€'},
                {'name': 'Bosphorus Cruise', 'duration': '2 hours', 'price': '50€'},
                {'name': 'Food Tour', 'duration': '3 hours', 'price': '75€'}
            ],
            'cappadocia': [
                {'name': 'Hot Air Balloon', 'duration': '2 hours', 'price': '200€'},
                {'name': 'Cave Exploration', 'duration': '3 hours', 'price': '60€'},
                {'name': 'ATV Safari', 'duration': '2 hours', 'price': '45€'}
            ],
            'antalya': [
                {'name': 'Beach Day', 'duration': '6 hours', 'price': '40€'},
                {'name': 'Ancient Ruins', 'duration': '4 hours', 'price': '55€'},
                {'name': 'Water Park', 'duration': '5 hours', 'price': '35€'}
            ]
        }
    
    async def initialize(self) -> None:
        """Initialize the plugin."""
        # In a real implementation, you might want to load data from a database
        pass
    
    async def process(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        """Process tourism-related requests."""
        action = input_data.get('action')
        
        if action == 'list_tours':
            location = input_data.get('location', '').lower()
            if location in self.tours:
                return {
                    'success': True,
                    'tours': self.tours[location]
                }
            else:
                return {
                    'success': False,
                    'error': f'No tours available for {location}'
                }
        
        elif action == 'book_tour':
            location = input_data.get('location', '').lower()
            tour_name = input_data.get('tour_name')
            date = input_data.get('date')
            participants = input_data.get('participants', 1)
            
            if location not in self.tours:
                return {
                    'success': False,
                    'error': f'Invalid location: {location}'
                }
            
            tour = next((t for t in self.tours[location] if t['name'].lower() == tour_name.lower()), None)
            if not tour:
                return {
                    'success': False,
                    'error': f'Tour not found: {tour_name}'
                }
            
            # In a real implementation, you would save the booking to a database
            return {
                'success': True,
                'booking': {
                    'location': location,
                    'tour': tour,
                    'date': date,
                    'participants': participants,
                    'total_price': f"{float(tour['price'].replace('€', '')) * participants}€"
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