from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import os
import sys
import yaml
import argparse

parser = argparse.ArgumentParser(prog='pyapp')
parser.add_argument("-c", "--config", help="path to config file", type=str, required=True)
args = parser.parse_args()

f = open(args.config)

conf = yaml.load(f)
PORT = conf['port']
SECRET_KEY = conf['secret-key']

app = Flask(__name__)

app.config['SECRET_KEY'] = SECRET_KEY

app.debug = True
