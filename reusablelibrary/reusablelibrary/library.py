class Library(object):
    def __init__(self):
        self.title = "Weather Report"
        self.css = " css/stylesheet.css"
        

    def convert_celuis(self,t):
        return (t - 32) * 0.55555555555
    def convert_kelvin(self,t):
        return (t + 459.67) * 0.55555555555
    def convert_rankine(self,t):
        return (t + 459.67)
