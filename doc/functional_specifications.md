Functional Specifications Document
==================================

This working document outlines the functional specifications for the development of a daily question-based application inspired by Duolingo. It aims to describe and organize the features derived from user needs analysis.

Introduction
------------

### Context

The project focuses on creating a multi-platform application that delivers daily questions to users using spaced repetition techniques. The app is accessible via mobile, web, and CLI interfaces, targeting various user categories such as students, professionals, and casual learners.

### Glossary

-   **Spaced Repetition**: A learning technique that involves reviewing information at increasing intervals to enhance long-term retention.

-   **CLI**: Command-Line Interface for terminal-based interactions with the application.

-   **API**: Application Programming Interface, allowing backend functionalities to be accessed programmatically.

-   **Category**: A grouping mechanism for questions (e.g., Science, History).

### Objectives

The application aims to achieve the following:

-   **Automation**: Provide daily questions to users based on a pre-defined learning schedule.

-   **Engagement**: Increase user retention through gamified features like progress tracking and notifications.

-   **Scalability**: Support growth in user base and question categories without major architectural changes.

-   **Accessibility**: Ensure the app is available on multiple platforms (mobile, web, CLI).

### State of the Art

#### Existing Solutions

-   **Duolingo**: Offers gamified language learning but focuses only on language-based questions.

-   **Quizlet**: Provides flashcard-based learning but lacks advanced spaced repetition algorithms.

-   **Anki**: Utilizes a spaced repetition algorithm but has limited gamification and UI appeal.

* * * * *

Implementation
--------------

### Stakeholders

The application will be developed for the following stakeholders:

-   **End Users**: Students, professionals, and casual learners who want to engage in structured, daily learning.

-   **Developers**: Responsible for building and maintaining the application infrastructure.

-   **Product Owners**: Define the requirements and oversee the project delivery.

### Final Users

Primary users include:

-   Individuals interested in consistent daily learning.

-   Users looking for a platform to improve knowledge retention in specific categories.

### Methodology

The project will follow an **Agile methodology**, involving iterative development and user feedback.

* * * * *

Technologies
------------

### Backend

-   **FastAPI**: For developing a high-performance API.

-   **PostgreSQL**: For relational data storage (users, progress).

-   **Docker**: For containerized deployments.

### Frontend

-   **Flutter**: For mobile app development.

-   **Vue.js**: For the web interface.

### Additional Tools

-   **Python-dotenv**: Manage environment variables.

-   **JWT**: For secure user authentication.

* * * * *

Development Process
-------------------

### Phases

1.  **Needs Analysis and Design**:

    -   Define user stories and functional requirements.

    -   Create wireframes for web and mobile interfaces.

2.  **Core API Development**:

    -   Implement user management (registration, authentication).

    -   Build endpoints for question delivery and progress tracking.

3.  **Frontend Development**:

    -   Develop a basic UI for mobile and web platforms.

4.  **Testing and Feedback**:

    -   Conduct user testing to identify improvements.

    -   Iterate based on feedback.

5.  **Deployment**:

    -   Deploy the application on a cloud platform.

* * * * *

Deliverables
------------

-   **MVP**: Minimum viable product with core functionalities.

-   **Documentation**: Usage and technical documentation for developers and users.

-   **Analytics**: Basic user activity and engagement metrics.

-   **User Feedback Report**: Insights gathered during the testing phase.

* * * * *

Definitions
-----------

### User

A registered individual who interacts with the application.

### Question

The core data structure for learning, containing:

-   Text content.

-   Category.

-   Difficulty level.

### Progress

Tracks user performance across categories and intervals:

-   Number of questions answered correctly.

-   Current position in the spaced repetition schedule.

* * * * *

Functionalities
---------------

### Core Features

#### User Management

-   Registration with email and password.

-   Login and JWT-based authentication.

-   Profile management for updating personal details.

#### Daily Questions

-   Assign daily questions based on spaced repetition.

-   Categorize questions for tailored learning.

-   Provide instant feedback on answers.

##### Enhanced Leitner System Implementation

The application implements an improved Leitner spaced repetition system with the following specifications:

**Session Structure**:
- **Maximum 25 questions per session** to prevent cognitive overload
- **4-hour minimum interval** between sessions to ensure proper rest
- **Automatic session management** with progress tracking

**Question Distribution per Session**:
- **5-10 new questions** (adjusted based on user's performance level and available time)
- **8-12 priority review questions** (most overdue based on Leitner intervals)
- **3-7 maintenance questions** (from boxes 4-5 for long-term retention)
- **Balanced distribution** across all subscribed categories

**Leitner Box System**:
- **Box 1**: 1 day interval (new or recently failed questions)
- **Box 2**: 3 days interval 
- **Box 3**: 7 days interval
- **Box 4**: 15 days interval
- **Box 5**: 30 days interval

**Intelligent Prioritization**:
- **Overdue questions prioritized** by number of days overdue
- **Category balancing** ensures no single category dominates
- **Difficulty mixing** combines easy/medium/hard questions for optimal motivation
- **"Leech" detection** identifies consistently failed questions for special handling

**Adaptive Learning Features**:
- **Performance-based quotas**: Users performing well get more new questions
- **Personal interval adjustment**: Intervals modified based on individual success rates
- **Daily cognitive load management**: Complex questions "cost" more from daily quota
- **Streak protection**: Maintains learning streaks with appropriate question selection

**Session Management**:
- **Mandatory breaks**: After 15 questions, system suggests a break
- **Progress persistence**: Sessions can be resumed later without losing progress
- **Completion rewards**: Positive reinforcement for finishing daily sessions
- **Flexible scheduling**: Users can adjust daily targets within recommended ranges

#### Progress Tracking

-   Display user progress in a graphical format.

-   Log correct/incorrect answers and update the schedule accordingly.

##### Advanced Progress Analytics

**Leitner Box Visualization**:
- **Real-time box distribution**: Show how many questions are in each Leitner box
- **Category progression**: Track progress per subscribed category
- **Retention rates**: Display success rates for each box level
- **Learning velocity**: Measure how quickly questions move between boxes

**Performance Metrics**:
- **Daily completion rates**: Track session completion consistency
- **Accuracy trends**: Monitor improvement over time per category
- **Streak tracking**: Maintain and display learning streaks
- **Cognitive load analysis**: Show optimal study times and patterns

**Predictive Features**:
- **Workload forecasting**: Predict upcoming review volumes
- **Difficulty assessment**: Identify challenging topics requiring attention
- **Time investment analysis**: Track time spent per question type
- **Learning curve visualization**: Show knowledge acquisition patterns

#### Notifications

-   Send reminders for unanswered questions via push notifications.

### Optional Features

#### Advanced Gamification

-   **Achievement system** with badges for consistency, accuracy, and category mastery
-   **Leaderboards** with weekly/monthly rankings across different metrics
-   **Streak protection** items to maintain learning consistency
-   **Daily challenges** with bonus questions and rewards
-   **Category mastery levels** with unlock requirements and rewards

#### Intelligent Learning Features

-   **Adaptive difficulty**: Dynamic question selection based on performance patterns
-   **Smart reminders**: Personalized notification timing based on optimal learning windows
-   **Learning insights**: Weekly reports on strengths, weaknesses, and recommendations
-   **Custom study modes**: Focus sessions for specific categories or difficulty levels
-   **Collaborative learning**: Study groups and shared progress with friends

#### Multi-Language Support

-   Translate questions and UI for international audiences.

-   **Localized learning paths**: Culture-specific question sets and learning approaches
-   **Multi-language question support**: Questions available in multiple languages for language learners

* * * * *

Constraints
-----------

### Performance

-   Handle up to 10,000 concurrent users with minimal latency.

### Scalability

-   Ensure the application can scale horizontally.

### Legal Compliance

-   Adhere to data protection regulations (e.g., GDPR).

* * * * *

Sitemap
-------

### Home

Landing page introducing the application.

### Authentication

-   Login and registration forms.

### Dashboard

-   Overview of user progress and upcoming questions.

### Categories

-   List of question categories with user progress.

### Notifications

-   View and manage reminders.

* * * * *

Future Enhancements
-------------------

-   Add real-time collaborative features.

-   Enhance analytics for deeper insights into user engagement.

-   Integrate with third-party learning platforms.
