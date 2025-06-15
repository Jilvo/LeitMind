# LeitnerQuest

[![Python](https://img.shields.io/badge/Python-3.12%2B-blue?logo=python)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green?logo=fastapi)](https://fastapi.tiangolo.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue?logo=postgresql)](https://www.postgresql.org/)
[![Flutter](https://img.shields.io/badge/Flutter-Mobile-blue?logo=flutter)](https://flutter.dev/)
[![Vue.js](https://img.shields.io/badge/Vue.js-Web-4FC08D?logo=vue.js)](https://vuejs.org/)
[![MIT License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

**LeitnerQuest** is a cross-platform application inspired by the Leitner system of spaced repetition. It helps users learn and retain information more effectively by delivering questions on a strategic schedule that adapts to their progress and performance.

---

## 🚀 Features

- **Daily Questions**: New questions delivered daily, with intervals that grow progressively (1 day, 3 days, 7 days, 15 days, etc.).
- **Multi-Platform Access**: Available on mobile (Flutter), web (Vue.js), and CLI.
- **Gamification**: Earn rewards, track your progress, and challenge yourself.
- **Customizable Content**: Create or explore question packs on various topics.
- **Analytics**: Track your learning performance with detailed stats.

---

## 🛠️ Technology Stack

- **Frontend**
  - Mobile: [Flutter](https://flutter.dev/)
  - Web: [Vue.js](https://vuejs.org/)
- **Backend**
  - Python ([FastAPI](https://fastapi.tiangolo.com/))
  - Database: [PostgreSQL](https://www.postgresql.org/)
  - Authentication: OAuth2 / JWT
  - (Optional) Web3: Solidity for reward tokens and immutable score storage
- **Additional Services**
  - Cloud Storage: AWS S3
  - Analytics: Google Analytics or custom engine

---

## ⚙️ Installation

### Prerequisites

- [Python 3.12+](https://www.python.org/downloads/)
- [PostgreSQL](https://www.postgresql.org/download/)
- [Flutter](https://flutter.dev/docs/get-started/install) (for mobile)
- [Node.js](https://nodejs.org/) (for web)

### Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/Jilvo/LeitMind.git
   cd LeitMind
   ```

2. **Install backend dependencies**
   ```bash
   cd backend
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Set up the database**
   ```bash
   psql -U postgres -c "CREATE DATABASE leitnerquest;"
   alembic upgrade head
   ```

4. **Run the backend server**
   ```bash
   uvicorn main:app --reload
   ```

5. **Run the frontend**
   - Mobile:
     ```bash
     cd frontend/mobile
     flutter run
     ```
   - Web:
     ```bash
     cd frontend/web
     npm install
     npm start
     ```

---

## 📖 Usage

1. **Sign Up / Log In**: Create an account to track your progress.
2. **Answer Questions**: Respond daily to improve retention.
3. **Monitor Progress**: Use the analytics dashboard.
4. **Explore Content**: Discover or upload question packs.

---

## 🗺️ Roadmap

- [ ] Implement reward tokens (Solidity/Web3)
- [ ] Add Badges, Success...
- [ ] Multiplayer mode
- [ ] Voice and image-based questions
- [ ] Integrations with third-party content providers

---

## 🤝 Contributing

We welcome contributions!  
1. Fork the repository  
2. Create a feature branch: `git checkout -b feature-name`  
3. Commit your changes: `git commit -m "Add new feature"`  
4. Push to the branch: `git push origin feature-name`  
5. Open a pull request

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 📬 Contact

For inquiries or support, contact us at [contact@leitnerquest.com](mailto:contact@leitnerquest.com).

---

Start your journey to smarter learning with **LeitnerQuest** today!