# from flask import Flask, jsonify, request

# papers_list = []

# @app.route("/add-paper", methods=["POST"])
# def add_paper():
#     data = request.get_json()
    
#     if not data:
#         return jsonify({"error": "No data received"}), 400
    
#     name = data.get("name")
#     subject = data.get("subject")
#     year = data.get("year")
    
#     if not name or not subject:
#         return jsonify({"error": "Name and subject are required"}), 400
    
#     new_paper = {
#         "id": len(papers_list) + 1,
#         "name": name,
#         "subject": subject,
#         "year": year or "Unknown"
#     }
    
#     papers_list.append(new_paper)
#     return jsonify({"message": "Paper added", "paper": new_paper}), 201











# #deepseek

# from flask import Flask, jsonify, request

# app = Flask(__name__)

# papers = []

# @app.route("/")
# def home():
#     return "PastPapers API is running"

# @app.route("/about")
# def about():
#     return "This is my personal past paper organiser API"

# @app.route("/papers")
# def get_papers():
#     return jsonify(papers)

# @app.route("/papers/physics")
# def get_physics_papers():
#     physics = [p for p in papers if p["subject"] == "Physics"]
#     return jsonify(physics)

# @app.route("/add-paper", methods=["POST"])
# def add_paper():
#     data = request.get_json()
    
#     if not data:
#         return jsonify({"error": "No data provided"}), 400
    
#     name = data.get("name")
#     subject = data.get("subject")
#     year = data.get("year")
    
#     if not name:
#         return jsonify({"error": "Name is required"}), 400
    
#     if not subject:
#         return jsonify({"error": "Subject is required"}), 400
    
#     papers.append({"name": name, "subject": subject, "year": year})
#     return jsonify({"message": "Paper added successfully", "papers": papers})

# if __name__ == "__main__":
#     app.run(debug=True)












from flask import Flask, jsonify,request 

papers_list = []

app = Flask(__name__) 

@app.route("/add-paper",methods = ["POST"])
def add_paper():
    data = request.get_json()

    if not data:
        return jsonify({"error":"No data received"}),400
    name = data.get("name")
    subject = data.get("subject")
    year = data.get("year")

    if not name or not subject:
        return jsonify({"error":"Name and subject are required"}),400
    new_paper = {
        "id":len(papers_list) + 1,
        "name":name,
        "subject":subject,
        "year":year or "Unknown"
    }
    papers_list.append(new_paper)
    return jsonify({"message":"Paper added","paper":new_paper}),201

if __name__ == "__main__":
    app.run(debug = True)