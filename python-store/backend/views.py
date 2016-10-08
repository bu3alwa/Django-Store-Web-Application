import sys
import os

from flask import render_template, request, session, redirect, session, Blueprint, abort, flash
from backend import app
from models import *
from backend import db
from jinja2 import TemplateNotFound



@app.route('/', methods=['GET'])
def index():
    return home

@app.route('/login', methods=['GET', 'POST'])
def login():


@app.route("/logout")
@login_required
def logout():
    logout_user()
        return redirect(/)
