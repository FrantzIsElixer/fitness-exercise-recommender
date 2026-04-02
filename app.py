from flask import Flask, jsonify, request, render_template
from recommendation_service import get_recommendation

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/recommend", methods=["GET"])
def recommend_exercise():
    goal = request.args.get("goal") or request.args.get("body_part")

    if not goal:
        return jsonify({"error": "Please provide a muscle group or body part"}), 400

    result, status_code = get_recommendation(goal)
    return jsonify(result), status_code
    

if __name__ == "__main__":
    app.run(debug=True)
