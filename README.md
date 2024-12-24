# LeitnerQuest

**LeitnerQuest** is a mobile and web application inspired by the Leitner system of spaced repetition. It helps users learn and retain information more effectively by delivering questions on a strategic schedule that adapts to their progress and performance.

## Features

- **Daily Questions**: Receive a new question daily, with intervals that grow progressively (1 day, 3 days, 7 days, 15 days, etc.).
- **Multi-Platform Access**: Available on mobile, web, and CLI for convenient access anytime, anywhere.
- **Gamification**: Earn rewards, track your progress, and challenge yourself to improve.
- **Customizable Content**: Create your own question packs or explore curated packs on various topics.
- **Analytics**: Track your learning performance and see detailed stats on your progress.

## Technology Stack

### Frontend:
- **Mobile**: Flutter / React Native / Swift / Android ?
- **Web**: React.js / Vue.js ?


### Backend:
- **Language**: Python (FastAPI)
- **Database**: PostgreSQL
- **Authentication**: OAuth2 / JWT
- **Web3 Integration** (Optional): Solidity for reward tokens and immutable score storage

### Additional Services:
- **Cloud Storage**: AWS S3 for multimedia assets
- **Analytics**: Integration with Google Analytics or custom analytics engine

## Installation

### Prerequisites
<!-- 1. Install [Flutter](https://flutter.dev/docs/get-started/install) for mobile development. -->
<!-- 2. Install [Node.js](https://nodejs.org/) for web development. -->
3. Set up a Python environment with FastAPI installed.
4. Install PostgreSQL for database management.

### Steps

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Jilvo/LeitMind.git
   cd leitnerquest
   ```

2. **Install backend dependencies**:
   ```bash
   cd backend
   python3 -m venv venv
   source venv/bin/activate  # or venv\Scripts\activate on Windows
   pip install -r requirements.txt
   ```

3. **Set up the database**:
   ```bash
   psql -U postgres -c "CREATE DATABASE leitnerquest;"
   alembic upgrade head
   ```

4. **Run the backend server**:
   ```bash
   uvicorn main:app --reload
   ```

5. **Run the frontend**:
   - For mobile:
     ```bash
     cd frontend/mobile
     flutter run
     ```
   - For web:
     ```bash
     cd frontend/web
     npm install
     npm start
     ```

## Usage

1. **Sign Up / Log In**: Create an account to start tracking your progress.
2. **Answer Questions**: Respond to questions daily to improve your retention.
3. **Monitor Progress**: Use the analytics dashboard to view your learning stats.
4. **Explore Content**: Discover new question packs or upload your own.

## Roadmap

- [ ] Implement reward tokens using Solidity and Web3.
- [ ] Add multiplayer mode for collaborative learning.
- [ ] Introduce voice and image-based questions.
- [ ] Expand to include integrations with third-party content providers.

## Contributing

We welcome contributions! To contribute:
1. Fork the repository.
2. Create a feature branch: `git checkout -b feature-name`.
3. Commit your changes: `git commit -m "Add new feature"`.
4. Push to the branch: `git push origin feature-name`.
5. Open a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Contact

For inquiries or support, contact us at [contact@leitnerquest.com](mailto:contact@leitnerquest.com).

---

Start your journey to smarter learning with LeitnerQuest today!
