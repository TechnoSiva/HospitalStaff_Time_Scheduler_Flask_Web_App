from flask import render_template, request, redirect, url_for
from app import app
from app.utils import generate_schedule
from app.models import Staff

# Example staff data (in real cases, this would be dynamic)
staff_list = [
    Staff('Dr. Rajesh Sharma', {'shift': 'morning'}, 40),    # Doctor, morning shift
    Staff('Nurse Priya Singh', {'shift': 'night'}, 36),      # Nurse, night shift
    Staff('Dr. Neha Verma', {'shift': 'evening'}, 38),       # Doctor, evening shift
    Staff('Nurse Anjali Iyer', {'shift': 'morning'}, 40),    # Nurse, morning shift
    Staff('Technician Ravi Kumar', {'shift': 'night'}, 32),  # Technician, night shift
    Staff('Dr. Shalini Patel', {'shift': 'night'}, 36),      # Doctor, night shift
    Staff('Nurse Kiran Desai', {'shift': 'morning'}, 34),    # Nurse, morning shift
    Staff('Technician Manish Gupta', {'shift': 'evening'}, 30), # Technician, evening shift
    Staff('Therapist Arjun Reddy', {'shift': 'morning'}, 28),   # Therapist, morning shift
    Staff('Pharmacist Meera Nair', {'shift': 'night'}, 40),   # Pharmacist, night shift
    Staff('Nurse Vinay Joshi', {'shift': 'evening'}, 36),    # Nurse, evening shift
    Staff('Therapist Lakshmi Menon', {'shift': 'morning'}, 40) # Therapist, morning shift
]

@app.route('/')
def index():
    return render_template('index.html', staff=staff_list)

@app.route('/schedule', methods=['GET', 'POST'])
def schedule():
    if request.method == 'POST':
        # In a real app, you could get staff availability/preferences from form data
        # Assuming some input is passed, generate the schedule
        schedule = generate_schedule(staff_list)
        
        # Pass the generated schedule to the template for display
        return render_template('schedule.html', schedule=schedule)

    # For GET requests, just show the schedule page with no schedule initially
    return render_template('schedule.html', schedule={})
