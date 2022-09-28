from db.run_sql import run_sql
from models.member import Member
from models.course import Course

def save(course):
    sql = "INSERT INTO courses (name, description, date, capacity) VALUES (%s, %s, %s, %s) RETURNING id"
    values = [course.name, course.description, course.date, course.capacity]
    results = run_sql(sql, values)
    id = results[0]['id']
    course.id = id


def select_all():
    courses = []
    sql = "SELECT * FROM courses"
    results = run_sql(sql)
    for result in results:
        course = Course(result['name'], result['description'], result['date'], result['capacity'], result['id'])
        courses.append(course)
    return courses

def select(id):
    sql = "SELECT * FROM courses WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        course = Course(result['name'], result['description'], result['date'], result['capacity'], result['id'])
    return course

def delete_all():
    sql = "DELETE FROM courses"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM courses WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(course):
    sql = "UPDATE courses SET (name, description, date, capacity) = (%s, %s, %s, %s) WHERE id = %s"
    values = [course.name, course.description, course.date, course.capacity, course.id]
    run_sql(sql, values)

def members(course):
    members = []

    sql = "SELECT members.* FROM members INNER JOIN bookings ON bookings.member_id = members.id WHERE course_id = %s"
    values = [course.id]
    results = run_sql(sql, values)

    for row in results:
        member = Member(row['first_name'], row['last_name'], row['premium'], row['active'], row['id'])
        members.append(member)

    number_of_members = len(members)

    return members, number_of_members