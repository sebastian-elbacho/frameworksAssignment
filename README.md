## Framework Assignment
FrameworkApp – Django Project Management & Messaging App

FrameworkApp is a web application built with **Django** and **PostgreSQL** that allows users to:

- register and log in
- manage their personal profile
- create and manage projects
- send and receive messages (inbox)
- work with simple roles (user/admin)
- enjoy a modern Bootstrap 5 based UI with JavaScript enhancements

This project was developed as part of a university assignment to demonstrate full-stack web development skills: backend logic, database integration, frontend design and deployment readiness.

---

## Features

###  User Management

- User registration with custom profile (phone, address, city).
- Login and logout using Django’s authentication system.
- Edit profile (both core `User` and related `UserProfile` data).
- Bootstrap-based registration and login forms using **django-crispy-forms** and **crispy-bootstrap5**.
- Toast notifications (Bootstrap toasts) after key actions such as registration, profile updates, project changes, etc.

### Security

- Passwords are **never stored in plain text**.
- Django’s built-in authentication uses **PBKDF2 with a salt** by default, which fulfils the requirement for secure, encrypted storage of user passwords.
- Access to core views (profile, projects, inbox, messaging) is protected with `@login_required`.
- Simple role-based access:
  - `UserProfile.role` can be `"user"` or `"admin"`.
  - Regular users see only their own projects.
  - Admin users can view all projects.

###  Projects

- Authenticated users can:
  - create new projects,
  - edit existing projects,
  - delete their own projects,
  - view a list of projects in a modern, responsive table.
- Admins can see all projects in the system.
- Project fields include basic information such as name, dates and status (extendable).

### Messaging (Inbox)

- Authenticated users can send messages to other users.
- Each user has an inbox that shows messages received, ordered from newest to oldest.
- The inbox view is styled using Bootstrap cards for clear readability.

###  UI & UX Enhancements

- Layout built with **Bootstrap 5** and a custom stylesheet (`static/teams/style.css`).
- Consistent page structure using a base template: `teams/layout.html`.
- Responsive design: works well on desktop and mobile devices.
- JavaScript-driven features:
  - **Real-time password validation** on the registration form.
  - **Bootstrap toast notifications** for feedback.
  - **Collapsible section** on the home page for additional technical information.

###  Extensibility & Modular Design

- Django project structure with separate apps:
  - `teams` – projects, messaging, profiles, main UI
  - `users` – prepared for further user-related logic (if needed)
- Easy to extend with:
  - additional apps (e.g. reports, notifications),
  - third-party APIs,
  - a different frontend (React, Vue, etc.),
  - a different database backend (via `DATABASES` in `settings.py`).

---

## Tech Stack

- **Backend:** Django 5
- **Database:** PostgreSQL
- **Frontend:** HTML, CSS, Bootstrap 5, JavaScript
- **Forms:** django-crispy-forms, crispy-bootstrap5
- **Server (for deployment):** gunicorn (WSGI)
- **OS:** Development on macOS (but works on any OS supporting Python & PostgreSQL)

---

## Project Structure (simplified)

```text
config/           # Django project settings and URLs
teams/            # Main app: views, models, forms, templates
users/            # Additional user app (optional extension)
static/teams/     # Custom CSS, JS and images
templates/teams/  # HTML templates (layout, home, login, register, etc.)
manage.py         # Django management script
requirements.txt  # Python dependencies
Procfile          # Process definition for gunicorn (deployment)
README.md         # This file
```

## Local Setup - How to Run the App

1. Clone the repository
git clone <your_repo_url>
cd frameworksAssignment

2. Create and activate a virtual environment (optional but recommended).
python3 -m venv venv        #macOS
source venv/bin/activate  # macOS / Linux
venv\Scripts\activate   # Windows

3. Install dependencies
pip install -r requirements.txt

4. Configure PostgreSQL
Make sure you have a PostgreSQL database created, e.g.:
Database name: framework_db
User: postgres
Password: tyju
Host: localhost
Port: 5432

In config/settings.py:

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "framework_db",
        "USER": "postgres",
        "PASSWORD": "tyju",
        "HOST": "localhost",
        "PORT": "5432",
    }
}

5. Apply migrations
python manage.py makemigrations
python manage.py migrate

6. Create a superuser (optional, for admin access)
python3 manage.py createsuperuser

7. Collect static files (for production / deployment)
python3 manage.py collectstatic

8. Run the development server
python3 mange.py runserver 

## visit: http://127.0.0.1:8000/











