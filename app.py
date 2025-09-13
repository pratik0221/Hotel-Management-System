from flask import Flask, render_template, request, redirect, url_for, flash
import mysql.connector

app = Flask(__name__)
app.secret_key = "hotel_secret"

# Database Connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="hotel_web"
)
cursor = conn.cursor(dictionary=True)

# Home
@app.route("/")
def index():
    return render_template("index.html")

# Guests
@app.route("/guests")
def guests():
    cursor.execute("SELECT * FROM guests")
    data = cursor.fetchall()
    return render_template("guests.html", guests=data)

@app.route("/add_guest", methods=["POST"])
def add_guest():
    name = request.form["name"]
    phone = request.form["phone"]
    email = request.form["email"]
    cursor.execute("INSERT INTO guests (name, phone, email) VALUES (%s,%s,%s)", (name, phone, email))
    conn.commit()
    flash("Guest Added Successfully")
    return redirect(url_for("guests"))

# Rooms
@app.route("/rooms")
def rooms():
    cursor.execute("SELECT * FROM rooms")
    data = cursor.fetchall()
    return render_template("rooms.html", rooms=data)

@app.route("/add_room", methods=["POST"])
def add_room():
    number = request.form["number"]
    rtype = request.form["type"]
    price = request.form["price"]
    cursor.execute("INSERT INTO rooms (room_number, room_type, price_per_night) VALUES (%s,%s,%s)", (number, rtype, price))
    conn.commit()
    flash("Room Added Successfully")
    return redirect(url_for("rooms"))

# Bills
@app.route("/bills")
def bills():
    cursor.execute("""
        SELECT b.bill_id, g.name AS guest, r.room_number, b.check_in, b.total_amount
        FROM bills b
        JOIN guests g ON b.guest_id = g.guest_id
        JOIN rooms r ON b.room_id = r.room_id
    """)
    data = cursor.fetchall()
    return render_template("bills.html", bills=data)

@app.route("/generate_bill", methods=["POST"])
def generate_bill():
    guest_id = request.form["guest_id"]
    room_id = request.form["room_id"]
    days = int(request.form["days"])

    cursor.execute("SELECT price_per_night FROM rooms WHERE room_id=%s", (room_id,))
    room = cursor.fetchone()
    if not room:
        flash("Room not found")
        return redirect(url_for("bills"))

    total = room["price_per_night"] * days
    cursor.execute("INSERT INTO bills (guest_id, room_id, check_in, check_out, total_amount) VALUES (%s,%s,NOW(), DATE_ADD(NOW(), INTERVAL %s DAY), %s)",
                   (guest_id, room_id, days, total))
    cursor.execute("UPDATE rooms SET status='occupied' WHERE room_id=%s", (room_id,))
    conn.commit()

    flash("Bill Generated Successfully")
    return redirect(url_for("bills"))

if __name__ == "__main__":
    app.run(debug=True)
