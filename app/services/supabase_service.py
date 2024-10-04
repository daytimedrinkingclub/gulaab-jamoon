# File: app/services/supabase_service.py
from app.supabase_config import supabase

def get_hotel_by_slug(slug):
    return supabase.table('hotels').select(
        'id',
        'created_at',
        'slug',
        'hero_url',
        'stay_id',
        'logo_url',
        'map_location',
        'city',
        'email',
        'contact',
        'facebook',
        'instagram',
        'all_images',
        'name'
    ).eq('slug', slug).execute()

def get_experiences_by_city(city_id):
    return supabase.table('experience').select(
        'id',
        'created_at',
        'name',
        'city',
        'rating',
        'thumbnail',
        'short_description',
        'long_description',
        'payment_link',
        'duration',
        'location_link',
        'open_time',
        'open_days',
        'price',
        'inclusions',
        'exclusions',
        'entry_fee',
        'close_time',
        'type'
    ).eq('city', city_id).execute()