
'''
Brittni Carter
9-8-15
Setting up the launcher
Design Patterns for Web Programming
'''

import webapp2
from pages import Page

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = Page()




app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)