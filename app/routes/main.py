# File: app/routes/main.py
from flask import Blueprint, render_template
from app.services.supabase_service import get_hotel_by_slug, get_experiences_by_city, get_experience_by_id

main_bp = Blueprint('main', __name__)

@main_bp.route('/<hotel_name>')
def hotel_page(hotel_name):
    hotel_data = get_hotel_by_slug(hotel_name)
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
    return "Hotel not found", 404

@main_bp.route('/experience/<int:experience_id>')
def experience_details(experience_id):
    experience_data = get_experience_by_id(experience_id)
    if experience_data.data:
        experience = experience_data.data[0]
        return render_template('main/experience_details.html', experience=experience)
    else:
        return "Experience not found", 404
    
@main_bp.route('/booking/<int:experience_id>')
def booking_page(experience_id):
    experience_data = get_experience_by_id(experience_id)
    if experience_data.data:
        experience = experience_data.data[0]
        return render_template('main/booking_page.html', experience=experience)
    else:
        return "Experience not found", 404