# Quickstart Guide

This guide will help you get started with the Smart AI Assistant quickly.

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git (optional, for cloning the repository)

## Installation Steps

1. **Get the Code**
   ```bash
   # Option 1: Clone the repository
   git clone https://github.com/yourusername/smart-assistant.git
   cd smart-assistant

   # Option 2: Download and extract the ZIP
   # Then navigate to the extracted directory
   ```

2. **Set Up Virtual Environment**
   ```bash
   # Create virtual environment
   python -m venv venv

   # Activate virtual environment
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure the Assistant**
   ```bash
   # Copy example configuration files
   cp .env.example .env
   cp config.json.example config.json

   # Edit .env with your API keys and settings
   # Edit config.json with your preferences
   ```

## Basic Usage

1. **Start the Assistant**
   ```bash
   python main.py
   ```

2. **Interact with the Assistant**
   - Type your questions or commands
   - The assistant will respond in Turkish
   - Type 'exit' to quit

## Example Commands

### General Questions
```
Merhaba, nasılsın?
Bugün hava nasıl?
Python nedir?
```

### Web Automation
```
Google'da Python programlama hakkında ara
YouTube'da müzik çal
```

### System Operations
```
Dosya oluştur
Dizin listele
Program başlat
```

### Plugin-Specific Commands
```
İstanbul'daki turları listele
Salsa derslerini göster
```

## Troubleshooting

### Common Issues

1. **Module Not Found Error**
   - Make sure you've activated the virtual environment
   - Run `pip install -r requirements.txt` again

2. **API Key Errors**
   - Check your `.env` file for correct API keys
   - Ensure you have valid API keys for all services

3. **Speech Recognition Issues**
   - Check microphone permissions
   - Verify Vosk model path in configuration

### Getting Help

- Check the [documentation](docs/deepdive.md) for detailed information
- Open an issue on GitHub for bugs or feature requests
- Contact support for additional help

## Next Steps

- Read the [detailed documentation](docs/deepdive.md)
- Explore plugin development
- Customize the assistant for your needs
- Contribute to the project 