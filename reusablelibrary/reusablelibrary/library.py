class FavoriteMovies(object):
    def __init__(self):
        self._movie_list
        #have an array to hold the movie information
        #some way to add to the array
        #generate a list of the movies
        #caluclate time span between movies

    def addMovie(self,m):
        self.movie_list.append(m)
        print m



class MovieData(object): # Data Object
    def __init__(self):
        self.title = ''
        self._year = 0 #check for valid year
        self.director = ''

    @property
    def year(self):
        pass

    @year.setter
    def year(self, y):
        if y is > 2015:
           print "Error, invalid date!"
           self._year = 2014
        else:
            self._year = y
