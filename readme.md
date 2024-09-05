
# ACM Induction Management System (Inductor)

This document provides an overview of ACM Inductor, a web application designed to streamline and simplify the club induction process for both administrators and applicants.

## Project Overview

ACM Inductor automates and organizes the induction process, allowing for efficient management of applicants, interview schedules, and panel assignments. Applicants can easily submit applications and receive updates regarding their status.

## Features
**1. Applicant Submission Process**

* Applicants access a public form to submit their basic details.
* Submitted data is stored in the database, and the application status is marked as "Pending."

**2. Admin Workflow (Interview Panel)**

* Admins (Interview Panel members) log in using provided credentials.
* The admin panel provides a dashboard with statistics on applicants.

**3. Managing Applicants**

* Admins can view detailed information about individual applicants.
* For pending applicants, admins can schedule interviews and assign panels.
* After interviews, admins can provide feedback and ratings.

**4. Changing Applicant Status**

* Admins can mark applicants as "Selected," "Rejected," or "Scheduled."

**5. Automated Notifications**

 -   Send automatic notifications to applicants based on their interview status:
        -   Scheduled: Interview date and time.
        -   Selected: Selection confirmation.
        -   Rejected: Rejection notification.

**6. REST API Access**

* API included for accessing the data outside the website as well.
* Restricted access to authorized Interview Panel members.
 * Does not expose sensitive data like passwords.

**7. Reporting**

* The admin panel generates reports on the induction process.


**8. Security and Permissions**

* The website ensures secure access and data protection.


## Dependencies

Before getting started, ensure you have the following dependencies installed:

-   Python (>= 3.x)
-   Django (>= 5.0.6)
-   Django REST Framework (>= 3.15.0)

## Installing Dependencies

Use the following command to install all the necessary Python packages:

```bash
pip install -r requirements.txt
```

## Getting Started

1.  Clone the repository:



```bash
git clone [https://github.com/yourusername/ACM-Inductions.git](https://github.com/RockingAayush/ACM-Induction.git)
```


2.  Navigate to the project directory:


```bash
cd ACM-Inductions/mysite/
```

3.  Install the required dependencies:


```bash
pip install -r requirements.txt
```


4.  Run the server:

```bash
python manage.py runserver
```

5.  Access the web app in your browser:

```
http://127.0.0.1:8000/
```

## Email Notification Setup

1.  Configure your email settings in the `mysite/settings.py` file under the `EMAIL_BACKEND` section.
2.  Update the sender email in `management/views.py` by replacing the placeholder with your email address.

## Login Credentials (For Demo Purposes)

-   Name: Aayush
-   Password: ABC//123

These credentials are for `InterviewPanel` members and can be managed through the Django Admin Panel.

To access the django-admin panel visit `http://127.0.0.1:8000/admin`.

Admin Login Credentials are:
- username: aayush
- password: 123456
## API Documentation

The project includes a `RESTful API` restricted to authorized Interview Panel members. Visit the API Documentation section in the Admin Dashboard for detailed instructions.


## Contact

For any questions, feedback, or suggestions, please contact at rastogi.bkn@gmail.com

