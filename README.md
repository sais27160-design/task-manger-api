# 🚀 Task Manager REST API

A full-stack, cloud-native Task Management application built to demonstrate Separation of Concerns using a Layered Architecture.

## 📌 Project Overview
This project is a complete RESTful API with an embedded frontend. It allows users to create, read, update, and delete tasks. The backend is built with Python and FastAPI, utilizing SQLAlchemy to communicate with a MySQL 8.4 database. The application is containerized with Docker and fully deployed on Google Cloud Run, connecting securely to Google Cloud SQL via IAM authentication.

## 🏗️ Architecture: The Layered Approach
This application strictly follows a layered architectural pattern to ensure the code is modular, scalable, and easy to maintain. 

* **API Layer (`routers/`)**: The entry point. It defines the HTTP endpoints (GET, POST, PUT, DELETE) and handles incoming requests and outgoing JSON responses using Pydantic models.
* **Service Layer (`services/`)**: The brain of the application. It contains all the business logic and rules, acting as the middleman between the API and the data.
* **Repository Layer (`repositories/`)**: The data access layer. This is the *only* part of the application allowed to communicate directly with the database using SQLAlchemy.
* **Data Models (`models/`)**: Defines the database schema (`task_orm.py`) and the data validation structures (`task_request.py`, `task_response.py`).

## 💻 Tech Stack
* **Backend:** Python 3.11, FastAPI
* **Database:** MySQL 8.4 (Hosted on Google Cloud SQL)
* **ORM / Driver:** SQLAlchemy, PyMySQL
* **Frontend:** HTML5, CSS3, Vanilla JavaScript (Fetch API)
* **Deployment & Infrastructure:** Docker, Google Cloud Run, Google IAM (Service Accounts)

## 🌐 Live Application
The API and frontend are successfully deployed and live at:
**[Insert Your Cloud Run URL Here: https://project-api-155102835604.us-central1.run.app]**

## 🔌 API Endpoints
The backend provides the following RESTful endpoints:

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | `/tasks/` | Retrieves a list of all current tasks. |
| `POST` | `/tasks/` | Creates a new task. Requires `title` and `description`. |
| `PUT` | `/tasks/{id}` | Updates an existing task (e.g., editing text or marking as done). |
| `DELETE` | `/tasks/{id}` | Deletes a task from the database entirely. |

## 🛠️ Key Technical Challenges Solved
* **MySQL 8.4 Authentication:** Handled the transition to `caching_sha2_password` by securely configuring the PyMySQL driver.
* **Cloud SQL IAM Security:** Configured Google Cloud IAM policies to allow the Cloud Run Service Account to securely connect to the database via Unix sockets without exposing credentials.
* **CORS & Routing:** Resolved frontend-to-backend routing conflicts to ensure seamless asynchronous JavaScript `fetch` operations.
