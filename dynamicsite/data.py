from library import yarnUtilities

class CostPerYard(object):
    def __init__(self):
        self.gauge = 0.00
        self.weight = 0.00
        self.name = ""
        self.yards = 0.00
        self.image = ""
        self.brand = ""


class Yarn(CostPerYard):
    def __init__(self):
        super(Yarn, self).__init__()
        self.cost = 0.00

    @property
    def cost(self):
        return self.cost

    @cost.setter
    def cost(self, c):
        self.cost = c

class KnittingYarn(Yarn):
def __init__(self):
    super(KnittingYarn, self).__init__()

    util = yarnUtilities()

    thickandquick = Yarn()
    thickandquick.cost = 6.99
    thickandquick.name = "Thick and Quick"
    thickandquick.weight = 6
    thickandquick.size = 6
    thickandquick.gauge = 4
    thickandquick.yards = 107
    thickandquick.brand = "Lion Brand"
    thickandquick.image = "http://cdn-us-ec.yottaa.net/551561a7312e580499000a44/6dfc9540b6ba0132c6c50a3ba3fac80a.yottaa.net/v~c.1d/aamm_prd/on/demandware.static/-/Sites-joann-product-catalog/default/dw44aa51c7/images/hi-res/master/prd12018.jpg?yocs=u_&yoloc=us"


    vannaschoice = Yarn()
    vannaschoice.cost = 4.99
    vannaschoice.name = "Vanna's Choice"
    vannaschoice.weight = 4
    vannaschoice.size = 3.5
    vannaschoice.gauge = 4
    vannaschoice.yards = 171
    vannaschoice.brand = "Lion Brand"
    vannaschoice.image = "http://cdn-us-ec.yottaa.net/551561a7312e580499000a44/6dfc9540b6ba0132c6c50a3ba3fac80a.yottaa.net/v~c.1d/aamm_prd/on/demandware.static/-/Sites-joann-product-catalog/default/dw52abd6bc/images/hi-res/master/xprd90044.jpg?yocs=u_&yoloc=us"


    buttercream = Yarn()
    buttercream.cost = 8.99
    buttercream.name = "Thick and Thin"
    buttercream.weight = 5
    buttercream.size = 4
    buttercream.gauge = 8
    buttercream.yards = 92
    buttercream.brand = "Buttercream"
    buttercream.image = "http://cdn-us-ec.yottaa.net/551561a7312e580499000a44/6dfc9540b6ba0132c6c50a3ba3fac80a.yottaa.net/v~c.1d/aamm_prd/on/demandware.static/-/Sites-joann-product-catalog/default/dw7d1accc7/images/hi-res/master/zprd_14328629a.jpg?yocs=u_&yoloc=us"

    hometown = Yarn()
    hometown.cost = 3.99
    hometown.name = "Hometown"
    hometown.weight = 5
    hometown.size = 6
    hometown.yards = 81
    hometown.gauge = 4
    hometown.brand = "Lion Brand"
    hometown.image = 'http://cdn-us-ec.yottaa.net/551561a7312e580499000a44/6dfc9540b6ba0132c6c50a3ba3fac80a.yottaa.net/v~c.1d/aamm_prd/on/demandware.static/-/Sites-joann-product-catalog/default/dw2c0bef66/images/hi-res/master/zprd_02108959a.jpg?yocs=u_&yoloc=us'

    supersaver = Yarn()
    supersaver.cost = 2.99
    supersaver.name = "Super Saver"
    supersaver.weight = 7
    supersaver.size = 6
    supersaver.yards = 364
    supersaver.gauge = 4
    supersaver.brand = "Red Heart"
    supersaver.image = 'http://cdn-us-ec.yottaa.net/551561a7312e580499000a44/6dfc9540b6ba0132c6c50a3ba3fac80a.yottaa.net/v~c.1d/aamm_prd/on/demandware.static/-/Sites-joann-product-catalog/default/dw61b5c854/images/hi-res/master/prd28157.jpg?yocs=u_&yoloc=us'

    self.list = [thickandquick, hometown, vannaschoice, supersaver]