import requests
import feedparser
import json
import datetime
from bs4 import BeautifulSoup
import time

class LegalAIUpdater:
    def __init__(self):
        self.official_sources = {
            "boe_rss": "https://www.boe.es/rss/boe.php",
            "extranjeria_news": "https://extranjeros.inclusion.gob.es/es/prensa/Noticias/index.html",
            "policia_news": "https://www.policia.es/prensa/prensa_actualidad.html"
        }
        
    def check_boe_updates(self):
        """Check Official State Gazette for immigration-related updates"""
        try:
            feed = feedparser.parse(self.official_sources["boe_rss"])
            updates = []
            
            for entry in feed.entries[:10]:  # Check last 10 entries
                if any(keyword in entry.title.lower() for keyword in 
                      ['extranjería', 'inmigración', 'residencia', 'nie', 'tie', 'visado']):
                    updates.append({
                        'date': entry.published,
                        'title': entry.title,
                        'link': entry.link,
                        'summary': entry.summary[:200] + '...' if entry.summary else ''
                    })
            return updates
        except Exception as e:
            print(f"Error checking BOE: {e}")
            return []
    
    def monitor_procedure_changes(self):
        """Monitor known procedures for changes"""
        procedures_to_monitor = [
            "NIE Application",
            "TIE Card", 
            "EU Registration",
            "Family Reunification",
            "Student Residence",
            "Work Permit"
        ]
        
        changes_detected = []
        
        for procedure in procedures_to_monitor:
            # Check for updates in official documentation
            latest_info = self.get_latest_procedure_info(procedure)
            changes_detected.extend(latest_info)
            
        return changes_detected
    
    def get_latest_procedure_info(self, procedure):
        """Get latest information for a specific procedure"""
        # This would use official APIs or structured data where available
        # For now, using known patterns and manual updates
        
        procedure_data = {
            "NIE Application": {
                "last_checked": datetime.datetime.now().isoformat(),
                "status": "current",
                "requirements": ["EX-15 form", "Passport", "Tasa 790", "Appointment"],
                "notes": "Process remains unchanged",
                "source": "Official Ministry website"
            },
            "TIE Card": {
                "last_checked": datetime.datetime.now().isoformat(),
                "status": "current", 
                "requirements": ["EX-17 form", "Passport", "Visa", "Empadronamiento", "Photos"],
                "notes": "Standard 30-40 day processing",
                "source": "Police website"
            }
        }
        
        return procedure_data.get(procedure, {})
