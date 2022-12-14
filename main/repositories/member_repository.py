from db.run_sql import run_sql
from models.member import Member
from models.course import Course

def save(member):
    sql = "INSERT INTO members (first_name, last_name, premium, active) VALUES (%s, %s, %s, %s) RETURNING id"
    values = [member.first_name, member.last_name, member.premium, member.active]
    results = run_sql(sql, values)
    id = results[0]['id']
    member.id = id

def select_all():
    members = []
    sql = "SELECT * FROM members"
    results = run_sql(sql)
    for result in results:
        member = Member(result['first_name'], result['last_name'], result['premium'], result['active'], result['id'])
        members.append(member)
    return members

def select(id):
    member = None
    sql = "SELECT * FROM members WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        member = Member(result['first_name'], result['last_name'], result['premium'], result['active'], result['id'])
    return member

def delete_all():
    sql = "DELETE FROM members"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM members WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(member):
    sql = "UPDATE members SET (first_name, last_name, premium, active) = (%s, %s, %s, %s) WHERE id = %s"
    values = [member.first_name, member.last_name, member.premium, member.active, member.id]
    run_sql(sql, values)

def courses(member):
    courses =[]
    sql = "SELECT courses.* FROM courses INNER JOIN bookings on bookings.course_id = courses.id WHERE member_id = %s"
    values = [member.id]
    results = run_sql(sql, values)

    for row in results:
        course = Course(row['name'], row['description'], row['date'], row['capacity'], row['id'])
        courses.append(course)

    return courses