# journal-website-v3
Below is a template for the `README.md` file that provides a setup guide for your journal website project on ancient science and medicine using PHP and Django.

```markdown
# Ancient Science and Medicine Journal Website

This project is a web-based platform for submitting and publishing research papers on ancient science and medicine. The website allows researchers to upload papers, which are then reviewed and published after approval by the admin. Built using **Django** for content management and **PHP** for file handling, this project offers functionality such as user registration, paper submission, peer review, search, and download options for research papers.

## Features
- User registration and authentication
- Paper submission and file upload
- Admin panel for managing research papers and reviews
- Search and filter functionality for research papers
- Download options for published papers
- Review system for submitted papers
- Categorization by topics and keywords

## Tech Stack
- **Backend**: Django (Python), PHP
- **Frontend**: HTML, CSS (Bootstrap or Tailwind), JavaScript
- **Database**: PostgreSQL (or MySQL)
- **Server**: Apache or Nginx
- **Deployment**: Gunicorn or uWSGI

---

## Setup Guide

### Prerequisites
Make sure you have the following installed:
- Python 3.x
- Django
- PHP 7.x or 8.x
- PostgreSQL or MySQL
- Apache or Nginx web server
- Git for version control

### Installation Steps

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/ancient_science_journal.git
   cd ancient_science_journal
   ```

2. **Create and Activate Virtual Environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Python Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up the Database**
   - **PostgreSQL**: Install PostgreSQL and create a database for the project.
     ```bash
     sudo -u postgres psql
     CREATE DATABASE journal_db;
     CREATE USER journal_user WITH PASSWORD 'yourpassword';
     ALTER ROLE journal_user SET client_encoding TO 'utf8';
     ALTER ROLE journal_user SET default_transaction_isolation TO 'read committed';
     ALTER ROLE journal_user SET timezone TO 'UTC';
     GRANT ALL PRIVILEGES ON DATABASE journal_db TO journal_user;
     ```

   - **MySQL**: If using MySQL, replace PostgreSQL setup commands accordingly.

5. **Configure Django Settings**
   - In the `settings.py` file, update the `DATABASES` configuration to match your database:
     ```python
     DATABASES = {
         'default': {
             'ENGINE': 'django.db.backends.postgresql',  # Use 'mysql' for MySQL
             'NAME': 'journal_db',
             'USER': 'journal_user',
             'PASSWORD': 'yourpassword',
             'HOST': 'localhost',
             'PORT': '5432',  # For PostgreSQL; use '3306' for MySQL
         }
     }
     ```

6. **Run Migrations**
   Run the database migrations to set up the database schema:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

7. **Create a Superuser (Admin)**
   Create an admin user for the Django admin interface:
   ```bash
   python manage.py createsuperuser
   ```

8. **Run the Development Server**
   Start the development server to view the project locally:
   ```bash
   python manage.py runserver
   ```

   The site should now be available at `http://127.0.0.1:8000/`.

---

### Setting up PHP for File Handling

1. **Install PHP** (if not already installed):
   ```bash
   sudo apt update
   sudo apt install php libapache2-mod-php php-mysql
   ```

2. **Create Upload Directory**
   Ensure you have a directory for paper uploads. Create it in the project root:
   ```bash
   mkdir -p uploads/papers
   ```

3. **Set Up PHP File Uploads**
   Add your PHP upload script in a separate folder (`php_scripts`) and ensure Apache is configured to handle PHP requests.

   Sample upload script (`upload.php`):
   ```php
   <?php
   if (isset($_FILES['paper'])) {
       $upload_dir = 'uploads/papers/';
       $file_name = basename($_FILES['paper']['name']);
       $upload_file = $upload_dir . $file_name;

       if (move_uploaded_file($_FILES['paper']['tmp_name'], $upload_file)) {
           echo "The file has been uploaded.";
       } else {
           echo "Sorry, there was an error uploading your file.";
       }
   }
   ?>
   ```

   Update your Django form to submit files to this script.

---

### Deployment

1. **Set Up Gunicorn or uWSGI** for production:
   ```bash
   pip install gunicorn
   gunicorn ancient_science_journal.wsgi
   ```

2. **Configure Apache/Nginx** to serve the Django app and the PHP scripts.

3. **Enable HTTPS**: For production, set up SSL using Let's Encrypt or another certificate provider to secure your site.

---

### Usage
1. Navigate to `http://127.0.0.1:8000/admin/` to access the Django admin panel and manage research papers.
2. Users can register, log in, submit papers, and search through the database of published research.

---

### License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

### Contributing
Feel free to submit pull requests or open issues to contribute to the project.

```

This `README.md` file provides a detailed setup guide for your project. You can customize the repository name, license, and other sections to match your project specifics.