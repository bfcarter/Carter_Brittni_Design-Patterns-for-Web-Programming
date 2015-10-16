class Library(object):
    def __init__(self):
        pass

#math for temp
    def convert_celuis(self,t):
        return (t - 32) * 0.55555555555
    def convert_kelvin(self,t):
        return (t + 459.67) * 0.55555555555
    def convert_rankine(self,t):
        return (t + 459.67)

