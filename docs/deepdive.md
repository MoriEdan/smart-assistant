# Deep Dive Documentation

This document provides detailed information about the Smart AI Assistant's architecture, components, and advanced usage.

## Architecture Overview

The Smart AI Assistant follows a modular, layered architecture:

```
┌─────────────────┐
│  User Interface │
└────────┬────────┘
         │
┌────────▼────────┐
│  Input Layer    │
└────────┬────────┘
         │
┌────────▼────────┐
│  Task Analysis  │
└────────┬────────┘
         │
┌────────▼────────┐
│  Action Layer   │
└────────┬────────┘
         │
┌────────▼────────┐
│  Plugin System  │
└─────────────────┘
```

## Core Components

### 1. Input Processor (`input_processor.py`)

Handles different types of user input:
- Text input processing
- Speech recognition (online and offline)
- Language detection and processing
- Voice activation and mode switching

#### Key Features:
- Dual-engine speech recognition (online/offline)
- Turkish language support
- Voice activation keywords: "hey asistan", "merhaba asistan", "asistan"
- Mode switching between voice and text modes
- Dynamic welcome messages based on current mode
- Error handling and fallback mechanisms

#### Voice Activation:
- Keywords: "hey asistan", "merhaba asistan", "asistan"
- Activation triggers voice mode
- Confirmation message on successful activation
- Fallback to text mode if activation fails

#### Mode Switching:
- Voice Mode Activation:
  - Command: "sesli mod" or "sesli dinleme modu"
  - Welcome Message: "Merhaba! Sesli dinleme modunda çalışıyorum. Size nasıl yardımcı olabilirim?"
- Text Mode Activation:
  - Command: "metin modu" or "yazılı mod"
  - Welcome Message: "Merhaba! Metin modunda çalışıyorum. Komutlarınızı yazabilirsiniz."

#### Configuration:
```json
{
    "speech_recognition": {
        "primary_engine": "online",
        "backup_engine": "vosk",
        "language": "tr-TR",
        "activation_keywords": ["hey asistan", "merhaba asistan", "asistan"],
        "vosk_model_path": "path/to/vosk/model",
        "sample_rate": 16000,
        "channels": 2
    }
}
```

### 2. Task Analyzer (`task_analyzer.py`)

Analyzes user input to determine intent and required actions:
- Uses Google Gemini API for natural language understanding
- Classifies tasks into different categories
- Extracts parameters and context
- Handles both voice and text input

#### Task Categories:
- Web automation
- System operations
- Plugin-specific tasks
- General conversation
- Mode switching commands

### 3. Web Automator (`web_automator.py`)

Handles web-related tasks:
- Browser automation
- Web scraping
- Form filling
- Navigation

#### Supported Actions:
- Navigate to URL
- Click elements
- Fill forms
- Extract data
- Handle dynamic content

### 4. Computer Operator (`computer_operator.py`)

Manages local system operations:
- File operations
- Command execution
- Process management
- System configuration

#### Security Features:
- Command validation
- Permission checking
- Safe execution environment

### 5. Plugin System

Extensible architecture for domain-specific functionality:
- Base plugin interface
- Plugin loading and management
- Event handling system
- Configuration management

## Advanced Configuration

### Voice Recognition Settings

```json
{
    "speech_recognition": {
        "primary_engine": "online",
        "backup_engine": "vosk",
        "language": "tr-TR",
        "activation_keywords": ["hey asistan", "merhaba asistan", "asistan"],
        "vosk_model_path": "path/to/vosk/model",
        "sample_rate": 16000,
        "channels": 2,
        "energy_threshold": 300,
        "dynamic_energy_threshold": True,
        "pause_threshold": 0.8
    }
}
```

### Mode Configuration

```json
{
    "modes": {
        "voice": {
            "welcome_message": "Merhaba! Sesli dinleme modunda çalışıyorum. Size nasıl yardımcı olabilirim?",
            "activation_commands": ["sesli mod", "sesli dinleme modu"],
            "deactivation_timeout": 300,
            "confirmation_sound": true
        },
        "text": {
            "welcome_message": "Merhaba! Metin modunda çalışıyorum. Komutlarınızı yazabilirsiniz.",
            "activation_commands": ["metin modu", "yazılı mod"]
        }
    }
}
```

## Development Guidelines

### Adding New Features

1. **Voice Activation Keywords**
   - Add new keywords to `activation_keywords` list in config
   - Update documentation with new keywords
   - Test with different voice inputs
   - Consider adding language-specific variations

2. **Mode Switching**
   - Add new mode commands to configuration
   - Implement mode-specific welcome messages
   - Update UI to reflect current mode
   - Add mode transition animations/sounds
   - Implement mode persistence

3. **Speech Recognition**
   - Configure Vosk model path
   - Set appropriate sample rate and channels
   - Test with different audio inputs
   - Implement noise reduction
   - Add support for multiple languages

### Testing

1. **Voice Recognition Testing**
   - Test with different activation keywords
   - Verify mode switching functionality
   - Check welcome messages for each mode
   - Test with background noise
   - Verify fallback mechanisms

2. **Error Handling**
   - Test offline recognition fallback
   - Verify error messages
   - Check recovery from failed states
   - Test microphone disconnection
   - Verify mode persistence

## Troubleshooting

### Voice Recognition Issues

1. **Activation Not Working**
   - Check microphone settings and permissions
   - Verify activation keywords in config
   - Test with different voice inputs
   - Check audio device configuration
   - Verify language settings

2. **Mode Switching Problems**
   - Verify mode commands in config
   - Check welcome message configuration
   - Test mode persistence
   - Verify microphone state
   - Check for conflicting commands

3. **Speech Recognition Errors**
   - Verify Vosk model installation
   - Check audio device configuration
   - Test with different sample rates
   - Verify language support
   - Check for background noise
   - Test with different microphones