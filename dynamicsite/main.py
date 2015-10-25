
import webapp2
from data import Data, Yarn

class MainHandler(webapp2.RequestHandler):
    def get(self):
      d= Data()
      y = Yarn()

class MainPage(object):

    def __init__(self):
        self.title = "Weather Report"
        self.css = " css/stylesheet.css"

        page = '''<!DOCTYPE HTML>



<html>
    <head>
        <title> Brittni's Yarn</title>
    </head>

    <body> <h1>Welcome to Brittni's Yarn Shop!</h1>
        <p>We have a variety of yarn for you to choose from. Please select one of the choices below.</p>

    <div id="yarns">
        <ul>
            <li id="thick"><a href="?Yarn=thickandquick">Thick and Quick</a>
            <br>
            <small>Price: $6.99</small>
            <li id="home"><a href="?Yarn=hometown">Hometown</a>
            <br>
            <small>Price:$3.99</small>
            <li id="vanna"><a href="?Yarn=vannaschoice">Vanna's Choice</a>
            <br>
            <small>Price: $4.99</small>
            <li id="super"><a href="?Yarn=supersaver">Super Saver</a>
            <br>
            <small>Price: $2.99</small>
            <li id="buttercream"><a href="?Yarn=buttercream">Thick and Thin</a>
            <br>
            <small>Price: $8.99</small>
        </ul>
    </div>
    </body>
</html>'''

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
