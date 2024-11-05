# Job Tracker Application

## Overview
The Job Tracker is a Django-based web application that helps users manage their job applications efficiently. It includes features for tracking job applications, viewing upcoming interviews, recording interview questions, and more. The app provides a dashboard with insightful statistics on applications and interview schedules.
## Key Features
**User Registration and Authentication**: Register new users, log in, and maintain sessions securely.
**Job Application Management**: Add, edit, and list job applications with statuses like "Rejected," "Shortlisted," or "Interview Scheduled."
**Dashboard**: View statistics for total applications, rejections, shortlisted applications, and upcoming interviews.
**Interview Schedule Tracking**: Track interviews scheduled for the future and view details on the dashboard.
**Interview Questions Storage**: Add and retrieve interview questions by company to help with interview preparation.
**Pagination**: Pagination support for application lists and today's applications for a better user experience.
Logout Functionality: Secure logout feature for users.

## Technologies Used
- **Backend:** Django Framework, Django ORM
- **Frontend:** HTML, CSS
- **Database:** MySQL
- **Authentication:** Django's built-in user authentication system

## Installation

### Prerequisites
- Python 3.x
- Django
- MySQL

### Steps
1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/Job_Tracker.git
    cd Job_Tracker
    ```

2. **Create a virtual environment:**
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows, use `env\Scripts\activate`
    ```

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up the database:**
    - Configure your database settings in `settings.py`.
    - Run migrations:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. **Create a superuser:**
    ```bash
    python manage.py createsuperuser
    ```

6. **Run the development server:**
    ```bash
    python manage.py runserver
    ```

7. **Access the application:**
    - Open your web browser and navigate to `http://127.0.0.1:8000/`.

## Usage

1. **Register** 
 - for a new account or log in if you already have one.
2. **Add Job Applications** 
 - through the "Add Job Application" form.
3. **Track Applications**
 - on the "Job Application List" page with pagination support.
4. **View Today’s Applications**
 - to see jobs applied for today.
5. **Use the Dashboard**
 - to get insights on applications and manage interview questions.
6. **Track Upcoming Interviews**
 - on the "Upcoming Interviews" page.
7. **Add Interview Questions**
 - specific to companies to help with preparation.
8. **Log Out**
 - securely when done.

## Code Overview

## views.py

- **register**: Handles user registration and automatically logs them in.
- **job_application_add:** Allows logged-in users to add new job applications.
- **job_application_list:** Displays a paginated list of the user’s job applications.
- **todays_applications_view:** Lists job applications submitted on the current date.
- **job_application_detail:*** Shows detailed information for a specific job application.
- **job_application_edit:** Allows users to edit their existing job applications.
- **dashboard:** Main user dashboard displaying statistics and the option to add interview questions.
- **upcoming_interviews_view:** Lists upcoming interviews for the user.
- **rejected_companies_view:** Displays a list of companies where the user’s applications were rejected.
- **shortlisted_applications_view:** Lists applications marked as "Shortlisted."
- **add_question:** Allows adding interview questions for specific companies.
- **interview_questions:** Shows a list of interview questions filtered by the logged-in user.
- **logout_view:** Handles user logout and redirects to the login page.
## models.py
- **JobApplication:** Model to store job applications with fields like company name, status, date applied, and interview date.
- **InterviewQuestion:** Model to store interview questions, each associated with a specific company and user.
## forms.py
- **JobApplicationForm:** Form to handle job application input.
- **UserRegistrationForm:** Form to handle user registration.
## Contributing
If you want to contribute to this project:

## Fork the repository.
Create a new branch (git checkout -b feature/new-feature).
Make your changes and commit them (git commit -m 'Add new feature').
Push to the branch (git push origin feature/new-feature).
Open a pull request.
License
This project is licensed under the MIT License. See the LICENSE file for details.

### Contact
For any inquiries, please contact:

- Name: Mohammed Abdul Waseem
- Email: abdulwaseem9777@gmail.com
- Location: Hyderabad, India



