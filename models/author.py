class Author:
    _author_db = []
    _id_counter = 1

    def __init__(self, name, id=None):
        self.id = id if id is not None else Author._id_counter
        if id is None:
            Author._id_counter += 1
        self.name = name
        self.articles = []
        Author._author_db.append(self)

    def __repr__(self):
        return f'<Author {self.name}>'

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @classmethod
    def get_all(cls):
        return cls._author_db

    def add_article(self, article):
        self.articles.append(article)