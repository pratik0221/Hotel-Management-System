
# 🏨 Hotel Management System (Web Version)

A simple **Hotel Management System** built using **Python (Flask)**, **MySQL**, **HTML**, and **CSS**.  
This project allows hotel admins to manage **Guests, Rooms, and Billing** with a clean web interface.  

---

## 🚀 Features
- 👤 **Guest Management** – Add and view hotel guests  
- 🏠 **Room Management** – Add rooms, view availability, and room details  
- 💳 **Billing System** – Generate bills for guests based on room price and stay duration  
- 📊 **MySQL Database** – Persistent storage for all records  

---

## 🛠️ Tech Stack
- **Frontend:** HTML, CSS  
- **Backend:** Python (Flask Framework)  
- **Database:** MySQL  
- **Server:** Flask Development Server  

---

## 📂 Project Structure
hotel_management/
│
├── app.py # Flask backend
├── templates/ # HTML templates
│ ├── index.html
│ ├── guests.html
│ ├── rooms.html
│ ├── bills.html
│
├── static/ # CSS, JS, images
│ ├── style.css
│
├── requirements.txt # Python dependencies
└── README.md # Project documentation


---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/hotel-management-system.git
cd hotel-management-system

2️⃣ Create Virtual Environment (optional but recommended)
python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Setup MySQL Database

Login to MySQL and run:

CREATE DATABASE hotel_web;
USE hotel_web;

CREATE TABLE guests (
    guest_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    phone VARCHAR(15) NOT NULL,
    email VARCHAR(100)
);

CREATE TABLE rooms (
    room_id INT AUTO_INCREMENT PRIMARY KEY,
    room_number VARCHAR(10) UNIQUE NOT NULL,
    room_type VARCHAR(50) NOT NULL,
    price_per_night INT NOT NULL,
    status ENUM('available','occupied') DEFAULT 'available'
);

CREATE TABLE bills (
    bill_id INT AUTO_INCREMENT PRIMARY KEY,
    guest_id INT,
    room_id INT,
    check_in DATETIME,
    check_out DATETIME,
    total_amount DECIMAL(10,2),
    payment_status ENUM('paid','pending') DEFAULT 'pending',
    FOREIGN KEY (guest_id) REFERENCES guests(guest_id),
    FOREIGN KEY (room_id) REFERENCES rooms(room_id)
);

5️⃣ Update Database Config in app.py
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",   # Change this to your MySQL password
    database="hotel_web"
)

6️⃣ Run the Flask App
python app.py


Now open 👉 http://127.0.0.1:5000/ in your browser.
