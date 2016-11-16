#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  sample.py
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

from app import App

# class CreateUser(App.http):
#     def post(self):
#         try:
#             # Parse the arguments
#             App.req.add_argument('email', type=str, help='Email address to create user')
#             App.req.add_argument('password', type=str, help='Password to create user')

#             args = App.req.parse_args()

#             _userEmail = args['email']
#             _userPassword = args['password']

#             return {'Email': _userEmail, 'Password': _userPassword}

#         except Exception as e:
#             return {'error': str(e)}

class CreateUser(App.http):
    def post(self):
        try:
            docs = list()
            for doc in App.db.table('test_table').run(App.con):
                docs.append(doc)

            App.response['data'] = docs
            App.response['paging'] = len(docs)
            return App.response

        except Exception as e:
            return {
                'error': str(e),
            }