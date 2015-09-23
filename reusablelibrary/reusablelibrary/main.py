
import webapp2
from library import CarData, FavoriteCar
from pages import ResultsPage

class MainHandler(webapp2.RequestHandler):
    def get(self):

        #page for class
        p = ResultsPage()
        lib = FavoriteCar
class Form(object):
    def __init__(self):
        self.title = "Welcome!"
        self.css = " css/stylesheet.css"
        self.head = """

<!DOCTYPE HTML>
<html>

    <head>
        <title>What is your favorite cAR?</title>
        <link rel="stylesheet" href="{self.css}">
    </head>
    <img src= "http://brittnicarter.com/wp-content/uploads/2015/07/logo-300x300.png" width= "100" height= "115">
    <h1>What is your Two Favorite Car?</h1>
    <body>"""



        # form
        self.body = '''<form method="GET" action=""
        <p> First Car </p>
        <label>Make: </label><input type="text" name="make"/>
        <label>Model: </label><input type="text" name="model"/>
        <label>Year: </label><input type="text" name="year"/>
        <input type="radio" name="transmission" value="Automatic" checked>Automatic
        <input type="radio" name="transmission" value="Manual">Manual
            <input type="submit" value="Submit"/>
            <p>What color?</p>
            <select name="colors">
                <option value="blue">Blue</option>
                <option value="black">Black</option>
                <option value="yellow">Yellow</option>
                <option value="green">Green</option>
                <option value="orange">Orange</option>
                <option value="red">Red</option>
                <option value="other">Other</option>
            </select>
            <input type="submit" value="Submit"/><label>Make: </label><input type="text" name="make"/>
        <p> Second Car</p>
        <label>Model: </label><input type="text" name="model"/>
        <label>Year: </label><input type="text" name="year"/>
        <input type="radio" name="transmission" value="Automatic" checked>Automatic
        <input type="radio" name="transmission" value="Manual">Manual
            <input type="submit" value="Submit"/>
            <p>What color?</p>
            <select name="colors">
                <option value="blue">Blue</option>
                <option value="black">Black</option>
                <option value="yellow">Yellow</option>
                <option value="green">Green</option>
                <option value="orange">Orange</option>
                <option value="red">Red</option>
                <option value="other">Other</option>
            </select>
            <input type="submit" value="Submit"/>
            '''
        self.close = """

        </form>
    </body>
</html>
    """

        p.body = lib.compile_list()
        self.response.write(p.print_out())

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
