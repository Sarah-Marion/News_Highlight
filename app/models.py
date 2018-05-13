class News:
    def __init__(self, name = None, description = None, url = None):
        self.name = name
        self.description = description
        self.url = url

class Articles:
    """
    Articles class to define Article Objects
    """
    def __init__(self, author, title, description, urlToImage, url, publishedAt):
        self.author = author
        self.title = title
        self.description = description
        self.urlToImage = urlToImage
        self.url = url
        self.publishedAt = publishedAt


class Sources:
    """
    Sources class to define the News Source Objects
    """
    def __init__(self, id, name, description, url, category):
        self.id = id
        self. name = name
        self.description = description
        self.url = url
        self.category = category
