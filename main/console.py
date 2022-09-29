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

member_4 = Member('Kate', 'Veatch', True, True)
member_repository.save(member_4)

member_5 = Member('Justin', 'Redman', False, True)
member_repository.save(member_5)

member_6 = Member('MeShell', 'Jones', True, True)
member_repository.save(member_6)

course_1_date = datetime.date(2022, 10, 12)
course_1 = Course('Dodgeball', 'If you can dodge a wrench, you can dodge a ball', course_1_date, 10)
course_repository.save(course_1)

course_2_date = datetime.date(2022, 11, 24)
course_2 = Course('Football Tactics', 'We never stop! Formations and how to play fast paced footy', course_2_date, 30)
course_repository.save(course_2)

course_3_date = datetime.date(2023, 4, 7)
course_3 = Course('Beach Volleyball', 'Learn how to play dirty. We show you the best techniques for throwing sand in your opponents eyes!', course_2_date, 4)
course_repository.save(course_3)

course_4_date = datetime.date(2023, 5, 11)
course_4 = Course('Celebrity Deathmatch', 'Learn how to fight like a plastecene person', course_2_date, 8)
course_repository.save(course_4)

booking_1 = Booking(member_1, course_1)
booking_repository.save(booking_1)

booking_2 = Booking(member_5, course_1)
booking_repository.save(booking_2)

booking_3 = Booking(member_3, course_2)
booking_repository.save(booking_3)

booking_4 = Booking(member_1, course_3)
booking_repository.save(booking_4)

booking_5 = Booking(member_2, course_3)
booking_repository.save(booking_5)

booking_6 = Booking(member_4, course_3)
booking_repository.save(booking_6)

pdb.set_trace