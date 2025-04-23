import pytest
import asyncio
from src.core.input_processor import InputProcessor
from src.core.task_analyzer import TaskAnalyzer
from src.core.web_automator import WebAutomator
from src.core.computer_operator import ComputerOperator
from src.core.response_generator import ResponseGenerator
from src.core.assistant_manager import AssistantManager

# Test configuration
TEST_CONFIG = {
    "api_keys": {
        "google_gemini": "test-key"
    },
    "speech_recognition": {
        "primary_engine": "online",
        "backup_engine": "vosk",
        "language": "tr-TR"
    },
    "web_automation": {
        "primary_engine": "browser-use",
        "backup_engine": "playwright",
        "headless": True
    },
    "plugins": {
        "enabled": True,
        "directory": "src/plugins/implementations"
    }
}

@pytest.mark.asyncio
async def test_input_processor():
    processor = InputProcessor(TEST_CONFIG)
    
    # Test text processing
    result = await processor.process_text("Merhaba dünya")
    assert result["type"] == "text"
    assert result["content"] == "Merhaba dünya"
    assert result["language"] == "tr-TR"
    
    # Test speech processing (mock)
    # In a real test, you would provide actual audio data
    result = await processor.process_speech(b"mock_audio_data")
    assert result["type"] == "speech"

@pytest.mark.asyncio
async def test_task_analyzer():
    analyzer = TaskAnalyzer(TEST_CONFIG)
    
    # Test task analysis
    input_data = {
        "type": "text",
        "content": "Google'da Python programlama hakkında ara"
    }
    result = await analyzer.analyze(input_data)
    
    assert result.intent is not None
    assert 0 <= result.confidence <= 1
    assert result.action_type in ["web", "computer", "plugin", "general"]

@pytest.mark.asyncio
async def test_web_automator():
    automator = WebAutomator(TEST_CONFIG)
    await automator.initialize()
    
    # Test web automation
    task = {
        "action": "navigate",
        "parameters": {
            "url": "https://www.google.com"
        }
    }
    result = await automator.execute_task(task)
    assert result["success"] is True
    
    await automator.cleanup()

@pytest.mark.asyncio
async def test_computer_operator():
    operator = ComputerOperator(TEST_CONFIG)
    
    # Test command execution
    task = {
        "action": "execute_command",
        "parameters": {
            "command": "echo test"
        }
    }
    result = await operator.execute_task(task)
    assert result["success"] is True

@pytest.mark.asyncio
async def test_response_generator():
    generator = ResponseGenerator(TEST_CONFIG)
    
    # Test response generation
    input_data = {
        "type": "text",
        "content": "Merhaba, nasılsın?"
    }
    result = await generator.generate_response(input_data)
    assert result["success"] is True
    assert "response" in result

@pytest.mark.asyncio
async def test_assistant_manager():
    manager = AssistantManager(TEST_CONFIG)
    await manager.initialize()
    
    # Test input processing
    input_data = {
        "type": "text",
        "content": "Merhaba"
    }
    result = await manager.process_input(input_data)
    assert result["success"] is True
    
    await manager.cleanup()

@pytest.mark.asyncio
async def test_plugin_system():
    manager = AssistantManager(TEST_CONFIG)
    await manager.initialize()
    
    # Test plugin loading
    assert len(manager.plugin_manager.get_available_plugins()) >= 0
    
    # Test plugin processing
    if "TourismAgencyPlugin" in manager.plugin_manager.get_available_plugins():
        result = await manager.plugin_manager.process_with_plugin(
            "TourismAgencyPlugin",
            {"action": "list_tours", "location": "istanbul"}
        )
        assert result["success"] is True
    
    await manager.cleanup()

if __name__ == "__main__":
    pytest.main([__file__]) 