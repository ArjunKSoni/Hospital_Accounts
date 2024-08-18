Hospital API
============

This is a Django-based API for managing hospital operations, including doctors, patients, departments, and patient records.

Table of Contents
-----------------

*   [Features](#features)
*   [Installation](#installation)
*   [Usage](#usage)
*   [API Endpoints](#api-endpoints)
*   [Authentication](#authentication)

Features
--------

*   User authentication (login, signup, logout) for both doctors and patients
*   CRUD operations for doctors, patients, departments, and patient records
*   Role-based access control (staff vs non-staff users)
*   Department-wise listing of doctors and patients

Installation
------------

### Using Docker

1.  Pull the Docker image:
    
        docker pull arjunksoni/hospital_account:dev
    
2.  Run the Docker container:
    
        docker run -p 10000:10000 arjunksoni/hospital_account:dev
    

### Manual Installation

1.  Clone the repository:
    
        git clone https://github.com/ArjunKSoni/Hospital_Accounts.git
        cd Hospital_Accounts
        cd hospital
    
3.  Create a virtual environment and activate it:
    
        python -m venv venv
        source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    
4.  Install the required packages:
    
        pip install -r requirements.txt
    
5.  Apply migrations:
    
        python manage.py migrate
    
6.  Create a superuser (admin):
    
        python manage.py createsuperuser
    
7.  Run the development server:
    
        python manage.py runserver 10000
    

Usage
-----

After starting the server, you can access the API at `http://localhost:10000/`.

API Endpoints
-------------

### Authentication

*   Login: `POST /`
*   Signup (Patient): `POST /signup_patient/`
*   Signup (Doctor): `POST /signup_doctor/`
*   Logout: `GET /logout`

### Doctors

*   List all doctors: `GET /api/v1/accounts/doctors/`
*   Create a doctor: `POST /api/v1/accounts/doctors/`
*   Get, update, or delete a specific doctor: `GET/PUT/DELETE /api/v1/accounts/doctors/<id>/`

### Patients

*   List all patients: `GET /api/v1/accounts/patients/`
*   Create a patient: `POST /api/v1/accounts/patients/`
*   Get, update, or delete a specific patient: `GET/PUT/DELETE /api/v1/accounts/patients/<id>/`

### Patient Records

*   List all patient records: `GET /api/v1/accounts/patient_records/`
*   Create a patient record: `POST /api/v1/accounts/patient_records/`
*   Get, update, or delete a specific patient record: `GET/PUT/DELETE /api/v1/accounts/patient_records/<id>/`

### Departments

*   List all departments: `GET /api/v1/accounts/departments/`
*   Create a department: `POST /api/v1/accounts/departments/`
*   Get doctors in a department: `GET /api/v1/accounts/department/<did>/doctors/`
*   Get patients in a department: `GET /api/v1/accounts/department/<did>/patients/`

Authentication
--------------

This API uses session-based authentication. Users must log in to access protected endpoints. Different views have different access levels based on whether the user is staff (doctor) or non-staff (patient).

*   Patients can only view their own records.
*   Doctors (staff) can view and manage all data.

Make sure to include proper authentication headers when making requests to protected endpoints.
