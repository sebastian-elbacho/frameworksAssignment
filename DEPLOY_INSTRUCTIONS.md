Link to the assignment: 

https://frameworksassignment-7.onrender.com


Instructions: How to Deploy My Django Web Application on Render (Beginner-Friendly) 
1. Preparing the Project 
I uploaded my entire Django project to GitHub and made sure the requirements.txt file was included. Render uses this file to install all the necessary Python packages. 
2. Creating a Web Service on Render 
- Log in to Render: https://dashboard.render.com 
- Click New → Web Service 
- Select your GitHub repository 
- Choose Environment: Python 
- Build Command: 
pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate 
- Start Command: gunicorn config.wsgi:application - Create the service 
3. Creating a PostgreSQL Database - Click New → PostgreSQL - Choose the Free plan - After the database is created, go to the Connections tab - Copy the Internal Database URL (example): postgresql://user:password@hostname:5432/databasename 
4. Adding the Environment Variable - Go to Web Service → Settings → Environment Variables - Add a new variable: Name: DATABASE_URL 
Value: (paste the Internal Database URL) - Save the changes 
5. Redeploying the Application - Click Manual Deploy → Clear build cache & deploy 
6. Accessing the Application Render will generate a URL such as: https://myapp.onrender.com Opening this link displays the running Django application. 
Summary: 
The project is hosted on GitHub, Render builds it automatically, the database is connected using DATABASE_URL, and the app runs with gunicorn. Deployment requires only one manual action after configuration. 

git add .
clear
'EOF'
Link to the assignment: 

https://frameworksassignment-7.onrender.com


Instructions: How to Deploy My Django Web Application on Render (Beginner-Friendly) 
1. Preparing the Project 
I uploaded my entire Django project to GitHub and made sure the requirements.txt file was included. Render uses this file to install all the necessary Python packages. 
2. Creating a Web Service on Render 
- Log in to Render: https://dashboard.render.com 
- Click New → Web Service 
- Select your GitHub repository 
- Choose Environment: Python 
- Build Command: 
pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate 
- Start Command: gunicorn config.wsgi:application - Create the service 
3. Creating a PostgreSQL Database - Click New → PostgreSQL - Choose the Free plan - After the database is created, go to the Connections tab - Copy the Internal Database URL (example): postgresql://user:password@hostname:5432/databasename 
4. Adding the Environment Variable - Go to Web Service → Settings → Environment Variables - Add a new variable: Name: DATABASE_URL 
Value: (paste the Internal Database URL) - Save the changes 
5. Redeploying the Application - Click Manual Deploy → Clear build cache & deploy 
6. Accessing the Application Render will generate a URL such as: https://myapp.onrender.com Opening this link displays the running Django application. 
Summary: 
The project is hosted on GitHub, Render builds it automatically, the database is connected using DATABASE_URL, and the app runs with gunicorn. Deployment requires only one manual action after configuration. 
'EOF'
Link to the assignment: 

https://frameworksassignment-7.onrender.com


Instructions: How to Deploy My Django Web Application on Render (Beginner-Friendly) 
1. Preparing the Project 
I uploaded my entire Django project to GitHub and made sure the requirements.txt file was included. Render uses this file to install all the necessary Python packages. 
2. Creating a Web Service on Render 
- Log in to Render: https://dashboard.render.com 
- Click New → Web Service 
- Select your GitHub repository 
- Choose Environment: Python 
- Build Command: 
pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate 
- Start Command: gunicorn config.wsgi:application - Create the service 
3. Creating a PostgreSQL Database - Click New → PostgreSQL - Choose the Free plan - After the database is created, go to the Connections tab - Copy the Internal Database URL (example): postgresql://user:password@hostname:5432/databasename 
4. Adding the Environment Variable - Go to Web Service → Settings → Environment Variables - Add a new variable: Name: DATABASE_URL 
Value: (paste the Internal Database URL) - Save the changes 
5. Redeploying the Application - Click Manual Deploy → Clear build cache & deploy 
6. Accessing the Application Render will generate a URL such as: https://myapp.onrender.com Opening this link displays the running Django application. 
Summary: 
The project is hosted on GitHub, Render builds it automatically, the database is connected using DATABASE_URL, and the app runs with gunicorn. Deployment requires only one manual action after configuration. 
