import os  # Add this import if needed
from flask import Blueprint, render_template, jsonify, request, flash
from database import get_stored_procedures, get_procedure_definition, test_connection, get_available_drivers
from config import save_config
import csv

main_routes = Blueprint('main', __name__)

@main_routes.route('/')
def index():
    display_names, full_names, error = get_stored_procedures()
    return render_template(
        'index.html', 
        display_names=display_names, 
        full_names=full_names, 
        error=error,
        zip=zip  # Pass the zip function to the template
    )

@main_routes.route('/mark_complete', methods=['POST'])
def mark_complete():
    data = request.get_json()
    procedure_name = data.get('procedure_name')

    if not procedure_name:
        return jsonify({'success': False, 'message': 'Procedure name is required.'}), 400

    # Write the procedure name and status to the CSV file
    try:
        with open('completed_procedures.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([procedure_name, 'completed'])
        return jsonify({'success': True, 'message': 'Procedure marked as complete.'})
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500

@main_routes.route('/get_procedure/<path:procedure_name>')
def get_procedure(procedure_name):
    definition, error = get_procedure_definition(procedure_name)
    if error:
        return jsonify({'error': error})
    return jsonify({'definition': definition})

@main_routes.route('/save_config', methods=['POST'])
def save_config_route():
    config = {
        'driver': request.form['driver'],
        'server': request.form['server'],
        'database': request.form['database'],
        'trusted_connection': request.form.get('trusted_connection', 'no'),
        'username': request.form.get('username', ''),
        'password': request.form.get('password', '')
    }

    success, message = test_connection(config)
    if success:
        save_config(config)
        flash('Configuration saved successfully!')
    else:
        flash(f'Configuration error: {message}')

    return '', 204

@main_routes.route('/test_connection', methods=['POST'])
def test_connection_route():
    config = {
        'driver': request.form['driver'],
        'server': request.form['server'],
        'database': request.form['database'],
        'trusted_connection': request.form.get('trusted_connection', 'no'),
        'username': request.form.get('username', ''),
        'password': request.form.get('password', '')
    }

    success, message = test_connection(config)
    return jsonify({'success': success, 'message': message})