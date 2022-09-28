from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.member import Member
from models.booking import Booking
import repositories.member_repository as member_repository
import repositories.course_repository as course_repository
import repositories.booking_repository as booking_repository

members_blueprint = Blueprint("members", __name__)

@members_blueprint.route("/members")
def members():
    members = member_repository.select_all()
    return render_template("members/index.html", members=members)

@members_blueprint.route("/members/new")
def new_member():
    return render_template("/members/new.html")

@members_blueprint.route("/members", methods=["POST"])
def create_member():
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    premium = request.form["premium"]
    new_member = Member(first_name, last_name, premium, True)
    member_repository.save(new_member)
    return redirect("/members")

@members_blueprint.route("/members/<id>/edit")
def edit_member(id):
    member = member_repository.select(id)
    courses = member_repository.courses(member)
    all_courses = course_repository.select_all()
    bookings = booking_repository.select_all()
    return render_template("members/edit.html", member=member, courses=courses, all_courses=all_courses, bookings=bookings)

@members_blueprint.route("/members/<id>", methods=["POST"])
def update_member(id):
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    premium = request.form["premium"]
    active = request.form["active"]
    member = Member(first_name, last_name, premium, active, id)
    member_repository.update(member)
    return redirect("/members")

@members_blueprint.route("/members/<id>/delete", methods=["POST"])
def delete_member(id):
    member_repository.delete(id)
    return redirect("/members")
