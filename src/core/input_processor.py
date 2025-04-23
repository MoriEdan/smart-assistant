import os
import asyncio
from typing import Optional, Dict, Any
import speech_recognition as sr
from vosk import Model, KaldiRecognizer
import json
import wave
from dotenv import load_dotenv

class InputProcessor:
    """Handles both text and speech input processing with voice activation."""
    
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.speech_config = config.get('speech_recognition', {})
        self.recognizer = sr.Recognizer()
        self.vosk_model = None
        self.voice_mode = False
        self.activation_keywords = ["hey asistan", "merhaba asistan", "asistan"]
        self._initialize_vosk()
        load_dotenv()
    
    def _initialize_vosk(self) -> None:
        """Initialize the Vosk model if configured."""
        model_path = self.speech_config.get('vosk_model_path')
        if model_path and os.path.exists(model_path):
            self.vosk_model = Model(model_path)
    
    async def process_text(self, text: str) -> Dict[str, Any]:
        """Process text input and handle mode switching commands."""
        if text.lower() in ["sesli mod", "sesli dinleme modu"]:
            self.voice_mode = True
            return {
                'type': 'mode_switch',
                'content': 'Sesli dinleme modu aktif. Dinliyorum...',
                'mode': 'voice'
            }
        elif text.lower() in ["metin modu", "yazılı mod"]:
            self.voice_mode = False
            return {
                'type': 'mode_switch',
                'content': 'Metin modu aktif. Yazılı komutlarınızı bekliyorum.',
                'mode': 'text'
            }
        
        return {
            'type': 'text',
            'content': text,
            'language': self.speech_config.get('language', 'tr-TR')
        }
    
    async def process_speech(self, audio_data: bytes) -> Dict[str, Any]:
        """Process speech input using primary and backup engines with activation detection."""
        try:
            # Try primary engine (online)
            if self.speech_config.get('primary_engine') == 'online':
                result = await self._process_speech_online(audio_data)
            else:
                # Fallback to Vosk
                result = await self._process_speech_vosk(audio_data)
            
            # Check for activation keywords
            content = result.get('content', '').lower()
            if any(keyword in content for keyword in self.activation_keywords):
                return {
                    'type': 'activation',
                    'content': content,
                    'activated': True
                }
            
            return result
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
    
    def is_voice_mode_active(self) -> bool:
        """Check if voice mode is currently active."""
        return self.voice_mode
    
    async def get_welcome_message(self) -> str:
        """Get the appropriate welcome message based on current mode."""
        if self.voice_mode:
            return "Merhaba! Sesli dinleme modunda çalışıyorum. Size nasıl yardımcı olabilirim?"
        return "Merhaba! Metin modunda çalışıyorum. Komutlarınızı yazabilirsiniz."