class News:
    def __init__(self, name = None, description = None, url = None):
        self.name = name
        self.description = description
        self.url = url

class Articles:
    """
    Articles class to define Article Objects
    """
    def __init__(self, title, name, url, imageurl, author,timepublished, description):
        self.title = title
        self.name = name
        self.url = url
        self.imageurl = imageurl
        self.author = author
        self.timepublished = timepublished
        self.description = description


class Sources:
    """
    Sources class to define the News Source Objects
    """
    def __init__(self, id, name, description, url, category):
        self.id = id
        self. name = name
        self.description = description
        self.url = url
        self.category =  category
