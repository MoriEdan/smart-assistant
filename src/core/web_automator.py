from typing import Dict, Any, Optional
import asyncio
from browser_use import Browser
from playwright.async_api import async_playwright, Browser as PlaywrightBrowser
import logging

class WebAutomator:
    """Handles web automation tasks using browser-use and Playwright."""
    
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.web_config = config.get('web_automation', {})
        self.primary_engine = self.web_config.get('primary_engine', 'browser-use')
        self.browser_use = None
        self.playwright = None
        self.playwright_browser = None
    
    async def initialize(self) -> None:
        """Initialize the web automation engines."""
        if self.primary_engine == 'browser-use':
            self.browser_use = Browser()
        else:
            playwright = await async_playwright().start()
            self.playwright = playwright
            self.playwright_browser = await playwright.chromium.launch(
                headless=self.web_config.get('headless', True)
            )
    
    async def execute_task(self, task: Dict[str, Any]) -> Dict[str, Any]:
        """Execute a web automation task."""
        try:
            if self.primary_engine == 'browser-use':
                return await self._execute_with_browser_use(task)
            else:
                return await self._execute_with_playwright(task)
        except Exception as e:
            logging.error(f"Web automation error: {str(e)}")
            return {
                'success': False,
                'error': str(e)
            }
    
    async def _execute_with_browser_use(self, task: Dict[str, Any]) -> Dict[str, Any]:
        """Execute task using browser-use."""
        if not self.browser_use:
            raise ValueError("Browser-use not initialized")
        
        action = task.get('action')
        params = task.get('parameters', {})
        
        if action == 'navigate':
            await self.browser_use.navigate(params.get('url'))
            return {'success': True}
        elif action == 'click':
            await self.browser_use.click(params.get('selector'))
            return {'success': True}
        elif action == 'type':
            await self.browser_use.type(params.get('selector'), params.get('text'))
            return {'success': True}
        elif action == 'extract':
            result = await self.browser_use.extract(params.get('selector'))
            return {'success': True, 'data': result}
        else:
            raise ValueError(f"Unsupported action: {action}")
    
    async def _execute_with_playwright(self, task: Dict[str, Any]) -> Dict[str, Any]:
        """Execute task using Playwright."""
        if not self.playwright_browser:
            raise ValueError("Playwright not initialized")
        
        context = await self.playwright_browser.new_context()
        page = await context.new_page()
        
        try:
            action = task.get('action')
            params = task.get('parameters', {})
            
            if action == 'navigate':
                await page.goto(params.get('url'))
                return {'success': True}
            elif action == 'click':
                await page.click(params.get('selector'))
                return {'success': True}
            elif action == 'type':
                await page.fill(params.get('selector'), params.get('text'))
                return {'success': True}
            elif action == 'extract':
                result = await page.text_content(params.get('selector'))
                return {'success': True, 'data': result}
            else:
                raise ValueError(f"Unsupported action: {action}")
        finally:
            await context.close()
    
    async def cleanup(self) -> None:
        """Clean up resources."""
        if self.playwright:
            await self.playwright_browser.close()
            await self.playwright.stop() 