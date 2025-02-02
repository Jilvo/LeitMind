# FastAPI + PostgreSQL Boilerplate

This is a boilerplate project to kickstart a FastAPI app with a PostgreSQL database.

## Features
- User and Question management with SQLAlchemy ORM
- FastAPI routers for modular API structure
- PostgreSQL integration

## Getting Started

1. Create and activate a virtual environment.
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Update `.env` with your database credentials.
4. Run the app:
   ```
   uvicorn app.main:app --reload
   ```

## Endpoints
- `/users` : Manage users
- `/questions` : Manage questions
- `/validate` : Manage validation of users for questions


## Organising questions
`Category` --> `Sub Category` --> `Theme` --> `Questions` --> `Answers`

Exemple :

`Histoire` --> `Préhistoire` --> `Paléolithique inférieur` --> `Quel est le nom du premier hominidé connu à avoir utilisé des outils de pierre ?` --> `"Homo habilis", "Homo erectus", "Australopithèque"`
