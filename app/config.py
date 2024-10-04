# File: app/config.py
import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret-key'
    SUPABASE_URL = "https://zdmttxqybtfifynjlzgl.supabase.co"
    SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InpkbXR0eHF5YnRmaWZ5bmpsemdsIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTcyNzc3MjUwNywiZXhwIjoyMDQzMzQ4NTA3fQ.8VUchuT4kT-Zv0A3T2OkKM9IZzCRPnh28D6B3SA7E5w"