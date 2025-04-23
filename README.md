# Smart AI Assistant

A powerful and flexible AI assistant system that combines various AI capabilities to provide a comprehensive solution for different tasks. The system supports text and speech input, web automation, local system operations, and extensible plugins for specific domains.

## Features

- **Multimodal Input Processing**
  - Text input support
  - Speech recognition (online and offline)
  - Turkish language support

- **Intelligent Task Analysis**
  - Intent recognition using Google Gemini API
  - Task classification and routing
  - Context-aware responses

- **Web Automation**
  - Browser automation using browser-use
  - Backup support with Playwright
  - Web scraping and interaction capabilities

- **Local System Operations**
  - Command execution
  - File operations
  - Script running
  - System management

- **Plugin System**
  - Modular architecture
  - Easy plugin development
  - Domain-specific functionality
  - Example plugins for tourism and education

## Installation

1. Clone the repository:
```bash
git clone https://github.com/MoriEdan/smart-assistant.git
cd smart-assistant
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Copy and configure environment variables:
```bash
cp .env.example .env
# Edit .env with your configuration
```

5. Copy and configure the main configuration:
```bash
cp config.json.example config.json
# Edit config.json with your settings
```

## Configuration

### Environment Variables (.env)
- `GOOGLE_GEMINI_API_KEY`: Your Google Gemini API key
- `SPEECH_RECOGNITION_LANGUAGE`: Default language for speech recognition (e.g., 'tr-TR')
- `VOSK_MODEL_PATH`: Path to Vosk model for offline speech recognition
- `LOG_LEVEL`: Logging level (INFO, DEBUG, etc.)
- `LOG_FILE`: Path to log file

### Main Configuration (config.json)
- API keys and credentials
- Speech recognition settings
- Web automation preferences
- Plugin configurations
- System settings

## Usage

1. Start the assistant:
```bash
python main.py
```

2. Interact with the assistant:
- Type your queries or commands
- Use voice input (if configured)
- Type 'exit' to quit

## Plugin Development

To create a new plugin:

1. Create a new Python file in `src/plugins/implementations/`
2. Inherit from `PluginBase`:
```python
from ..plugin_base import PluginBase

class MyPlugin(PluginBase):
    def __init__(self, config):
        super().__init__(config)
    
    async def initialize(self):
        # Initialize your plugin
    
    async def process(self, input_data):
        # Process input and return results
    
    async def cleanup(self):
        # Clean up resources
```

3. Implement the required methods
4. The plugin will be automatically loaded on startup

## Example Plugins

### Tourism Agency Plugin
- List available tours
- Book tours
- Manage reservations

### Dance School Plugin
- List dance classes
- Register for classes
- Schedule private lessons

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Google Gemini API for natural language processing
- Vosk for offline speech recognition
- browser-use and Playwright for web automation
- Open Interpreter for local system operations 