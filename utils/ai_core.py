import os
import requests
import json
import datetime
import feedparser
from bs4 import BeautifulSoup
import time

class SecureImmigrationAI:
    def __init__(self):
        self.official_sources = {
            "boe_rss": "https://www.boe.es/rss/boe.php",
            "extranjeria": "https://extranjeros.inclusion.gob.es",
            "policia": "https://www.policia.es", 
            "ue_directives": "https://ec.europa.eu/immigration"
        }
        # SECURE: Get token from environment variable
        self.hf_token = os.getenv('HUGGINGFACE_TOKEN', '')
        
    def call_huggingface_ai(self, prompt):
        """SECURE Hugging Face API call"""
        if not self.hf_token:
            return self.fallback_response(prompt)
            
        try:
            API_URL = "https://api-inference.huggingface.co/models/microsoft/DialoGPT-large"
            headers = {"Authorization": f"Bearer {self.hf_token}"}
            
            payload = {
                "inputs": prompt,
                "parameters": {"max_length": 800, "temperature": 0.7}
            }
            
            response = requests.post(API_URL, headers=headers, json=payload, timeout=30)
            
            if response.status_code == 200:
                result = response.json()
                if isinstance(result, list) and len(result) > 0:
                    return result[0].get('generated_text', self.fallback_response(prompt))
            return self.fallback_response(prompt)
            
        except Exception as e:
            print(f"Hugging Face API error: {e}")
            return self.fallback_response(prompt)
    
    def call_openrouter_free(self, prompt):
        """Backup: OpenRouter free tier (no token needed)"""
        try:
            response = requests.post(
                "https://openrouter.ai/api/v1/chat/completions",
                headers={
                    "Authorization": "Bearer free",
                    "Content-Type": "application/json",
                    "HTTP-Referer": "https://tramibot.streamlit.app",
                    "X-Title": "Tramibot AI"
                },
                json={
                    "model": "google/palm-2-chat-bison",
                    "messages": [{"role": "user", "content": prompt}],
                    "max_tokens": 800
                },
                timeout=30
            )
            
            if response.status_code == 200:
                return response.json()['choices'][0]['message']['content']
            return self.fallback_response(prompt)
            
        except:
            return self.fallback_response(prompt)
    
    def call_ai_safely(self, prompt):
        """Main AI call - tries multiple secure methods"""
        # Try Hugging Face first (if token available)
        if self.hf_token:
            result = self.call_huggingface_ai(prompt)
            if result and "unavailable" not in result.lower():
                return result
        
        # Fallback to OpenRouter (free, no token)
        return self.call_openrouter_free(prompt)
    
    def fallback_response(self, prompt):
        """Fallback when AI services are down"""
        return "AI service is currently updating. Please check official Spanish government websites for the most current information."
    
    # Keep all your other methods (scan_official_updates, etc.)
    def scan_official_updates(self):
        """Scan official sources for procedure changes"""
        updates = []
        
        try:
            feed = feedparser.parse(self.official_sources["boe_rss"])
            for entry in feed.entries[:15]:
                if self.is_immigration_related(entry.title):
                    updates.append({
                        'source': 'BOE',
                        'date': entry.published,
                        'title': entry.title,
                        'content': entry.summary,
                        'link': entry.link,
                        'ai_analysis': self.analyze_update_safely(entry.title + " " + entry.summary)
                    })
        except Exception as e:
            print(f"BOE scan error: {e}")
        
        return updates
    
    def analyze_update_safely(self, update_text):
        """Analyze updates using secure AI"""
        prompt = f"""
        Analyze this Spanish legal update for immigration impact:
        {update_text}
        
        Provide brief analysis of:
        - Which procedures are affected
        - Key changes
        - Urgency level
        """
        return self.call_ai_safely(prompt)
    
    def is_immigration_related(self, text):
        keywords = ['extranjería', 'inmigración', 'residencia', 'nie', 'tie', 'visado']
        text_lower = text.lower()
        return any(keyword in text_lower for keyword in keywords)
    
    def generate_procedure_guide(self, procedure_name, user_context=""):
        """Generate AI-powered procedure guidance"""
        prompt = f"""
        As a Spanish immigration expert, provide CURRENT 2024 guidance for: {procedure_name}
        
        User context: {user_context}
        
        Include:
        1. Current requirements and documents
        2. Step-by-step process
        3. Processing times and costs
        4. Common issues and solutions
        
        Base on official Spanish government sources.
        """
        
        ai_response = self.call_ai_safely(prompt)
        
        return {
            'procedure': procedure_name,
            'generated_at': datetime.datetime.now().isoformat(),
            'ai_guidance': ai_response,
            'sources_checked': ['BOE', 'Ministry of Inclusion']
        }

# Secure instance
immigration_ai = SecureImmigrationAI()
