# 🚗 License Plate Recognition & Smart Parking System

An intelligent parking management system built with **Python, OpenCV, Flask, and SQL**, capable of detecting vehicle license plates automatically from images, storing entry/exit data, and calculating parking fees in real-time.

---

## 🧩 Features

✅ **Automatic Plate Detection** – Uses OpenCV & Tesseract OCR to detect and extract license plate numbers  
✅ **SQL Database Integration** – Stores all vehicle data with timestamps, durations, and fees  
✅ **Flask Web Dashboard** – View, add, and manage vehicles via a clean web interface  
✅ **Smart Fee Calculation** – Calculates parking fees automatically based on duration  
✅ **Expandable Design** – Can integrate live camera feed or machine learning models for more accuracy  

---

## 🏗️ Project Structure

```
LicensePlateParkingSystem/
│
├── app.py                    # Flask backend (main entry point)
├── requirements.txt          # Dependencies
├── README.md                 # Project documentation
│
├── /templates                # HTML templates
│   ├── index.html
│   ├── add_vehicle.html
│   └── exit_vehicle.html
│
├── /static                   # Static files
│   └── style.css
│
├── /scripts                  # Backend modules
│   ├── detect_plate.py
│   └── database_ops.py
│
└── /database                 # SQLite database
    └── parking.db
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone this repository
```bash
git clone https://github.com/ehsanul01/LicensePlateParkingSystem.git
cd LicensePlateParkingSystem
```

### 2️⃣ Create and activate a virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Run the application
```bash
python app.py
```

Then open [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser 🚀

---

## 🧠 How It Works

1. Upload a car image (from `/add` page).  
2. The system detects the license plate and stores it in an SQLite database.  
3. When the vehicle exits (`/exit` page), it calculates duration and fee automatically.  
4. Dashboard (`/`) shows all vehicle entries, exits, and total charges.

---

## 🖥️ Technologies Used

- **Python 3.14**
- **Flask** (for web framework)
- **OpenCV** (for image processing)
- **pytesseract** (for OCR)
- **SQLite3** (for database)
- **HTML/CSS** (for frontend)

---

## 📸 Future Enhancements

- Live camera feed for real-time detection  
- Vehicle type classification (car, bike, truck)  
- User login system and admin dashboard  
- Cloud database support (MySQL/PostgreSQL)  
- Email/SMS notifications for registered users  

---



## 👨‍💻 Author

**Ehsanul Haque**  
🧠 Computer Science @ University at Buffalo  
📍 Buffalo, NY  
🔗 [LinkedIn](https://www.linkedin.com/in/ehsanul-haque/) • [GitHub](https://github.com/ehsanul01)

---

### ⭐ If you like this project, please give it a star on GitHub!
