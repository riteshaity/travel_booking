# Travel Booking Web App

Welcome to **Travel Booking**, a Django-based web application that makes planning your trips easy and seamless! Whether you’re booking a flight, train, or bus, this app allows users to browse travel options, manage bookings, and stay on top of their travel plans—all in one place.

---

## 🚀 Features

### User Management
- **Register, Login & Logout**: Secure authentication using Django’s built-in system.
- **Profile Management**: Update your username, email, and personal details anytime.

### Travel Options
- Browse different travel modes: **Flight, Train, Bus**.
- View travel details including **source, destination, date & time, price, and available seats**.
- Filter travel options by type, source, destination, or date to find the perfect journey.

### Booking System
- **Book your trip** by selecting available seats and confirming your travel.
- Each booking tracks:
  - Number of seats booked
  - Total price
  - Booking date
  - Status (Confirmed / Cancelled)
- **View your bookings**: Keep track of current and past bookings.
- **Cancel bookings**: Flexible cancellations directly from your dashboard.

### Frontend
- Clean, responsive design using **Bootstrap 5**.
- Mobile-friendly and easy-to-use interface.

---

## 🛠️ Technology Stack

- **Backend:** Django 5
- **Frontend:** HTML, CSS, Bootstrap 5
- **Database:** MySQL
- **Authentication:** Django built-in user model
- **Deployment:** Localhost / can be deployed on any server

---

## 📦 Installation & Setup

1. Clone this repository:
   ```bash
   git clone <your-repo-url>
   cd travel_booking
Create and activate a virtual environment:
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # macOS/Linux

pip install -r requirements.txt

CREATE DATABASE travel_booking_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER 'db_user'@'localhost' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON travel_booking_db.* TO 'db_user'@'localhost';
FLUSH PRIVILEGES;

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'travel_booking_db',
        'USER': 'db_user',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

Run migrations and start the server:
python manage.py migrate
python manage.py runserver


## 📸 Screenshots
<img width="1894" height="951" alt="Screenshot 2025-08-29 040102" src="https://github.com/user-attachments/assets/4d4d378b-6ae6-4d71-b654-b510d42be949" />
<img width="1350" height="607" alt="Screenshot 2025-08-29 040115" src="https://github.com/user-attachments/assets/3b5ab980-0a82-4e04-b84f-91b5d9b23c38" />
<img width="1920" height="1020" alt="Screenshot 2025-08-29 040340" src="https://github.com/user-attachments/assets/078af360-70f8-4733-85b4-a39a5734523e" />

## 💡 Notes
Initial data can be added via Django admin or fixtures.

Ensure MySQL service is running before starting the server.


## Made with ❤️ by Aity Riteshraj
