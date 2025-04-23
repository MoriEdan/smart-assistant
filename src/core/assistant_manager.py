from typing import Dict, Any, Optional
import asyncio
import logging
from .input_processor import InputProcessor
from .task_analyzer import TaskAnalyzer
from .web_automator import WebAutomator
from .computer_operator import ComputerOperator
from .response_generator import ResponseGenerator
from ..plugins.plugin_manager import PluginManager

class AssistantManager:
    """Manages and coordinates all components of the AI assistant system."""
    
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.input_processor = InputProcessor(config)
        self.task_analyzer = TaskAnalyzer(config)
        self.web_automator = WebAutomator(config)
        self.computer_operator = ComputerOperator(config)
        self.response_generator = ResponseGenerator(config)
        self.plugin_manager = PluginManager(config)
        self.conversation_context = {}
    
    async def initialize(self) -> None:
        """Initialize all components."""
        try:
            await self.web_automator.initialize()
            await self.plugin_manager.load_plugins()
            logging.info("Assistant initialized successfully")
        except Exception as e:
            logging.error(f"Initialization error: {str(e)}")
            raise
    
    async def process_input(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        """Process user input and generate appropriate response."""
        try:
            # Process input based on type
            if input_data.get('type') == 'text':
                processed_input = await self.input_processor.process_text(input_data.get('content', ''))
            elif input_data.get('type') == 'speech':
                processed_input = await self.input_processor.process_speech(input_data.get('audio_data', b''))
            else:
                raise ValueError("Invalid input type")
            
            # Analyze the task
            task_analysis = await self.task_analyzer.analyze(processed_input)
            
            # Execute appropriate action based on analysis
            if task_analysis.action_type == 'web':
                result = await self.web_automator.execute_task(task_analysis.parameters)
            elif task_analysis.action_type == 'computer':
                result = await self.computer_operator.execute_task(task_analysis.parameters)
            elif task_analysis.action_type == 'plugin':
                result = await self.plugin_manager.process_with_plugin(
                    task_analysis.plugin_name,
                    task_analysis.parameters
                )
            else:  # general conversation
                result = await self.response_generator.generate_response(
                    processed_input,
                    self.conversation_context
                )
            
            # Update conversation context
            if result.get('success'):
                self.conversation_context = await self.response_generator.update_context(
                    self.conversation_context,
                    processed_input.get('content', '')
                )
            
            return result
            
        except Exception as e:
            logging.error(f"Processing error: {str(e)}")
            return {
                'success': False,
                'error': str(e),
                'response': "Üzgünüm, bir hata oluştu. Lütfen tekrar deneyin."
            }
    
    async def cleanup(self) -> None:
        """Clean up all components."""
        try:
            await self.web_automator.cleanup()
            await self.plugin_manager.cleanup()
            logging.info("Assistant cleaned up successfully")
        except Exception as e:
            logging.error(f"Cleanup error: {str(e)}")
            raise 