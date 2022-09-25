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

