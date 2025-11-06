import schedule
import time
from ai_updater import LegalAIUpdater

def daily_update_job():
    """Run daily to check for updates"""
    updater = LegalAIUpdater()
    
    # Check official sources
    boe_updates = updater.check_boe_updates()
    procedure_changes = updater.monitor_procedure_changes()
    
    # Save updates to database (implement this)
    save_updates(boe_updates, procedure_changes)

# Schedule daily checks
schedule.every().day.at("09:00").do(daily_update_job)

def run_scheduler():
    while True:
        schedule.run_pending()
        time.sleep(3600)  # Check every hour
