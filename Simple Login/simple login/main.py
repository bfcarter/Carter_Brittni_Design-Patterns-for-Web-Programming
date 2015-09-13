
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
        <title>Simple Form</title>
    </head>
    <body>'''

        page_body = '''<form method="GET" action=""
        <label>Name: </label><input type="text" name="user"/>
        <label>Email: </label><input type="text" name="email"/>
        <input type="submit" value="Submit"/>
        <input type="radio" name="sex" value="male" checked>Male
        <input type="radio" name="sex" value="female">Female'''
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
