import pdb
import datetime

from models.booking import Booking
import repositories.booking_repository as booking_repository

from models.member import Member
import repositories.member_repository as member_repository

from models.course import Course
import repositories.course_repository as course_repository

booking_repository.delete_all()
member_repository.delete_all()
course_repository.delete_all()

member_1 = Member('White', 'Goodman', False, True)
member_repository.save(member_1)

member_2 = Member('Pat', 'O Houlihan', False, True)
member_repository.save(member_2)

member_3 = Member('Steve', 'Cowan', False, True)
member_repository.save(member_3)

course_1_date = datetime.date(2022, 10, 12)
course_1 = Course('Dodgeball', 'If you can dodge a wrench, you can dodge a ball', course_1_date, 10)
course_repository.save(course_1)

course_2_date = datetime.date(2022, 11, 24)
course_2 = Course('Football Tactics', 'We never stop! Formations and how to play fast paced footy', course_2_date, 30)
course_repository.save(course_2)

booking_1 = Booking(member_1, course_1)
booking_repository.save(booking_1)

booking_2 = Booking(member_2, course_1)
booking_repository.save(booking_2)

booking_3 = Booking(member_3, course_2)
booking_repository.save(booking_3)

pdb.set_trace