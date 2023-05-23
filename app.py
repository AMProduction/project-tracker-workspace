#  Copyright (c) 2023. AMProduction

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://user:password@localhost/project_tracker"
app.config["SECRET_KEY"] = b'-8\xd5\xdb\xa7\xe1\xd0pW\x8f\xadD\x8e`<C\xee\x16\x0f\xb4\x84rz`'
db = SQLAlchemy(app)


class Project(db.Model):
    __tablename__ = 'projects'
    project_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(length=50))


class Task(db.Model):
    __tablename__ = 'tasks'
    task_id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('projects.project_id'))
    description = db.Column(db.String(length=50))

    project = db.relationship("Project")


@app.route("/")
def show_projects():
    return render_template("index.html", projects=Project.query.all())


@app.route("/project/<project_id>")
def show_tasks(project_id):
    return render_template("project-tasks.html", project=Project.query.filter_by(project_id=project_id).first(),
                           tasks=Task.query.filter_by(project_id=project_id).all())


@app.route("/add/project", methods=['POST'])
def add_project():
    # TODO: Add project
    return "Project added successfully"


@app.route("/add/task/<project_id>", methods=['POST'])
def add_task(project_id):
    # TODO Add task
    return "Task added successfully"


app.run(debug=True, host="127.0.0.1", port=3000)
