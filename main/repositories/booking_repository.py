from db.run_sql import run_sql
from models.booking import Booking
from models.member import Member
import repositories.member_repository as member_repository
from models.course import Course
import repositories.course_repository as course_repository

def save(booking):
    sql = "INSERT INTO bookings (member_id, course_id) VALUES (%s, %s) RETURNING id"
    values = [booking.member.id, booking.course.id]
    results = run_sql(sql, values)
    booking.id = results[0]['id']

def select_all():
    bookings = []
    sql = "SELECT * FROM bookings"
    results = run_sql(sql)
    for result in results:
        member = member_repository.select(result['member_id'])
        course = course_repository.select(result['course_id'])
        booking = Booking(member, course, result['id'])
        bookings.append(booking)
    return bookings

def select(id):
    booking = None
    sql = "SELECT * FROM bookings WHERE id = %s"
    values = [id]

    results = run_sql(sql, values)
    if results:
        result = results[0]
        member = member_repository.select(result['member_id'])
        course = course_repository.select(result['course_id'])
        booking = Booking(member, course, result['id'])
    return booking

def delete_all():
    sql = "DELETE FROM bookings"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM bookings WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(booking):
    sql = "UPDATE bookings SET (member_id, course_id) = (%s, %s) WHERE id = %s"
    values = [booking.member.id, booking.course.id, booking.id]
    run_sql(sql, values)