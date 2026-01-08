{\rtf1\ansi\ansicpg1252\cocoartf2709
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;\f1\froman\fcharset0 Times-Roman;\f2\ftech\fcharset77 Symbol;
}
{\colortbl;\red255\green255\blue255;\red0\green0\blue0;}
{\*\expandedcolortbl;;\cssrgb\c0\c0\c0;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh11060\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 Link to the assignment: \
\
{\field{\*\fldinst{HYPERLINK "https://frameworksassignment-7.onrender.com/"}}{\fldrslt https://frameworksassignment-7.onrender.com}}\
\
\
\pard\pardeftab720\sa240\partightenfactor0

\fs26\fsmilli13333 \cf2 \expnd0\expndtw0\kerning0
Instructions: How to Deploy My Django Web Application on Render (Beginner-Friendly) 
\f1\fs24 \

\f0\fs26\fsmilli13333 1. Preparing the Project 
\f1\fs24 \

\f0\fs26\fsmilli13333 I uploaded my entire Django project to GitHub and made sure the requirements.txt file was included. Render uses this file to install all the necessary Python packages. 
\f1\fs24 \

\f0\fs26\fsmilli13333 2. Creating a Web Service on Render 
\f1\fs24 \

\f0\fs26\fsmilli13333 - Log in to Render: https://dashboard.render.com 
\f1\fs24 \

\f0\fs26\fsmilli13333 - Click New 
\f2 \uc0\u8594  
\f0 Web Service 
\f1\fs24 \

\f0\fs26\fsmilli13333 - Select your GitHub repository 
\f1\fs24 \

\f0\fs26\fsmilli13333 - Choose Environment: Python 
\f1\fs24 \

\f0\fs26\fsmilli13333 - Build Command: 
\f1\fs24 \

\f0\fs26\fsmilli13333 pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate 
\f1\fs24 \

\f0\fs26\fsmilli13333 - Start Command:\uc0\u8232 gunicorn config.wsgi:application - Create the service 
\f1\fs24 \

\f0\fs26\fsmilli13333 3. Creating a PostgreSQL Database\uc0\u8232 - Click New 
\f2 \uc0\u8594  
\f0 PostgreSQL\uc0\u8232 - Choose the Free plan\u8232 - After the database is created, go to the Connections tab\u8232 - Copy the Internal Database URL (example): postgresql://user:password@hostname:5432/databasename 
\f1\fs24 \

\f0\fs26\fsmilli13333 4. Adding the Environment Variable\uc0\u8232 - Go to Web Service 
\f2 \uc0\u8594  
\f0 Settings 
\f2 \uc0\u8594  
\f0 Environment Variables - Add a new variable:\uc0\u8232 Name: DATABASE_URL 
\f1\fs24 \

\f0\fs26\fsmilli13333 Value: (paste the Internal Database URL) - Save the changes 
\f1\fs24 \

\f0\fs26\fsmilli13333 5. Redeploying the Application\uc0\u8232 - Click Manual Deploy 
\f2 \uc0\u8594  
\f0 Clear build cache & deploy 
\f1\fs24 \

\f0\fs26\fsmilli13333 6. Accessing the Application\uc0\u8232 Render will generate a URL such as: https://myapp.onrender.com\u8232 Opening this link displays the running Django application. 
\f1\fs24 \

\f0\fs26\fsmilli13333 Summary: 
\f1\fs24 \

\f0\fs26\fsmilli13333 The project is hosted on GitHub, Render builds it automatically, the database is connected using DATABASE_URL, and the app runs with gunicorn. Deployment requires only one manual action after configuration. 
\f1\fs24 \
}