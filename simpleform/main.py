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
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        page_head = '''<!DOCTYPE HTML>
<html>

    <head>
        <title>Contact Human Resources Department Form</title>
        <link rel="stylesheet" href="css/style.css">
    </head>
    <img src= "http://brittnicarter.com/wp-content/uploads/2015/07/logo-300x300.png" width= "100" height= "115">
    <h1>Contact Human Resources Department Form</h1>
    <body>'''

        # form
        page_body = '''<form method="GET" action=""
        <label>Name: </label><input type="text" name="user"/>
        <label>Email: </label><input type="text" name="email"/>
        <label>Phone: </label><input type="text" name="phone"/>
        <input type="radio" name="sex" value="male" checked>Male
        <input type="radio" name="sex" value="female">Female

        <p>Who would you like to contact?</p>
            <select name="contact">
                <option value="donald">Donald</option>
                <option value="Richard">Richard</option>
                <option value="lisa">Lisa</option>
                <option value="rhonda">Rhonda</option>
            </select>
            <input type="submit" value="Submit"/>
            '''
        page_close = '''

        </form>
    </body>
</html>'''

        if self.request.GET:
            #stores info we got from the form
            user = self.request.GET['user']
            email = self.request.GET['email']
            sex = self.request.GET['sex']
            phone = self.request.GET['phone']
            contact = self.request.GET['contact']
            self.response.write(page_head + user + ' ' + email + ' ' + sex + ' ' + phone + ' ' + contact + ' ' + page_close)
        else:
            self.response.write(page_head + page_body + page_close) #print

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)