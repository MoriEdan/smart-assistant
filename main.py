import asyncio
import json
import os
import logging
from dotenv import load_dotenv
from src.core.assistant_manager import AssistantManager
from rich.console import Console
from rich.logging import RichHandler

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(message)s",
    datefmt="[%X]",
    handlers=[RichHandler(rich_tracebacks=True)]
)

console = Console()

async def main():
    """Main entry point for the application."""
    try:
        # Load environment variables
        load_dotenv()
        
        # Load configuration
        config_path = os.getenv('CONFIG_PATH', 'config.json')
        if not os.path.exists(config_path):
            console.print(f"[red]Configuration file not found: {config_path}[/red]")
            return
        
        with open(config_path, 'r') as f:
            config = json.load(f)
        
        # Initialize assistant
        assistant = AssistantManager(config)
        await assistant.initialize()
        
        console.print("[green]AI Assistant initialized successfully![/green]")
        console.print("Type 'exit' to quit.")
        
        # Main interaction loop
        while True:
            try:
                user_input = input("\nYou: ").strip()
                
                if user_input.lower() == 'exit':
                    break
                
                # Process input
                result = await assistant.process_input({
                    'type': 'text',
                    'content': user_input
                })
                
                # Display response
                if result.get('success'):
                    console.print(f"\nAssistant: {result.get('response')}")
                else:
                    console.print(f"\n[red]Error: {result.get('error')}[/red]")
                
            except KeyboardInterrupt:
                break
            except Exception as e:
                console.print(f"\n[red]Error: {str(e)}[/red]")
        
    except Exception as e:
        console.print(f"[red]Fatal error: {str(e)}[/red]")
    finally:
        # Cleanup
        try:
            await assistant.cleanup()
        except Exception as e:
            console.print(f"[red]Cleanup error: {str(e)}[/red]")

if __name__ == "__main__":
    asyncio.run(main()) 