# Job Project

This is a Django-based Job Project that allows employers to post jobs and job seekers to apply directly through the platform. The project includes features such as user authentication, job posting (with salary ranges), resume upload for applications, search & filtering on the home page, pagination, and user profiles.

## Features

- **Employers** can create, update, and delete **their own** job posts.
- **Job seekers** can apply to jobs by uploading a resume and optionally providing a cover letter.
- A **home page** with a search box and advanced filtering by job title, country, city, category, and subcategory.
- **Pagination** for job listings.
- **User profiles** for both employers and job seekers.
- Dockerized for production deployment.

## Requirements

- Python 3.10+
- PostgreSQL (or another supported database; adjust settings accordingly)
- Docker (for containerization)

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Alirezz2020/job.git
2. **Create and activate a virtual environment:**
```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
   
   pip install --upgrade pip #Install dependencies:
   pip install -r requirements.txt

   python manage.py migrate #Run migrations
   
   python manage.py createsuperuser #Create a superuser
   
   python manage.py runserver #Run the development server
   #The application will be available at http://localhost:8000.


   
   

   

