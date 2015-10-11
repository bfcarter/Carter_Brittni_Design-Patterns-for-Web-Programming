
import webapp2
from library import Library
#from pages import ResultsPage

class MainHandler(webapp2.RequestHandler):
    def get(self):

        #page for class
        p = Form()
        l = Library()
        if self.request.GET:
            temp = int(self.request.GET["temperature"])
            c = l.convert_celuis(temp)
            self.response.write("<h1>you got form crap " + str(c) + "</h1>")
        else:
            self.response.write(p.print_out())
        #lib = FavoriteCar()
class Form(object):
    def __init__(self):
        self.title = "Weather Report"
        self.css = " css/stylesheet.css"
        self.head = """

<!DOCTYPE HTML>
<html>

    <head>
        <title>{self.title}</title>
        <link rel="stylesheet" href="{self.css}">
    </head>
    <img src= "http://brittnicarter.com/wp-content/uploads/2015/07/logo-300x300.png" width= "100" height= "115">
    <h1>Weather Report</h1>
    <body>"""



        # form
        self.body = '''<form method="GET" action=""
        <label>Name:</label><input type="text" name="name"/>
        <label>City: </label><input type="text" name="city"/>
        <label>Temperature </label><input type="text" name="temperature"/>
        <input type="radio" name="transmission" value="Automatic" checked>Automatic
        <input type="radio" name="transmission" value="Manual">Manual
            <input type="submit" value="Submit"/>
            <p>What does it look like outside?</p>
            <select name="colors">
                <option value="sunny">Sunny</option>
                <option value="cloudy">Cloudy</option>
                <option value="thunderstorm">Thunderstorm</option>
                <option value="other">Other</option>
            </select>

            '''
        self.close = """

        </form>
    </body>
</html>
    """
    def print_out(self):
        all = (self.head + self.body + self.close).format(**locals())
        return all
       # self.body = lib.compile_list()
        #self.response.write(self.body.print_out())
class ResultsForm(object):
    def __init__(self):
        self.title = "Weather Report"
        self.css = " css/stylesheet.css"
        self.head = """


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
