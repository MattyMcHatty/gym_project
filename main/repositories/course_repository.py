from db.run_sql import run_sql
from models.member import Member
from models.course import Course

def save(course):
    sql = "INSERT INTO courses (name, description, date, capacity) VALUES (%s, %s, %s, %s) RETURNING id"
    values = [course.name, course.description, course.date, course.capacity]
    results = run_sql(sql, values)
    id = results[0]['id']
    course.id = id


