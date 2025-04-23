# Quickstart Guide

This guide will help you get started with the Smart AI Assistant quickly.

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git (optional, for cloning the repository)
- Microphone (for voice mode)

## Installation Steps

1. **Get the Code**
   ```bash
   # Option 1: Clone the repository
   git clone https://github.com/MoriEdan/smart-assistant.git
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

2. **Voice Mode Activation**
   - The assistant starts in text mode by default
   - To activate voice mode, say one of these keywords:
     - "hey asistan"
     - "merhaba asistan"
     - "asistan"
   - The assistant will respond with a welcome message

3. **Mode Switching**
   - To switch to voice mode:
     - Say or type: "sesli mod" or "sesli dinleme modu"
   - To switch to text mode:
     - Say or type: "metin modu" or "yazılı mod"
   - The assistant will confirm the mode change

4. **Interact with the Assistant**
   - In text mode: Type your questions or commands
   - In voice mode: Speak your questions or commands
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

### Voice Commands
```
"Hey asistan, bugün hava nasıl?"
"Merhaba asistan, müzik çal"
"Asistan, dosya oluştur"
```

## Troubleshooting

### Common Issues

1. **Module Not Found Error**
   - Make sure you've activated the virtual environment
   - Run `pip install -r requirements.txt` again

2. **API Key Errors**
   - Check your `.env` file for correct API keys
   - Ensure you have valid API keys for all services

3. **Voice Recognition Issues**
   - Check microphone settings and permissions
   - Ensure proper language configuration in config.json
   - Verify Vosk model installation if using offline recognition
   - Try speaking clearly and at a normal pace
   - Check if the activation keywords are recognized
   - Verify that the correct mode is active

4. **Mode Switching Problems**
   - Ensure you're using the correct mode switching commands
   - Check if the assistant confirms mode changes
   - Verify microphone is working in voice mode
   - Test both voice and text commands in each mode