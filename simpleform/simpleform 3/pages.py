__author__ = 'brittnicarter'
class Page(object):
    def __init__(self):
        self.title = "Welcome!"
        self.css ="css/stylesheet.css"
        self.head = """

<!DOCTYPE HTML>
<html>

    <head>
        <title>Contact Human Resources Department Form</title>
        <link rel="stylesheet" href="{self.css}">
    </head>
    <img src= "http://brittnicarter.com/wp-content/uploads/2015/07/logo-300x300.png" width= "100" height= "115">
    <h1>Contact Human Resources Department Form</h1>
    <body>"""



        # form
        self.body = '''<form method="GET" action=""
        <label>Name: </label><input type="text" name="user"/>
        <label>Email: </label><input type="text" name="email"/>
        <label>Phone: </label><input type="text" name="phone"/>
        <input type="radio" name="sex" value="male" checked>Male
        <input type="radio" name="sex" value="female">Female

        <p>Who would you like to contact?</p>
            <select name="contact">
                <option value="donald">Donald</option>
                <option value="Richard">Richard</option>
                <option value="lisa">Lisa</option>
                <option value="rhonda">Rhonda</option>
            </select>
            <input type="submit" value="Submit"/>
            '''
        self.close = """

        </form>
    </body>
</html>
        """

        if self.body.GET:
            #stores info we got from the form
            user = self.body.GET['user']
            email = self.body.GET['email']
            sex = self.body.GET['sex']
            phone = self.body.GET['phone']
            contact = self.body.GET['contact']
            self.body.write(self.head + user + ' ' + email + ' ' + sex + ' ' + phone + ' ' + contact + ' ' + self.close)
        else:
            self.body.write(self.head + self.body + self.close) #print