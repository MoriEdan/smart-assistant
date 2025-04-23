from typing import Dict, Any, Optional
import google.generativeai as genai
import logging

class ResponseGenerator:
    """Generates responses for general conversation and queries."""
    
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        api_key = config.get('api_keys', {}).get('google_gemini')
        if not api_key:
            raise ValueError("Google Gemini API key not found in config")
        
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-pro')
        self._setup_prompt_template()
    
    def _setup_prompt_template(self) -> None:
        """Set up the prompt template for the model."""
        self.prompt_template = """
        You are a helpful AI assistant that can:
        1. Answer general questions
        2. Provide explanations
        3. Engage in natural conversation
        4. Offer suggestions and recommendations
        
        Current conversation context:
        {context}
        
        User input: {input}
        
        Please provide a helpful and informative response in Turkish.
        """
    
    async def generate_response(self, input_data: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Generate a response for the given input."""
        try:
            prompt = self._create_prompt(input_data, context)
            response = await self.model.generate_content_async(prompt)
            
            return {
                'success': True,
                'response': response.text,
                'context': context
            }
        except Exception as e:
            logging.error(f"Response generation error: {str(e)}")
            return {
                'success': False,
                'error': str(e),
                'response': "Üzgünüm, bir hata oluştu. Lütfen tekrar deneyin."
            }
    
    def _create_prompt(self, input_data: Dict[str, Any], context: Optional[Dict[str, Any]]) -> str:
        """Create a prompt for the model."""
        context_str = ""
        if context:
            context_str = f"Previous messages: {context.get('messages', [])}"
        
        return self.prompt_template.format(
            context=context_str,
            input=input_data.get('content', '')
        )
    
    async def update_context(self, context: Dict[str, Any], new_message: str) -> Dict[str, Any]:
        """Update the conversation context with a new message."""
        if 'messages' not in context:
            context['messages'] = []
        
        context['messages'].append(new_message)
        
        # Keep only the last 10 messages to maintain context
        if len(context['messages']) > 10:
            context['messages'] = context['messages'][-10:]
        
        return context 