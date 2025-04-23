import os
import asyncio
from typing import Optional, Dict, Any
import speech_recognition as sr
from vosk import Model, KaldiRecognizer
import json
import wave

class InputProcessor:
    """Handles both text and speech input processing."""
    
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.speech_config = config.get('speech_recognition', {})
        self.recognizer = sr.Recognizer()
        self.vosk_model = None
        self._initialize_vosk()
    
    def _initialize_vosk(self) -> None:
        """Initialize the Vosk model if configured."""
        model_path = self.speech_config.get('vosk_model_path')
        if model_path and os.path.exists(model_path):
            self.vosk_model = Model(model_path)
    
    async def process_text(self, text: str) -> Dict[str, Any]:
        """Process text input."""
        return {
            'type': 'text',
            'content': text,
            'language': self.speech_config.get('language', 'tr-TR')
        }
    
    async def process_speech(self, audio_data: bytes) -> Dict[str, Any]:
        """Process speech input using primary and backup engines."""
        try:
            # Try primary engine (online)
            if self.speech_config.get('primary_engine') == 'online':
                return await self._process_speech_online(audio_data)
            
            # Fallback to Vosk
            return await self._process_speech_vosk(audio_data)
        except Exception as e:
            print(f"Speech recognition error: {str(e)}")
            return {
                'type': 'speech',
                'content': '',
                'error': str(e)
            }
    
    async def _process_speech_online(self, audio_data: bytes) -> Dict[str, Any]:
        """Process speech using online recognition."""
        with sr.AudioData(audio_data, 16000, 2) as source:
            text = self.recognizer.recognize_google(
                source,
                language=self.speech_config.get('language', 'tr-TR')
            )
            return {
                'type': 'speech',
                'content': text,
                'engine': 'online'
            }
    
    async def _process_speech_vosk(self, audio_data: bytes) -> Dict[str, Any]:
        """Process speech using Vosk offline recognition."""
        if not self.vosk_model:
            raise ValueError("Vosk model not initialized")
        
        # Convert audio data to WAV format
        wav_data = self._convert_to_wav(audio_data)
        
        rec = KaldiRecognizer(self.vosk_model, 16000)
        rec.AcceptWaveform(wav_data)
        
        result = json.loads(rec.FinalResult())
        return {
            'type': 'speech',
            'content': result.get('text', ''),
            'engine': 'vosk'
        }
    
    def _convert_to_wav(self, audio_data: bytes) -> bytes:
        """Convert audio data to WAV format."""
        # This is a simplified version - in production, you'd want to use proper audio conversion
        return audio_data 