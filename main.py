#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  main.py
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

# Import main class from module app
from app import App

# Define root as main executable
if __name__ == "__main__":
    App.main.run()