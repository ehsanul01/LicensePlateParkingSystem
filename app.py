from flask import Flask, render_template, request, redirect, url_for
from scripts.detect_plate import detect_license_plate
from scripts.database_ops import init_db, add_vehicle, exit_vehicle, get_all_vehicles
import os

app = Flask(__name__)
init_db()

UPLOAD_FOLDER = "static/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    data = get_all_vehicles()
    return render_template('index.html', vehicles=data)

@app.route('/add', methods=['GET', 'POST'])
def add_vehicle_route():
    if request.method == 'POST':
        file = request.files['image']
        path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(path)
        plate = detect_license_plate(path)
        if plate:
            add_vehicle(plate)
        return redirect(url_for('index'))
    return render_template('add_vehicle.html')

@app.route('/exit', methods=['GET', 'POST'])
def exit_vehicle_route():
    if request.method == 'POST':
        plate = request.form['plate']
        exit_vehicle(plate)
        return redirect(url_for('index'))
    return render_template('exit_vehicle.html')

if __name__ == '__main__':
    app.run(debug=True)