# File: app/supabase_config.py
from supabase import create_client

supabase = None

def initialize_supabase(app):
    global supabase
    supabase = create_client(app.config['SUPABASE_URL'], app.config['SUPABASE_KEY'])
    print("Connecting to Supabase database...")
    try:
        # Attempt a simple query to check the connection
        supabase.table('hotels').select('id').limit(1).execute()
        print("Successfully connected to Supabase database.")
    except Exception as e:
        print(f"Failed to connect to Supabase database. Error: {str(e)}")