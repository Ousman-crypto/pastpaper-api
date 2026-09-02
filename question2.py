from flask import Flask , jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "PastPapers API is running"

@app.route("/about")
def about():
    return "This is my personal past paper organiser API"

@app.route("/papers")
def get_papers():
    papers = [
        {"name":"Physics Final 2024","subject":"Physics","year":"2024"},
        {"name":"Networking Exam 2024","subject":"Networking","year":"2024"},
        {"name":"Database Test 2023","subject":"Database","year":"2023"}
    ]
    return jsonify(papers)

@app.route("/papers/physics")
def get_physics_papers():
    papers = [
        {"name":"Physics Final 2024","subject":"Physics","year":"2024"},
        {"name":"Physics Final 2023","subject":"Physics","year":"2023"},
        {"name":"Physics Test 2022","subject":"Physics","year":"2022"}
    ]
    physics = [p for p in papers if p["subject"] == "Physics"]
    return jsonify(physics)

if __name__ == "__main__":
    app.run(debug=True)