class Article:
    _article_db = []
    _id_counter = 1

    def __init__(self, title, content, author, magazine, id=None):
        self.id = id if id is not None else Article._id_counter
        if id is None:
            Article._id_counter += 1
        self.title = title
        self.content = content
        self.author = author
        self.magazine = magazine
        Article._article_db.append(self)
        author.add_article(self)
        magazine.add_article(self)

    def __repr__(self):
        return f'<Article {self.title}>'

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value

    @property
    def author(self):
        return self._author

    @property
    def magazine(self):
        return self._magazine

    @classmethod
    def get_all(cls):
        return cls._article_db

    @magazine.setter
    def magazine(self, value):
        self._magazine = value

    @author.setter
    def author(self, value):
        self._author = value