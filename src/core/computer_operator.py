from typing import Dict, Any, Optional
import asyncio
from interpreter import interpreter
import logging
import os

class ComputerOperator:
    """Handles local system operations using Open Interpreter."""
    
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.interpreter = interpreter
        self._configure_interpreter()
    
    def _configure_interpreter(self) -> None:
        """Configure the Open Interpreter with appropriate settings."""
        # Set up interpreter configuration
        self.interpreter.auto_run = True
        self.interpreter.model = "gpt-3.5-turbo"  # Default model
        self.interpreter.temperature = 0.7
        
        # Set up system-specific configurations
        if os.name == 'nt':  # Windows
            self.interpreter.system_message = """
            You are a helpful AI assistant running on Windows.
            You can execute system commands and perform local operations.
            Always ensure operations are safe and user-approved.
            """
        else:  # Unix-like systems
            self.interpreter.system_message = """
            You are a helpful AI assistant running on a Unix-like system.
            You can execute system commands and perform local operations.
            Always ensure operations are safe and user-approved.
            """
    
    async def execute_task(self, task: Dict[str, Any]) -> Dict[str, Any]:
        """Execute a local system task."""
        try:
            action = task.get('action')
            params = task.get('parameters', {})
            
            if action == 'execute_command':
                return await self._execute_command(params)
            elif action == 'run_script':
                return await self._run_script(params)
            elif action == 'file_operation':
                return await self._file_operation(params)
            else:
                raise ValueError(f"Unsupported action: {action}")
        except Exception as e:
            logging.error(f"Computer operation error: {str(e)}")
            return {
                'success': False,
                'error': str(e)
            }
    
    async def _execute_command(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """Execute a system command."""
        command = params.get('command')
        if not command:
            raise ValueError("No command specified")
        
        # Execute the command using Open Interpreter
        result = await self.interpreter.chat(f"Execute the following command: {command}")
        return {
            'success': True,
            'output': result
        }
    
    async def _run_script(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """Run a script file."""
        script_path = params.get('path')
        if not script_path or not os.path.exists(script_path):
            raise ValueError(f"Script file not found: {script_path}")
        
        # Read and execute the script
        with open(script_path, 'r') as f:
            script_content = f.read()
        
        result = await self.interpreter.chat(f"Execute the following script:\n{script_content}")
        return {
            'success': True,
            'output': result
        }
    
    async def _file_operation(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """Perform file operations."""
        operation = params.get('operation')
        source = params.get('source')
        destination = params.get('destination')
        
        if operation == 'copy':
            command = f"copy {source} {destination}"
        elif operation == 'move':
            command = f"move {source} {destination}"
        elif operation == 'delete':
            command = f"del {source}"
        else:
            raise ValueError(f"Unsupported file operation: {operation}")
        
        result = await self.interpreter.chat(f"Execute the following command: {command}")
        return {
            'success': True,
            'output': result
        }
    
    async def cleanup(self) -> None:
        """Clean up resources."""
        # Open Interpreter doesn't require explicit cleanup
        pass 