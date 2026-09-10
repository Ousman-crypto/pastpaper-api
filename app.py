# # # # # from flask import Flask

# # # # # app = Flask(__name__)

# # # # # @app.route("/")
# # # # # def home():
# # # # #     return "PastPapers API is running"

# # # # # @app.route("/about")
# # # # # def about():
# # # # #     return "This is my personal past paper organiser API"

# # # # # if __name__ == "__main__":
# # # # #     app.run(debug=True)    

# # # # from flask import Flask, jsonify, request 

# # # # app = Flask(__name__)

# # # # papers_list = []

# # # # @app.route("/")
# # # # def home():
# # # #     return "PastPapers APT is running"

# # # # @app.route("/about")
# # # # def about():
# # # #     return "This is my personal past paper organiser API"

# # # # @app.route("/add-paper",methods = ["POST"])
# # # # def add_paper():
# # # #     data = request.get_json()

# # # #     if not data:
# # # #         return jsonify({"error":"No data received"}),400
# # # #     name = data.get("name")
# # # #     subject = data.get("subject")
# # # #     year = data.get("year")

# # # #     if not name or not subject:
# # # #         return jsonify({"error":"Name and subject are required"}),400
# # # #     new_paper = {
# # # #         "id":len(papers_list) + 1,
# # # #         "name":name,
# # # #         "subject":subject,
# # # #         "year":year or "Unknown"
# # # #     }
# # # #     papers_list.append(new_paper)
# # # #     return jsonify({"message":"Paper added","paper":new_paper}),201

# # # # @app.route("/papers")
# # # # def get_papers():
# # # #     return jsonify(papers_list)

# # # # if __name__ == "__main__":
# # # #     app.run(debug=True)

# # # from flask import Flask, jsonify, request
# # # from flask_cors import CORS
# # # import sqlite3

# # # app = Flask(__name__)
# # # CORS(app)

# # # # ============================================
# # # # DATABASE SETUP
# # # # ============================================

# # # def get_db():
# # #     conn = sqlite3.connect("papers.db")
# # #     conn.row_factory = sqlite3.Row
# # #     return conn

# # # def init_db():
# # #     conn = get_db()
# # #     conn.execute("""
# # #         CREATE TABLE IF NOT EXISTS papers (
# # #             id INTEGER PRIMARY KEY AUTOINCREMENT,
# # #             name TEXT NOT NULL,
# # #             subject TEXT NOT NULL,
# # #             year TEXT,
# # #             paper_type TEXT
# # #         )
# # #     """)
# # #     conn.commit()
# # #     conn.close()

# # # # ============================================
# # # # ROUTES
# # # # ============================================

# # # @app.route("/")
# # # def home():
# # #     return "PastPapers API is running"

# # # @app.route("/papers")
# # # def get_papers():
# # #     conn = get_db()
# # #     papers = conn.execute("SELECT * FROM papers").fetchall()
# # #     conn.close()
# # #     return jsonify([dict(p) for p in papers])

# # # @app.route("/add-paper", methods=["POST"])
# # # def add_paper():
# # #     data = request.get_json()

# # #     if not data:
# # #         return jsonify({"error": "No data received"}), 400

# # #     name = data.get("name")
# # #     subject = data.get("subject")
# # #     year = data.get("year", "Unknown")
# # #     paper_type = data.get("paper_type", "Exam")

# # #     if not name or not subject:
# # #         return jsonify({"error": "Name and subject are required"}), 400

# # #     conn = get_db()
# # #     conn.execute(
# # #         "INSERT INTO papers (name, subject, year, paper_type) VALUES (?, ?, ?, ?)",
# # #         (name, subject, year, paper_type)
# # #     )
# # #     conn.commit()
# # #     conn.close()

# # #     return jsonify({"message": "Paper added successfully"}), 201

# # # @app.route("/papers/delete/<int:paper_id>", methods=["DELETE"])
# # # def delete_paper(paper_id):
# # #     conn = get_db()
# # #     conn.execute("DELETE FROM papers WHERE id = ?", (paper_id,))
# # #     conn.commit()
# # #     conn.close()
# # #     return jsonify({"message": "Paper deleted"}), 200

# # # # ============================================
# # # # START
# # # # ============================================

# # # if __name__ == "__main__":
# # #     init_db()
# # #     app.run(debug=True)



# # from flask import Flask,jsonify,request
# # from flask_cors import CORS
# # import sqlite3

# # app = Flask(__name__)
# # CORS(app)

# # def get_db():
# #     conn = sqlite3.connect("papers.db")
# #     conn.row_factory = sqlite3.Row
# #     return conn

# # def init_db():
# #     conn = get_db()
# #     conn.execute("""
# #     CREATE TABLE IF NOT EXISTS papers (
# #         id INTEGER PRIMARY KEY AUTOINCREMENT,
# #         name TEXT NOT NULL,
# #         subject TEXT NOT NULL,
# #         year TEXT,
# #         paper_type TEXT,
# #         data TEXT
# #         )
# #     """)
# #     conn.commit()
# #     conn.close()

# # @app.route("/")
# # def home():
# #     return "PastPapers API is running"

# # @app.route("/papers")
# # def get_papers():
# #     conn = get_db()
# #     papers = conn.execute("SELECT * FROM papers").fetchall()
# #     conn.close()
# #     return jsonify([dict(p) for p in papers])

# # @app.route("/add-paper",methods=["POST"])
# # def add_paper():
# #     data = request.get_json()

# #     if not data:
# #         return jsonify({"error": "No data received"}), 400

# #     name = data.get("name")
# #     subject = data.get("subject")
# #     year = data.get("year", "Unknown")
# #     paper_type = data.get("paper_type", "Exam")
# #     file_data = data.get("data","")

# #     if not name or not subject:
# #         return jsonify({"error":"Name and subject are required"}), 400

# #     conn = get_db()
# #     conn.execute(
# #         "INSERT INTO papers (name, subject, year, paper_type) VALUES (?, ?, ?, ?, ?)",
# #         (name, subject, year, paper_type, file_data)
# #     )
# #     conn.commit()
# #     conn.close()

# #     return jsonify({"message": "Paper added successfully"}), 201

# # @app.route("/papers/delete/<int:paper_id>", methods=["DELETE"])
# # def delete_paper(paper_id):
# #     conn = get_db()
# #     conn.execute("  DELETE FROM papers WHERE id = ?", (paper_id,))
# #     conn.commit()
# #     conn.close()
# #     return jsonify({"message": "Paper deleted"}), 200

# # if __name__ == "__main__":
# #     init_db()
# #     app.run(debug=True)


# import os
# import psycopg2
# from psycopg2.extras import RealDictCursor
# from flask import Flask, jsonify, request
# from flask_cors import CORS

# app = Flask(__name__)
# CORS(app)

# DATABASE_URL = os.environ.get('DATABASE_URL')

# def get_db():
#     conn = psycopg2.connect(DATABASE_URL, cursor_factory=RealDictCursor)
#     return conn

# def init_db():
#     conn = get_db()
#     cur = conn.cursor()
#     cur.execute("""
#         CREATE TABLE IF NOT EXISTS papers (
#             id         SERIAL PRIMARY KEY,
#             name       TEXT NOT NULL,
#             subject    TEXT NOT NULL,
#             year       TEXT,
#             paper_type TEXT,
#             data       TEXT
#         )
#     """)
#     conn.commit()
#     cur.close()
#     conn.close()
# # def get_db():
# #     conn = sqlite3.connect("papers.db")
# #     conn.row_factory = sqlite3.Row
# #     return conn

# # def init_db():
# #     conn = get_db()
# #     conn.execute("""
# #         CREATE TABLE IF NOT EXISTS papers (
# #             id         INTEGER PRIMARY KEY AUTOINCREMENT,
# #             name       TEXT NOT NULL,
# #             subject    TEXT NOT NULL,
# #             year       TEXT,
# #             paper_type TEXT,
# #             data       TEXT
# #         )
# #     """)
# #     conn.commit()
# #     conn.close()

# # ============================================
# # ROUTES
# # ============================================

# @app.route("/")
# def home():
#     return "PastPapers API is running"

# @app.route("/papers")
# def get_papers():
#     conn = get_db()
#     cur  = conn.cursor()
#     cur.execute("SELECT * FROM papers")
#     papers = cur.fetchall()
#     cur.close()
#     conn.close()
#     return jsonify([dict(p) for p in papers])

# @app.route("/add-paper", methods=["POST"])
# def add_paper():
#     data = request.get_json()
#     if not data:
#         return jsonify({"error": "No data received"}), 400

#     name       = data.get("name")
#     subject    = data.get("subject")
#     year       = data.get("year", "Unknown")
#     paper_type = data.get("paper_type", "Exam")
#     file_data  = data.get("data", "")

#     if not name or not subject:
#         return jsonify({"error": "Name and subject required"}), 400

#     conn = get_db()
#     cur  = conn.cursor()
#     cur.execute(
#         "INSERT INTO papers (name,subject,year,paper_type,data) VALUES (%s,%s,%s,%s,%s)",
#         (name, subject, year, paper_type, file_data)
#     )
#     conn.commit()
#     cur.close()
#     conn.close()
#     return jsonify({"message": "Paper added"}), 201

# @app.route("/papers/edit/<int:paper_id>", methods=["PUT"])
# def edit_paper(paper_id):
#     data     = request.get_json()
#     new_name = data.get("name")
#     conn = get_db()
#     cur  = conn.cursor()
#     cur.execute("UPDATE papers SET name=%s WHERE id=%s", (new_name, paper_id))
#     conn.commit()
#     cur.close()
#     conn.close()
#     return jsonify({"message": "Updated"}), 200

# @app.route("/papers/delete/<int:paper_id>", methods=["DELETE"])
# def delete_paper(paper_id):
#     conn = get_db()
#     cur  = conn.cursor()
#     cur.execute("DELETE FROM papers WHERE id=%s", (paper_id,))
#     conn.commit()
#     cur.close()
#     conn.close()
#     return jsonify({"message": "Deleted"}), 200

# # ============================================
# # START
# # ============================================
# init_db()
# if __name__ == "__main__":
#     app.run(debug=True)

import os
import psycopg2
from psycopg2.extras import RealDictCursor
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

DATABASE_URL = os.environ.get('DATABASE_URL')

def get_db():
    conn = psycopg2.connect(DATABASE_URL, cursor_factory=RealDictCursor)
    return conn

def init_db():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS papers (
            id         SERIAL PRIMARY KEY,
            name       TEXT NOT NULL,
            subject    TEXT NOT NULL,
            year       TEXT,
            paper_type TEXT,
            data       TEXT
        )
    """)
    conn.commit()
    cur.close()
    conn.close()

@app.route("/")
def home():
    return "PastPapers API is running"

@app.route("/papers")
def get_papers():
    conn = get_db()
    cur  = conn.cursor()
    cur.execute("SELECT * FROM papers")
    papers = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify([dict(p) for p in papers])

@app.route("/add-paper", methods=["POST"])
def add_paper():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data received"}), 400
    name       = data.get("name")
    subject    = data.get("subject")
    year       = data.get("year", "Unknown")
    paper_type = data.get("paper_type", "Exam")
    file_data  = data.get("data", "")
    if not name or not subject:
        return jsonify({"error": "Name and subject required"}), 400
    conn = get_db()
    cur  = conn.cursor()
    cur.execute(
        "INSERT INTO papers (name,subject,year,paper_type,data) VALUES (%s,%s,%s,%s,%s)",
        (name, subject, year, paper_type, file_data)
    )
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({"message": "Paper added"}), 201

@app.route("/papers/edit/<int:paper_id>", methods=["PUT"])
def edit_paper(paper_id):
    data     = request.get_json()
    new_name = data.get("name")
    if not new_name:
        return jsonify({"error": "Name is required"}), 400
    conn = get_db()
    cur  = conn.cursor()
    cur.execute("UPDATE papers SET name=%s WHERE id=%s", (new_name, paper_id))
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({"message": "Updated"}), 200

@app.route("/papers/delete/<int:paper_id>", methods=["DELETE"])
def delete_paper(paper_id):
    conn = get_db()
    cur  = conn.cursor()
    cur.execute("DELETE FROM papers WHERE id=%s", (paper_id,))
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({"message": "Deleted"}), 200

# Runs on both local and Render
init_db()

if __name__ == "__main__":
    app.run(debug=True)