import os
from typing import Dict, Any
import google.generativeai as genai
from pydantic import BaseModel

class TaskAnalysis(BaseModel):
    """Model for task analysis results."""
    intent: str
    confidence: float
    action_type: str
    parameters: Dict[str, Any]
    plugin_name: str = ""

class TaskAnalyzer:
    """Analyzes user input to determine intent and required actions."""
    
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        api_key = config.get('api_keys', {}).get('google_gemini')
        if not api_key:
            raise ValueError("Google Gemini API key not found in config")
        
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-pro')
    
    async def analyze(self, input_data: Dict[str, Any]) -> TaskAnalysis:
        """Analyze user input to determine intent and required actions."""
        prompt = self._create_analysis_prompt(input_data)
        
        try:
            response = await self.model.generate_content_async(prompt)
            analysis = self._parse_response(response.text)
            return TaskAnalysis(**analysis)
        except Exception as e:
            print(f"Task analysis error: {str(e)}")
            return TaskAnalysis(
                intent="unknown",
                confidence=0.0,
                action_type="general",
                parameters={}
            )
    
    def _create_analysis_prompt(self, input_data: Dict[str, Any]) -> str:
        """Create a prompt for the Gemini model."""
        return f"""
        Analyze the following user input and determine:
        1. The user's intent
        2. The confidence level (0-1)
        3. The type of action required (web, computer, plugin, or general)
        4. Any relevant parameters
        5. If a plugin is needed, specify which one

        Input: {input_data.get('content', '')}
        Input Type: {input_data.get('type', 'unknown')}
        
        Respond in JSON format with the following structure:
        {{
            "intent": "string describing the intent",
            "confidence": float between 0 and 1,
            "action_type": "web|computer|plugin|general",
            "parameters": {{}},
            "plugin_name": "name of plugin if applicable"
        }}
        """
    
    def _parse_response(self, response_text: str) -> Dict[str, Any]:
        """Parse the model's response into a structured format."""
        # In a real implementation, you'd want to properly parse the JSON response
        # and handle potential errors
        import json
        try:
            return json.loads(response_text)
        except json.JSONDecodeError:
            return {
                "intent": "unknown",
                "confidence": 0.0,
                "action_type": "general",
                "parameters": {},
                "plugin_name": ""
            } 