# TechHub - Training Courses Platform 🚀

## About The Project
**TechHub** is a comprehensive full-stack web application built using the **Django** framework. It serves as a modern platform for browsing and enrolling in technical training courses. The project was developed to demonstrate core software engineering concepts, including database management, state maintenance, and secure user authentication.

## Key Features ✨

* **Database Management:**
    * Designed and implemented relational models for **Courses**, **Categories**, and **Contacts**.
    * Fully integrated with **MariaDB** for persistent data storage.
* **Session-Based "My List":**
    * Developed a dynamic enrollment list (Cart) using **Django Sessions**.
    * Tracks selected courses and calculates the total cost in real-time.
* **User Authentication & Authorization:**
    * Secure **Registration** and **Login** system for students.
    * Enforced access control: The checkout process is restricted to authenticated users only using `@login_required`.
* **Contact Management:**
    * A dedicated "Contact Us" feature that saves user inquiries directly to the database.
    * Allows administrators to review and manage messages via the Django Admin panel.
* **Responsive UI/UX:**
    * Modern and clean interface styled with **Bootstrap 5**.
    * Fully responsive design for mobile and desktop views.

## Built With 🛠️
* **Backend:** Python 3, Django
* **Database:** MariaDB (MySQL)
* **Frontend:** HTML5, CSS3, Bootstrap 5 (via `django-bootstrap5`)

## How to Run 💻

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/RaghadMAsiri/Django_FinalProject.git](https://github.com/RaghadMAsiri/Django_FinalProject.git)
    cd Django_FinalProject
    ```

2.  **Set up the virtual environment:**
    ```bash
    python -m venv myenv
    # Activate on Windows:
    myenv\Scripts\activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install django django-bootstrap5 mysqlclient
    ```

4.  **Database Configuration:**
    * Ensure MariaDB is running and create a database named `training_db`.
    * Update `DATABASES` settings in `core_project/settings.py` if necessary.

5.  **Run Migrations:**
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

6.  **Start the Development Server:**
    ```bash
    python manage.py runserver
    ```
    Visit the application at: `http://127.0.0.1:8000/`

---
*Developed by Raghad Asiri as part of the Full stack Django Web Development Course Project.* 