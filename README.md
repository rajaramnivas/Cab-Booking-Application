# 🚖 Cab Booking Application

## 📌 Project Overview

The **Cab Booking Application** is a web-based application developed using Python and Django that simplifies the cab booking process by connecting customers and drivers through a centralized platform.

The application provides role-based functionality that allows customers to register, log in, manage cab bookings, and track trip status, while drivers can log in, view booking requests, and accept rides. It uses Django ORM and MySQL for database management and data operations.

This project demonstrates the practical implementation of web development concepts, user authentication, database integration, and CRUD operations.

## ✨ Key Features

- **User Registration and Login:** Supports customer and driver authentication.
- **Role-Based Functionality:** Provides separate features for customers and drivers.
- **Cab Booking Management:** Enables customers to create and manage bookings.
- **Ride Acceptance:** Allows drivers to accept available ride requests.
- **Trip Status Tracking:** Helps users follow the status of their bookings.
- **Database Management:** Stores and manages application data using MySQL.
- **Django Admin:** Supports administrative management where configured.

## 🛠️ Technologies Used

- **Programming Language:** Python
- **Backend Framework:** Django
- **Database:** MySQL
- **ORM:** Django ORM
- **Frontend:** HTML5, CSS3
- **Version Control:** Git and GitHub

## ⚙️ Installation and Setup

### Prerequisites

Make sure you have the following installed:

- Python
- pip
- MySQL Server
- Git

### 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd YOUR_PROJECT_FOLDER
```

Replace the repository URL and folder name with your actual values.

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate the environment.

**Windows:**
```bash
venv\Scripts\activate
```

**macOS/Linux:**
```bash
source venv/bin/activate
```

### 3. Install Dependencies

If your repository includes a `requirements.txt` file:

```bash
pip install -r requirements.txt
```

### 4. Configure the Database

Create a MySQL database and configure the database connection in your Django settings file.

Use environment variables or a local configuration file for sensitive credentials. Never commit database passwords or secret keys to GitHub.

### 5. Apply Database Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create an Administrator Account

```bash
python manage.py createsuperuser
```

### 7. Run the Development Server

```bash
python manage.py runserver
```

Open the local development address displayed in your terminal in a web browser.

## 🎯 Learning Outcomes

- Practical experience with Python and Django web development.
- Understanding user authentication and role-based access.
- Working with Django ORM and relational databases.
- Implementing CRUD operations and booking workflows.
- Learning Git and GitHub for source code management.

## 🔮 Future Enhancements

- Integrate online payment functionality.
- Add GPS-based driver tracking.
- Implement fare estimation.
- Add booking notifications.
- Develop a responsive interface for mobile devices.

## 👨‍💻 Developer

**Rajaram S**

Python Full Stack Developer

- GitHub: https://github.com/rajaramnivas
- LinkedIn: https://www.linkedin.com/in/rajurajaram26/

---

⭐ If you find this project useful, feel free to explore the repository and share feedback.
