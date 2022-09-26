from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.course import Course
import repositories.course_repository as course_repository
import repositories.member_repository as member_repository

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

@courses_blueprint.route("/courses/<id>")
def show_course(id):
    course = course_repository.select(id)
    members, number_of_members = course_repository.members(course)
    all_members = member_repository.select_all()
    return render_template("courses/show.html", course=course, members=members, all_members=all_members, number_of_members=number_of_members)

@courses_blueprint.route("/courses/<id>/edit")
def edit_course(id):
    course = course_repository.select(id)
    return render_template("courses/edit.html", course=course)

@courses_blueprint.route("/courses/<id>", methods=["POST"])
def update_course(id):
    name = request.form["name"]
    description = request.form["description"]
    date = request.form["date"]
    capacity = request.form["capacity"]
    course = Course(name, description, date, capacity, id)
    course_repository.update(course)
    return redirect("/courses")

@courses_blueprint.route("/courses/<id>/delete", methods=["POST"])
def delete_course(id):
    course_repository.delete(id)
    return redirect("/courses")