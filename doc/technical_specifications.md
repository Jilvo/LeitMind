Technical Specifications Document
=================================

This document outlines the technical specifications for the daily question-based application project. It provides a detailed overview of the architecture, file structure, and technologies used to implement the system.

Architecture
------------

The application follows a modular architecture with distinct layers for frontend, backend, and storage, ensuring scalability and maintainability.

### High-Level Components

-   **Frontend**:

    -   Mobile application (Flutter).

    -   Web interface (Vue.js).

-   **Backend**:

    -   FastAPI-powered API.

    -   Business logic and data validation.

-   **Storage**:

    -   PostgreSQL for relational data (users, progress, categories).

    -   File system for media assets (e.g., question images).

* * * * *

Repository Structure
--------------------

The repository is organized as follows:

```
project/
├── assets/                  # Static files
│   ├── fonts/               # Font files
│   ├── img/                 # Images
│   ├── js/                  # JavaScript
│   └── style/               # CSS and SCSS
├── bin/                     # Executables
├── data/                    # Raw data
│   ├── questions/           # Question datasets
│   └── categories/          # Category datasets
├── doc/                     # Documentation
│   ├── functional_specifications.md
│   └── technical_specifications.md
├── log/                     # Log files
├── src/                     # Source code
│   ├── config.py            # Configuration
│   ├── controller/          # Controllers (logic for endpoints)
│   ├── helper/              # Helper functions
│   ├── interface/           # Interfaces (CLI, web)
│   │   ├── cli/             # Command-line interface
│   │   └── web/             # Web interface (Vue.js)
│   ├── model/               # Data models
│   │   ├── user.py          # User model
│   │   ├── question.py      # Question model
│   │   └── progress.py      # Progress tracking model
│   ├── repository/          # Data access layer
│   │   ├── filesystem/      # File system repository
│   │   └── postgresql/      # PostgreSQL repository
│   ├── service/             # Business logic services
│   │   └── auth.py          # Authentication services
│   └── view/                # Views for rendering responses
├── storage/                 # File storage
│   ├── questions/           # Stored question files
│   ├── media/               # User-uploaded media (e.g., avatars)
│   └── categories/          # Category templates
├── tests/                   # Test cases
├── README.md                # Project documentation
└── requirements.txt         # Dependencies
```

* * * * *

Data
----

The application uses two storage systems:

1.  **File System**:

    -   Stores question-related images and media assets.

2.  **Relational Database (PostgreSQL)**:

    -   Stores structured data such as users, questions, and progress tracking.

### Database Tables

#### Users

-   Stores user data.

-   **Columns**:

    -   `id`: Primary key.

    -   `username`: Unique username.

    -   `email`: Unique email address.

    -   `hashed_password`: Password hash.

    -   `country`: Country from a list of existants country

    -   `created_at`: Timestamp for when the user was created.

    -   `updated_at`: Timestamp for the last update to the user's record.

#### Questions

-   Stores questions and related metadata.

-   **Columns**:

    -   `id`: Primary key.

    -   `text`: Question text.

    -   `category_id`: Foreign key linking to the category table.

    -   `image_path`: Path to associated image (if any).

    -   `created_at`: Timestamp for when the question was created.

    -   `updated_at`: Timestamp for the last update to the question's record.

#### Categories

-   Defines categories for grouping questions.

-   **Columns**:

    -   `id`: Primary key.

    -   `name`: Unique category name.

    -   `description`: Brief description of the category.

    -   `created_at`: Timestamp for when the category was created.

    -   `updated_at`: Timestamp for the last update to the category's record.

#### Progress

-   Tracks user progress for questions.

-   **Columns**:

    -   `id`: Primary key.

    -   `user_id`: Foreign key linking to the users table.

    -   `question_id`: Foreign key linking to the questions table.

    -   `status`: Current status (e.g., `completed`, `pending`, `in_progress`).

    -   `next_review`: Timestamp for the next scheduled review.

    -   `attempts`: Number of attempts made on the question.

    -   `created_at`: Timestamp for when the progress was created.

    -   `updated_at`: Timestamp for the last update to the progress's record.

#### Notifications

-   Stores notifications for users.

-   **Columns**:

    -   `id`: Primary key.

    -   `user_id`: Foreign key linking to the users table.

    -   `message`: Notification message content.

    -   `is_read`: Boolean indicating if the notification has been read.

    -   `sent_at`: Timestamp for when the notification was sent.

#### User_Settings

-   Stores user-specific settings and preferences.

-   **Columns**:

    -   `id`: Primary key.

    -   `user_id`: Foreign key linking to the users table.

    -   `language`: Preferred language for the user.

    -   `notification_frequency`: Frequency of notifications (e.g., daily, weekly).

    -   `theme`: Theme preference (e.g., light, dark).

    -   `created_at`: Timestamp for when the settings were created.

    -   `updated_at`: Timestamp for the last update to the settings record.

* * * * *

Code Structure
--------------

The project follows an **MVC-inspired structure**:

-   **Model**:

    -   Defines the schema and data structure for the application.

-   **View**:

    -   Handles the presentation logic for the API responses.

-   **Controller**:

    -   Implements the business logic and routes for handling requests.

### Key Components

#### Configuration (`config.py`)

Centralized configuration for managing environment variables and application settings.

#### Controller

Handles user requests and maps them to the appropriate service logic.

#### Model

Defines the schema for the database tables and data validation.

#### Repository

Implements the data access layer for interacting with PostgreSQL and the file system.

#### Service

Contains the business logic, such as user authentication and question assignment based on spaced repetition.

* * * * *

Technologies
------------

### Backend

-   **FastAPI**: For building RESTful APIs.

-   **SQLAlchemy**: ORM for PostgreSQL.

-   **Alembic**: Database migration tool.

### Frontend

-   **Flutter**: Mobile app development.

-   **Vue.js**: Web interface.

### Other Tools

-   **Docker**: Containerized deployments.

-   **pytest**: Automated testing.

* * * * *

File Storage
------------

-   **Questions**: Stores questions formatted for the application.

-   **Media**: Stores user-uploaded media assets such as profile pictures.

### File Organization

```
storage/
├── questions/
├── media/
└── categories/
```

* * * * *

Testing
-------

The application includes unit and integration tests:

-   **Unit Tests**:

    -   Test individual components, such as models and services.

-   **Integration Tests**:

    -   Test the interaction between API endpoints and the database.

* * * * *

Deployment
----------

The application will be deployed using Docker containers. A `docker-compose.yml` file will orchestrate the backend, frontend, and database services.

* * * * *

Appendices
----------

### References

-   FastAPI Documentation

-   [PostgreSQL Documentation](https://www.postgresql.org/docs/)

-   Docker Documentation
