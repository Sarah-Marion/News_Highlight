class News:
    def __init__(self, name = None, description = None, url = None):
        self.name = name
        self.description = description
        self.url = url

class Article:
    """
    Article class to define Article Objects
    """
    def __init__(self, title, name, url, imageurl, author=None,timepublished, description = None):
        self.title = title
        self.name = name
        self.url = url
        self.imageurl = imageurl
        self.author = author
        self.timepublished = timepublished
        self.description = description
