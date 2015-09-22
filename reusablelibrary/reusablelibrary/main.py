
import webapp2
from library import MovieData, FavoriteMovies
from pages import ResultsPage
class MainHandler(webapp2.RequestHandler):
    def get(self):

        #page for class
        p = ResultsPage()
        lib = FavoriteMovies

        #movie title
        #year movie was made
        #director of the film
        md1 = MovieData()
        md1.title = "The Princes Bride"
        md1.year = 1989
        md1.director = "Rob Reiner"
        lib.addMovie(md1)

        md2 = MovieData()
        md2.title = "Dune"
        md2.year = 1986
        md2.director = "David Lynch"


        self.response.write(p.print_out())

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
