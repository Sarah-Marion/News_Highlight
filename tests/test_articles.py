import unittest
from app.models import Articles

class ArticleTest(unittest.TestCase):
    """
    Test Article class to test behaviours of the Article class
    
    Args:
        Unittest.TestCase: Test case class that helps create test cases
    """

    def setUp(self):
        """
        Set up method to run before each test case
        """
        self.new_article = Articles('BBC News', "Paris attack suspect 'of Chechen origin'", 'The man killed one person and injured four others in Paris in an attack claimed by the IS group.', 'https://ichef.bbci.co.uk/images/ic/1024x576/p06705l3.jpg','http://www.bbc.co.uk/news/world-europe-44098615', '2018-05-13T06:36:21Z')

    
    
    def test_instance(self):
        """
        Test case to check if self.new_article is an instance of Article
        """
        self.assertTrue(isinstance(self.new_article, Articles) )

    
    
    def test_init(self):
        """
        Test case to check if the Article class is initialised
        """
        self.assertEquals( self.new_article.author, 'BBC News')
        self.assertEquals( self.new_article.title, "Paris attack suspect 'of Chechen origin'")
        self.assertEquals( self.new_article.description, 'The man killed one person and injured four others in Paris in an attack claimed by the IS group.')
        self.assertEquals( self.new_article.urlToImage, 'https://ichef.bbci.co.uk/images/ic/1024x576/p06705l3.jpg')
        self.assertEquals( self.new_article.url, 'http://www.bbc.co.uk/news/world-europe-44098615')
        self.assertEquals( self.new_article.publishedAt, '2018-05-13T06:36:21Z')

    
    
    def test_publish_date_format(self):
        """
        Test case to check if UTC date format is converted to a display-friendly format
        """
        
        # display_friendly_format = self.new_article.publish_date_format(self.new_article.publishedAt)
        # self.assertEqual( display_friendly_format, '2018-05-13')


