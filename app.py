# app.py

from flask import Flask, render_template, request, g
from flask_sqlalchemy import SQLAlchemy
import sqlite3

# --- App and Database Configuration ---

app = Flask(__name__)
# This creates a database file named 'blog.db' in a special 'instance' folder.
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
db = SQLAlchemy(app)

# --- Database Model Definition ---

# This class defines the 'post' table in our database.
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.String(500), nullable=False)

    def __repr__(self):
        return f'<Post {self.title}>'

# --- Database Connection for Raw (Vulnerable) Queries ---
DATABASE = 'instance/blog.db'

def get_db():
    # Establishes a raw connection to the database file.
    db_conn = getattr(g, '_database', None)
    if db_conn is None:
        db_conn = g._database = sqlite3.connect(DATABASE)
    return db_conn

@app.teardown_appcontext
def close_connection(exception):
    # Closes the connection when the request is done.
    db_conn = getattr(g, '_database', None)
    if db_conn is not None:
        db_conn.close()

# --- Routes (Web Pages) ---

@app.route('/', methods=['GET'])
def index():
    query_param = request.args.get('search')

    if query_param:
        # This whole block is now correctly indented
        conn = get_db()
        cursor = conn.cursor()

        # --- THE SECURE FIX ---
        # The query uses a '?' as a safe placeholder.
        query = "SELECT * FROM post WHERE title LIKE ?"
        # The user input is passed in safely as a separate parameter.
        cursor.execute(query, (f'%{query_param}%',))

        posts_tuples = cursor.fetchall()
        posts = [{'title': row[1], 'content': row[2]} for row in posts_tuples]
    else:
        # This runs if there's no search term
        posts = Post.query.all()

    return render_template('index.html', posts=posts)