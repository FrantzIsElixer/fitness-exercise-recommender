# Fitness Exercise Recommendation System

## Project Overview

This project is a Flask-based web application and REST API that helps users find strong exercise recommendations for a selected muscle group or body part. A user enters an area such as `chest`, `legs`, `abs`, or `lower back`, and the system returns a list of recommended exercises along with a star rating from 1 to 5.

The application uses an external REST API, ExerciseDB through RapidAPI, to retrieve exercise information. The returned data is processed and displayed in a simple, user-friendly interface designed to be easy to read and use.

## Purpose

The purpose of this project is to demonstrate:

- Building a Python web application with Flask
- Consuming data from an external REST API
- Processing JSON responses
- Returning recommendation data through a custom API endpoint
- Presenting results in a clean front-end interface

## Features

- Search by muscle group or body part
- Retrieve exercise data from ExerciseDB using REST API calls
- Display a list of recommended exercises
- Show a 1 to 5 star rating for each exercise
- Handle invalid or unsupported user input
- Provide a fallback list of exercises if the external API is unavailable
- Simple and improved visual layout for readability

## Technologies Used

- Python 3
- Flask
- Requests
- HTML, CSS, and JavaScript
- ExerciseDB API via RapidAPI

## How the System Works

1. The user enters a muscle group or body part into the search box.
2. The front end sends a request to the Flask route: `/recommend`.
3. The Flask app calls the recommendation service.
4. The recommendation service sends a request to the ExerciseDB REST API.
5. The returned JSON data is processed and exercises are assigned star ratings.
6. The top results are displayed on the page in a clean list format.

If the external API key is missing or the API cannot be reached, the app uses a built-in fallback exercise list so the program can still demonstrate its main functionality.

## Project Structure

```text
COSC319/
|-- app.py
|-- recommendation_service.py
|-- README.md
|-- templates/
|   `-- index.html
```

## API Information

This project uses the following external API:

- ExerciseDB API on RapidAPI

Example API data may include:

- Exercise name
- Target muscle
- Body part
- Equipment used

## Installation and Setup

### 1. Install Required Packages

Run the following command in the project folder:

```bash
python -m pip install flask requests
```

### 2. Set the API Key

This project requires a RapidAPI key for ExerciseDB.

Set the key as an environment variable instead of hardcoding it into the code.

Windows PowerShell:

```powershell
setx RAPID_API_KEY "YOUR_API_KEY_HERE"
```

After setting the key, restart the terminal before running the app.

### 3. Run the Application

```bash
python app.py
```

The application will run locally at:

```text
http://127.0.0.1:5000
```

## Available Routes

### Home Page

```http
GET /
```

Displays the main user interface.

### Recommendation Endpoint

```http
GET /recommend?goal=chest
```

Example JSON response:

```json
{
  "goal": "chest",
  "matched_group": "chest",
  "top_exercise": {
    "name": "Barbell Bench Press",
    "rating": 5,
    "stars": "★★★★★"
  },
  "exercise_list": [
    {
      "name": "Barbell Bench Press",
      "rating": 5,
      "stars": "★★★★★"
    },
    {
      "name": "Incline Dumbbell Press",
      "rating": 5,
      "stars": "★★★★★"
    }
  ],
  "total_exercises_found": 5
}
```

## Rating Logic

The application uses a simple rule-based rating system.

- Exercises that are commonly considered strong compound movements are given higher ratings.
- Exercises that are effective assistance or isolation movements are given moderate ratings.
- Ratings are displayed visually as 1 to 5 stars.

This approach is straightforward and easy to explain for a class project, while still producing useful exercise recommendations.

## Error Handling

The application includes basic error handling for:

- Missing input
- Unsupported body parts or muscle groups
- External API failure
- Missing RapidAPI key

When the external API is unavailable, the app still works by using a built-in fallback dataset.

## Limitations

- The rating system is rule-based and not personalized
- The application does not currently store user accounts or workout history
- Results depend partly on the external API being available
- Exercise recommendations are limited to a short list rather than full workout plans

## Future Improvements

- Add exercise images and descriptions
- Build full workout plans instead of single-category recommendations
- Add filters for equipment, difficulty, or fitness level
- Store user preferences in a database
- Improve the recommendation logic with more detailed scoring

## Conclusion

This project demonstrates how a web application can combine Flask, REST APIs, and front-end design to create a practical fitness recommendation tool. It shows the use of external data, server-side processing, JSON handling, and a simple interface that allows users to search for exercises by body part and receive readable, star-rated results.
