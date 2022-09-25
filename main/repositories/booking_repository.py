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
    id = results[0]['id']
    booking.id = id

