from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.course import Course
import repositories.course_repository as course_repository

courses_blueprint = Blueprint("courses", __name__)

@courses_blueprint.route("/courses")
def courses():
    courses = course_repository.select_all()
    return render_template("courses/index.html", courses=courses)

@courses_blueprint.route("/courses/new")
def new_course():
    return render_template("/courses/new.html")

@courses_blueprint.route("/courses", methods=["POST"])
def create_course():
    name = request.form["name"]
    description = request.form["description"]
    date = request.form["date"]
    capacity = request.form["capacity"]
    new_course = Course(name, description, date, capacity)
    course_repository.save(new_course)
    return redirect("/courses")