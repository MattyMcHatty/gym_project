from db.run_sql import run_sql
from models.member import Member

def save(member):
    sql = "INSERT INTO members (first_name, last_name, premium, active) VALUES (%s, %s, %s, %s) RETURNING id"
    values = [member.first_name, member.last_name, member.premium, member.active]
    results = run_sql(sql, values)
    id = results[0],['id']
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

