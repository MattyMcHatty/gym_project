from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.course import Course
import repositories.course_repository as course_repository

courses_blueprint = Blueprint("courses", __name__)