# Book Tracker API using Django and MySQL 
- (TechOps Session - October 24, 2023)

Welcome to the Book Tracker API, the backend component of a web application developed with Django and MySQL. This API serves as the foundation for managing and tracking books read and their respective authors.

## Table of Contents
- [Book Tracker API using Django and MySQL](#book-tracker-api-using-django-and-mysql)
  - [Table of Contents](#table-of-contents)
  - [Prerequisites](#prerequisites)
  - [Getting Started](#getting-started)
    - [Installation](#installation)
    - [Running the Server](#running-the-server)
  - [Project Structure](#project-structure)
  - [API Endpoints](#api-endpoints)
  - [Contributing](#contributing)

## Prerequisites

Before you dive into the project, make sure you have the following prerequisites in place:
- Python 3
- Django
- MySQL (or an alternative database of your choice)

## Getting Started

### Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/sosmongare/booktracker-api.git
   ```

2. Navigate to the project directory:

   ```bash
   cd booktracker-api
   ```

3. Install the necessary Python packages using Pipenv:

   ```bash
   pip install -r requirements.txt
   ```

### Running the Server

1. Activate the virtual environment (On windows):

   ```bash
   . env/scripts/activate
   ```

2. Launch the Django development server:

   ```bash
   python manage.py runserver
   ```

The server will start and be accessible at `http://localhost:8000/`.

## Project Structure

The project is structured as follows:

- `backend/`: The primary Django project directory.
- `booktracker/`: A Django app that houses models, views, and serializers.
- `api/`: Contains API views and endpoints.
- `models.py`: Defines the database models, such as Book and Author.
- `serializers.py`: Serializes model data for API responses to a JSON representation.
- `views.py`: Contains API views and viewsets.

## API Endpoints

- `GET /api/books/`: Retrieve a list of all books.
- `POST /api/books/`: Create a new book.
- `GET /api/books/<id>/`: Retrieve a specific book.
- `PUT /api/books/<id>/`: Update a specific book.
- `DELETE /api/books/<id>/`: Delete a specific book.
- `GET /api/authors/`: Retrieve a list of all authors.
- `POST /api/authors/`: Create a new author.
- `GET /api/authors/<id>/`: Retrieve a specific author.
- `PUT /api/authors/<id>/`: Update a specific author.
- `DELETE /api/authors/<id>/`: Delete a specific author.

## Contributing

We welcome contributions to this project! If you'd like to contribute, please follow these steps:
1. Fork the project.
2. Create a feature branch: `git checkout -b feature/my-feature`.
3. Commit your changes: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin feature/my-feature`.
5. Submit a pull request.

---

Happy coding!

