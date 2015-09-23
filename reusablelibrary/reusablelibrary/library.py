class FavoriteCar(object):
    def __init__(self):
        self.__car__list = []
        #have an array to hold the movie information
        #some way to add to the array
        #generate a list of the movies
        #caluclate time span between movies

    def add_car(self,m):
        self.car__list.append(m)
        print m.title


    def compile_list(self):
        output = ''
        for season in self.__car__list:
            output += 'Make' + car.make + '(' + str(car.year) +') ' + car.model + '<br />'
        return output
    def calc_time_span(self):
        '''

        calculate the time in between cars
        '''
        years = []
        for movie in self.__car_list:
            years.append(car.year)

        years.sort()

        num = len(years) - 1
        span = years[num] - years[0]
        return 'The span between your favorite car is' + str(span)

    @property
    def car__list(self):
        return self.__car__list




class CarData(object): # Data Object
    def __init__(self):
        self.title = ''
        self._year = 0 #check for valid year
        self.director = ''

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, y):
        if y > 2015:
           print "Error, invalid date!"
           self._year = 2015
        else:
            self._year = y
