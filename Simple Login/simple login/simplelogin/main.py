#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

'''
Brittni Carter
9-8-15
Setting up the launcher
Design Patterns for Web Programming
'''

import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        page_head = '''<!DOCTYPE HTML>
<html>
    <head>
        <title>Simple Contact Form</title>
    </head>
    <body>'''

        page_body = '''<form method="GET" action=""
        <label>Name: </label><input type="text" name="user"/>
        <label>Email: </label><input type="text" name="email"/>
        <input type="radio" name="sex" value="male" checked>Male
        <input type="radio" name="sex" value="female">Female
        <input type="submit" value="Submit"/>
        <p>Who would you like to contact?</p>
            <a href="?email=donald@hr.com&user="Donald">Donald</a><br/>
            <a href="?email=richard@hr.com&user="Richard">Richard</a><br/>
            <a href="?email=brenda@hr.com&user="Brenda">Brenda</a><br/>
            <a href="?email=lisa@hr.com&user="Lisa">Lisa</a><br/>'''
        page_close = '''

        </form>
    </body>
</html>'''

        if self.request.GET:
            #stores info we got from the form
            user = self.request.GET['USER']
            email = self.request.GET ['email']
            self.response.write(page_head + user + ' ' + email + page_body + page_close)
        else:
            self.response.write(page_head + page_body + page_close) #print

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)