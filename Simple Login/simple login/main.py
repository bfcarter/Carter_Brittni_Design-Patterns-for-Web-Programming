
'''
Brittni Carter
9-8-15
Setting up the launcher
Design Patterns for Web Programming
'''

import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        page = '''<DOCTYPE HTML>
<HTML>
    <head>
        <title>Simple Form</title>
    </head>
    <body>
        <form method="GET">
            <label>Name:</label><input type="text" name="user"/>
            <label>Email:</label><input type="text" name="email"/>
            <input type="submit" value="submit"/>
        </form>

    </body>
</HTML>'''
        if self.request.GET:
            user= self.request.GET ['user']
            email= self.request.GET ['email']
        self.response.write('Hello world!') #print

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
