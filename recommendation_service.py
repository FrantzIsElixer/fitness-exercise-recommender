import os

import requests

RAPID_API_KEY = os.getenv("RAPID_API_KEY")
API_HOST = "exercisedb.p.rapidapi.com"

HEADERS = {
    "X-RapidAPI-Key": RAPID_API_KEY,
    "X-RapidAPI-Host": API_HOST,
}

FALLBACK_LIBRARY = {
    "chest": [
        {"name": "Barbell Bench Press", "rating": 5},
        {"name": "Incline Dumbbell Press", "rating": 5},
        {"name": "Push-Up", "rating": 4},
        {"name": "Cable Fly", "rating": 4},
        {"name": "Chest Dips", "rating": 4},
    ],
    "back": [
        {"name": "Deadlift", "rating": 5},
        {"name": "Pull-Up", "rating": 5},
        {"name": "Barbell Row", "rating": 5},
        {"name": "Lat Pulldown", "rating": 4},
        {"name": "Seated Cable Row", "rating": 4},
    ],
    "shoulders": [
        {"name": "Overhead Press", "rating": 5},
        {"name": "Lateral Raise", "rating": 4},
        {"name": "Arnold Press", "rating": 4},
        {"name": "Face Pull", "rating": 4},
        {"name": "Rear Delt Fly", "rating": 4},
    ],
    "arms": [
        {"name": "Barbell Curl", "rating": 5},
        {"name": "Hammer Curl", "rating": 4},
        {"name": "Close-Grip Bench Press", "rating": 5},
        {"name": "Triceps Pushdown", "rating": 4},
        {"name": "Chin-Up", "rating": 4},
    ],
    "biceps": [
        {"name": "Barbell Curl", "rating": 5},
        {"name": "Incline Dumbbell Curl", "rating": 4},
        {"name": "Hammer Curl", "rating": 4},
        {"name": "Cable Curl", "rating": 4},
        {"name": "Chin-Up", "rating": 4},
    ],
    "triceps": [
        {"name": "Close-Grip Bench Press", "rating": 5},
        {"name": "Skull Crusher", "rating": 4},
        {"name": "Triceps Pushdown", "rating": 4},
        {"name": "Overhead Triceps Extension", "rating": 4},
        {"name": "Bench Dips", "rating": 3},
    ],
    "legs": [
        {"name": "Back Squat", "rating": 5},
        {"name": "Romanian Deadlift", "rating": 5},
        {"name": "Walking Lunge", "rating": 4},
        {"name": "Leg Press", "rating": 4},
        {"name": "Bulgarian Split Squat", "rating": 5},
    ],
    "quads": [
        {"name": "Back Squat", "rating": 5},
        {"name": "Front Squat", "rating": 5},
        {"name": "Leg Press", "rating": 4},
        {"name": "Walking Lunge", "rating": 4},
        {"name": "Leg Extension", "rating": 3},
    ],
    "hamstrings": [
        {"name": "Romanian Deadlift", "rating": 5},
        {"name": "Nordic Curl", "rating": 5},
        {"name": "Glute Ham Raise", "rating": 4},
        {"name": "Leg Curl", "rating": 4},
        {"name": "Good Morning", "rating": 4},
    ],
    "glutes": [
        {"name": "Barbell Hip Thrust", "rating": 5},
        {"name": "Romanian Deadlift", "rating": 5},
        {"name": "Bulgarian Split Squat", "rating": 4},
        {"name": "Cable Kickback", "rating": 3},
        {"name": "Step-Up", "rating": 4},
    ],
    "calves": [
        {"name": "Standing Calf Raise", "rating": 5},
        {"name": "Seated Calf Raise", "rating": 4},
        {"name": "Jump Rope", "rating": 4},
        {"name": "Single-Leg Calf Raise", "rating": 4},
        {"name": "Farmer's Walk on Toes", "rating": 3},
    ],
    "core": [
        {"name": "Plank", "rating": 5},
        {"name": "Hanging Leg Raise", "rating": 5},
        {"name": "Cable Crunch", "rating": 4},
        {"name": "Ab Wheel Rollout", "rating": 5},
        {"name": "Dead Bug", "rating": 4},
    ],
    "abs": [
        {"name": "Hanging Leg Raise", "rating": 5},
        {"name": "Cable Crunch", "rating": 4},
        {"name": "Ab Wheel Rollout", "rating": 5},
        {"name": "Reverse Crunch", "rating": 4},
        {"name": "Bicycle Crunch", "rating": 3},
    ],
    "lower back": [
        {"name": "Romanian Deadlift", "rating": 5},
        {"name": "Back Extension", "rating": 4},
        {"name": "Bird Dog", "rating": 4},
        {"name": "Good Morning", "rating": 4},
        {"name": "Superman Hold", "rating": 3},
    ],
    "full body": [
        {"name": "Deadlift", "rating": 5},
        {"name": "Clean and Press", "rating": 5},
        {"name": "Thruster", "rating": 4},
        {"name": "Kettlebell Swing", "rating": 4},
        {"name": "Burpee", "rating": 3},
    ],
}

ALIAS_MAPPING = {
    "arm": "arms",
    "arms": "arms",
    "bicep": "biceps",
    "biceps": "biceps",
    "tricep": "triceps",
    "triceps": "triceps",
    "chest": "chest",
    "pec": "chest",
    "pecs": "chest",
    "back": "back",
    "lats": "back",
    "shoulder": "shoulders",
    "shoulders": "shoulders",
    "delts": "shoulders",
    "leg": "legs",
    "legs": "legs",
    "quad": "quads",
    "thighs": "legs",
    "thigh": "legs",
    "quads": "quads",
    "hamstring": "hamstrings",
    "hamstrings": "hamstrings",
    "glute": "glutes",
    "glutes": "glutes",
    "butt": "glutes",
    "calf": "calves",
    "calves": "calves",
    "core": "core",
    "ab": "abs",
    "abs": "abs",
    "stomach": "abs",
    "lower back": "lower back",
    "full body": "full body",
    "whole body": "full body",
}

SUPPORTED_GROUPS = sorted(FALLBACK_LIBRARY.keys())


def _normalize_goal(goal):
    cleaned_goal = " ".join(goal.lower().strip().split())
    return ALIAS_MAPPING.get(cleaned_goal, cleaned_goal)


def _format_exercises(exercises):
    formatted = []

    for exercise in exercises:
        rating = max(1, min(5, exercise["rating"]))
        formatted.append(
            {
                "name": exercise["name"],
                "rating": rating,
                "stars": "\u2605" * rating + "\u2606" * (5 - rating),
            }
        )

    return formatted


def _fetch_from_api(mapped_goal):
    if not RAPID_API_KEY:
        return None

    url = f"https://{API_HOST}/exercises/target/{mapped_goal}"

    try:
        response = requests.get(url, headers=HEADERS, timeout=8)
        response.raise_for_status()
    except requests.RequestException:
        return None

    exercises = response.json()
    if not isinstance(exercises, list) or not exercises:
        return None

    ranked_exercises = []
    for exercise in exercises[:10]:
        name = exercise.get("name", "").strip()
        if not name:
            continue

        lowered_name = name.lower()
        rating = 3
        if any(keyword in lowered_name for keyword in ("squat", "deadlift", "press", "pull-up", "row", "hip thrust")):
            rating = 5
        elif any(keyword in lowered_name for keyword in ("curl", "lunge", "raise", "pulldown", "extension", "fly")):
            rating = 4

        ranked_exercises.append({"name": name.title(), "rating": rating})

    return ranked_exercises or None


def get_recommendation(goal):
    if not goal or not goal.strip():
        return {"error": "Please enter a muscle group or body part."}, 400

    normalized_goal = _normalize_goal(goal)
    exercises = _fetch_from_api(normalized_goal)

    if not exercises:
        exercises = FALLBACK_LIBRARY.get(normalized_goal)

    if not exercises:
        return {
            "error": "No exercises found for that body part.",
            "supported_groups": SUPPORTED_GROUPS,
        }, 404

    formatted_exercises = _format_exercises(exercises)

    return {
        "goal": goal.strip(),
        "matched_group": normalized_goal,
        "top_exercise": formatted_exercises[0],
        "exercise_list": formatted_exercises,
        "total_exercises_found": len(formatted_exercises),
    }, 200
