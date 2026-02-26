from flask import Flask, jsonify, request, render_template
import requests
import os

app = Flask(__name__)

# Replace this with your actual RapidAPI key
RAPID_API_KEY = os.getenv("RAPID_API_KEY")

if not RAPID_API_KEY:
    raise RuntimeError("RAPID_API_KEY environment variable not set")

HEADERS = {
    "X-RapidAPI-Key": RAPID_API_KEY,
    "X-RapidAPI-Host": "exercisedb.p.rapidapi.com"
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/recommend", methods=["GET"])
def recommend_exercise():
    goal = request.args.get("goal")

    if not goal:
        return jsonify({"error": "Please provide a goal"}), 400

    # Example: chest goal
    url = f"https://exercisedb.p.rapidapi.com/exercises/target/{goal}"
    response = requests.get(url, headers=HEADERS)

    if response.status_code != 200:
        return jsonify({"error": "Failed to fetch exercise data"}), 500

    exercises = response.json()

    if not exercises:
        return jsonify({"error": "No exercises found for the given goal"}), 404

    # Simple rule-based logic
    best_exercise = exercises[0]["name"] # Default to the first exercise
    rating = 7 # Default rating

    for exercise in exercises:
        name = exercise["name"].lower()
        if "press" in name or "squat" in name or "deadlift" in name:
            best_exercise = exercise["name"]
            rating = 10
            break

    return jsonify({
        "goal": goal,
        "recommended_exercise": best_exercise,
        "rating": rating,
        "total_exercises_found": len(exercises)
    })

if __name__ == "__main__":
    app.run(debug=True)
