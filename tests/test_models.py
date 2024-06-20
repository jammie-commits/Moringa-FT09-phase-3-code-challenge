import unittest
from models.author import Author
from models.article import Article
from models.magazine import Magazine

class TestModels(unittest.TestCase):
    def test_author_creation(self):
        author = Author("John Doe", id=1)
        self.assertEqual(author.name, "John Doe")
        self.assertEqual(author.id, 1)

    def test_article_creation(self):
        author = Author("John Doe", id=1)
        magazine = Magazine("Tech Weekly", "Technology", id=1)
        article = Article("Test Title", "Test Content", author, magazine, id=1)
        self.assertEqual(article.title, "Test Title")
        self.assertEqual(article.content, "Test Content")
        self.assertEqual(article.author, author)
        self.assertEqual(article.magazine, magazine)
        self.assertEqual(article.id, 1)

    def test_magazine_creation(self):
        magazine = Magazine("Tech Weekly", "Technology", id=1)
        self.assertEqual(magazine.name, "Tech Weekly")
        self.assertEqual(magazine.category, "Technology")
        self.assertEqual(magazine.id, 1)

if __name__ == "__main__":
    unittest.main()
