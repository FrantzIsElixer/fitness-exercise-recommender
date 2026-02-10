from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

# Replace this with your actual RapidAPI key
RAPID_API_KEY = "143025f610msh471b10b590f3805p1b3b01jsnafa2ba4ce519"

HEADERS = {
    "X-RapidAPI-Key": RAPID_API_KEY,
    "X-RapidAPI-Host": "exercisedb.p.rapidapi.com"
}

@app.route("/")
def home():
    return jsonify({"message": "Fitness Exercise Recommendation API"})

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

    # Simple rule-based logic
    best_exercise = exercises[0]["name"]

    return jsonify({
        "goal": goal,
        "recommended_exercise": best_exercise,
        "rating": 10
    })

if __name__ == "__main__":
    app.run(debug=True)
