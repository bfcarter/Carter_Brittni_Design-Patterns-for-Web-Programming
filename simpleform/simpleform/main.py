
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
        l = Library()
class Form(object):
    def __init__(self):
        self.title = "Weather Report"
        self.css = " css/stylesheet.css"
        self.head = """




app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)