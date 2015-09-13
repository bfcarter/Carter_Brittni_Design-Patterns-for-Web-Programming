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
        page= '''<!DOCTYPE HTML>
<html>
    <head>
        <title>Simple Form</title>
    </head>
    <body>
        <form method="GET" action=""
        <label>Name: </label><input type="text" name="user"/>
        <label>Email: </label><input type="text" name="email"/>
        <input type="submit" value="Submit"/>
        </form>
    </body>
</html>'''
        if self.request.GET:
            #stores info we got from the form
            user = self.request.GET['USER']
            email = self.request.GET ['email']

        self.response.write(page) #print

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)