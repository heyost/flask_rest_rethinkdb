#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  __init__.py
#  
#  Flask REST API with RethinkDB as DB
#
#  Copyright (C) 2016  Muhamad Fajar <therevance@gmail.com>
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

# Import config as dictionary
import app.config as conf

# Import everything related with project
from flask import Flask
from flask_restful import Resource, Api, reqparse
from rethinkdb import rethinkdb

# Main class, base object from app
class App():
    # Initializing Flask as base application
    main = Flask(__name__)

    # Initializing RethinkDB as database
    con = rethinkdb.connect(conf.HOST, conf.PORT, conf.DB, conf.USER, conf.PASSWORD)
    db = rethinkdb
    
    # Call API function
    api = Api(main, catch_all_404s=True)

    # Initializing HTTP resource from library
    http = Resource
    req = reqparse.RequestParser()

    def __init__(self):
        super(App, self).__init__()
        self.main = main
        self.con = con
        self.db = db
        self.api = api
        self.http = http
        self.req = req
        
# Import route configuration
import app.route

# Load FLask configuration
App.main.config.from_object('app.config')
