Fitness Exercise Recommendation & Rating System
Overview

This project is a small microservice-based application that recommends and rates gym exercises based on a user’s fitness goal. It consumes data from an external REST API and processes JSON data across services to return meaningful exercise recommendations.

The project is inspired by a Solo Leveling–based fitness app concept, where users improve their stats by performing effective workouts.

Features

Fetches real exercise data from an external REST API

Processes and normalizes JSON responses

Rates exercises on a scale from 1–10

Returns recommendations in JSON format

Simple REST endpoints using Flask

Technologies Used

Python 3

Flask

Requests

ExerciseDB API (via RapidAPI)

External API

ExerciseDB API (RapidAPI)
Provides exercise information such as:

Exercise name

Target muscle

Body part

Required equipment

Example response:

{
  "name": "bench press",
  "target": "pectorals",
  "equipment": "barbell",
  "bodyPart": "chest"
}

Project Structure
fitness-api/
│
├── app.py
├── requirements.txt
└── README.md

Setup Instructions
1. Install Dependencies
python -m pip install flask requests

2. API Key Setup

This project requires a RapidAPI key for the ExerciseDB API.

Do NOT hardcode your API key.

Set it as an environment variable:

Windows (PowerShell):

setx RAPID_API_KEY "YOUR_API_KEY_HERE"


macOS / Linux:

export RAPID_API_KEY="YOUR_API_KEY_HERE"


Restart your terminal after setting the key.

3. Run the Application
python app.py


The server will start at:

http://127.0.0.1:5000

API Endpoints
Home
GET /


Response:

{
  "message": "Fitness Exercise Recommendation API"
}

Recommend Exercise
GET /recommend?goal=pectorals


Response:

{
  "goal": "pectorals",
  "recommended_exercise": "bench press",
  "rating": 10
}


⚠️ Note: The goal parameter must match valid target muscles used by the ExerciseDB API (e.g., pectorals, biceps, triceps).

Rating Logic

The current implementation uses a simple rule-based approach:

Exercises directly targeting the selected muscle group receive the highest rating.

Future improvements may include difficulty level, equipment availability, and workout combinations.

Limitations

Uses in-memory logic (no database yet)

Ratings are rule-based (not machine learning)

Limited to individual exercise recommendations

Future Enhancements

Store user goals in a database

Support multiple fitness goals

Generate full workout plans

Add a web-based UI

Improve rating algorithm