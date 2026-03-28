# 📝 Flask Job Application Portal

A full-stack web application built with Python and Flask. This system handles frontend form submissions, stores applicant data securely in a local SQLite database using SQLAlchemy, and automatically dispatches a confirmation email to the applicant via Flask-Mail.

<img width="1741" height="897" alt="Job-Application-Form" src="https://github.com/user-attachments/assets/ab6b6799-2d80-4197-968b-bc2221e82fa0" />
<img width="1813" height="865" alt="Submission-mail" src="https://github.com/user-attachments/assets/dd69d79b-41a1-43e8-8fa6-199a17f7629d" />


## 🧠 System Architecture
1. **Frontend Interface:** A responsive HTML5 form styled with Bootstrap 5. It collects applicant details (Name, Email, Start Date, Occupation) and uses Jinja2 templating to flash success messages from the server.
2. **Database Engine:** Flask-SQLAlchemy maps the Python `Form` class directly to a relational SQLite database (`data.db`). It automatically initializes the schema and commits session data persistently.
3. **Notification Service:** Flask-Mail establishes an SMTP connection to generate and send a formatted confirmation email instantly upon a successful database commit.

## 🛠️ Tech Stack
* **Backend Framework:** Python 3.12, Flask
* **Database:** SQLite, Flask-SQLAlchemy
* **Email Provider:** Flask-Mail (SMTP configuration)
* **Frontend:** HTML5, Bootstrap 5 (CDN), jQuery

