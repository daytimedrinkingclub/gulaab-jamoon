# File: app/routes/main.py
from flask import Blueprint, render_template, abort
from app.services.supabase_service import get_hotel_by_slug, get_experiences_by_city, get_experience_by_id

main_bp = Blueprint('main', __name__)

@main_bp.route('/<hotel_slug>')
def hotel_page(hotel_slug):
    hotel_data = get_hotel_by_slug(hotel_slug)
    if hotel_data.data:
        hotel = hotel_data.data[0]
        experiences_data = get_experiences_by_city(hotel['city'])
        
        experiences = []
        packages = []
        
        for experience in experiences_data.data:
            if experience['type'] == 9:
                packages.append(experience)
            else:
                experiences.append(experience)
        
        return render_template('main/landing_page.html', hotel=hotel, experiences=experiences, packages=packages)
    return abort(404, description="Hotel not found")

@main_bp.route('/<hotel_slug>/experience/<int:experience_id>')
def experience_details(hotel_slug, experience_id):
    hotel_data = get_hotel_by_slug(hotel_slug)
    if not hotel_data.data:
        return abort(404, description="Hotel not found")
    
    hotel = hotel_data.data[0]
    experience_data = get_experience_by_id(experience_id)
    if experience_data.data:
        experience = experience_data.data[0]
        return render_template('main/experience_details.html', hotel=hotel, experience=experience)
    else:
        return abort(404, description="Experience not found")