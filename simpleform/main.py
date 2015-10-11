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
        f = Form()


class Form(object):
    def __init__(self):
        self.title = "Magazine Sign Up"
        self.css = " css/style.css"
        self.head = """
<!DOCTYPE HTML>
<html>
    <head>
        <title>{self.title}</title>
        <link href="{self.css}" rel="stylesheet" type="text/css"/>
    </head>
    <img src= "http://brittnicarter.com/wp-content/uploads/2015/07/logo-300x300.png" width= "100" height= "115">
    <body>
        """
        self.body = '''<form method="GET" action=""
        <h1>"Sign Up for our mailing list!"
        <label>Name: </label><input type="text" name="user"/>
        <label>Email: </label><input type="text" name="email"/>
        <label>Phone: </label><input type="text" name="phone"/>
        <input type="radio" name="sex" value="male" checked>Male
        <input type="radio" name="sex" value="female">Female

        <p>What product are you most interested in?</p>
            <select name="product">
                <option value="Body Butter">Body Butter</option>
                <option value="Sugar Scrub">Sugar Scrub</option>
                <option value="Shea Soap">Shea Soap</option>
                <option value="Lip Balm">Lip Balm</option>
            </select>
            <input type="submit" value="Submit"/>
            '''
        self.close = """

        </form>
    </body>
</html>
        """

        if self.body.GET:
            #stores info we got from the form
            user = self.body.GET['user']
            email = self.body.GET['email']
            sex = self.body.GET['sex']
            phone = self.body.GET['phone']
            contact = self.body.GET['product']
            self.body.write(self.head + user + ' ' + email + ' ' + sex + ' ' + phone + ' ' + contact + ' ' + self.close)
        else:
            self.body.write(self.head + self.body + self.close) #print

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)

