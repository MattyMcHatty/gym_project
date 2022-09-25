from db.run_sql import run_sql
from models.member import Member

def save(member):
    sql = "INSERT INTO members (first_name, last_name, premium, active) VALUES (%s, %s, %s, %s) RETURNING id"
    values = [member.first_name, member.last_name, member.premium, member.active]
    results = run_sql(sql, values)
    id = results[0],['id']
    member.id = id

