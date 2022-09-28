from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.booking import Booking
import repositories.booking_repository as booking_repository
import repositories.member_repository as member_repository
import repositories.course_repository as course_repository

bookings_blueprint = Blueprint("bookings", __name__)

@bookings_blueprint.route("/bookings")
def bookings():
    bookings = booking_repository.select_all()
    return render_template("bookings/index.html", bookings=bookings)

@bookings_blueprint.route("/bookings/new", methods=['GET'])
def new_booking():
    members = member_repository.select_all()
    courses = course_repository.select_all()
    return render_template("bookings/new.html", members=members, courses=courses)

@bookings_blueprint.route("/bookings", methods=["POST"])
def create_booking():
    member_id = request.form['member_id']
    course_id = request.form['course_id']
    redirector = request.form['redirector']
    member = member_repository.select(member_id)
    course = course_repository.select(course_id)
    booking = Booking(member, course)
    booking_repository.save(booking)
    if redirector == 'member_edit':
        return redirect("members/" + str(member.id) + "/edit")
    elif redirector == 'course_show':
        return redirect("courses/" + str(course.id))
    else:
        return redirect("/bookings")

@bookings_blueprint.route("/bookings/<id>/delete", methods=["POST"])
def delete_booking(id):
    booking_repository.delete(id)
    return redirect("/bookings")