Polling Application

The Polling Application is a web-based platform that allows users to create, participate in, and view the results of polls. It provides a simple and intuitive interface for users to engage in various polls on different topics.

Features

User Authentication: Users can sign up, log in, and log out to access the polling features.
Create Polls: Authenticated users can create polls by providing a question and multiple options for voting.
Participate in Polls: Authenticated users can vote in polls by selecting their preferred options.
View Poll Results: Users can view the results of polls, including the percentage of votes for each option.
Deadline for Polls: Creators can optionally set a deadline for polls, after which no more votes can be cast.

Installation

Clone the repository: git clone https://github.com/your-username/polling-app.git
Navigate to the project directory: cd polling-app
Install dependencies: pip install -r requirements.txt
Run migrations: python manage.py migrate
Start the development server: python manage.py runserver


Usage

Access the application in your web browser at http://localhost:8000.
Sign up for a new account or log in with existing credentials.
Create a new poll by providing a question and options.
Participate in polls by selecting your preferred options.
View the results of polls to see the distribution of votes.
Log out of your account when finished.
