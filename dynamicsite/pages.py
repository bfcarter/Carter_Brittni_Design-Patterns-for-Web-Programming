class Page(self):
    def get(self):
        pass


class ContentPage(object):
        def __init__(self):
            self._title = "Welcome!"
            self.css = "css/styles.css"
            self._head = """
<!DOCTYPE HTML>
<html>
    <head>
        <title> Enter your information: </title>
        <link href="css/styles.css" rel="Stylesheet" type="text/css"/>
    </head>
    <body>
        """

        self.body = ""
        self._error = ''
        self._close = """
    </body>
</html>
        """

    def print_out(self):
        all = self._head + self.body + self._error + _self._close
        return all