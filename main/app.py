from flask import Flask, render_template

from controllers.members_controller import members_blueprint
from controllers.courses_controller import courses_blueprint
from controllers.bookings_controller import bookings_blueprint

import repositories.member_repository as member_repository
import repositories.course_repository as course_repository

app = Flask(__name__)

app.register_blueprint(members_blueprint)
app.register_blueprint(courses_blueprint)
app.register_blueprint(bookings_blueprint)

@app.route("/")
def main():
    members = member_repository.select_all()
    courses = course_repository.select_all()
    return render_template('index.html', members=members, courses=courses)

if __name__ == '__main__':
    app.run()