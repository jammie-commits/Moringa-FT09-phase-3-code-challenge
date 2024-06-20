class Magazine:
    _magazine_db = []
    _id_counter = 1

    def __init__(self, name, category, id=None):
        self.id = id if id is not None else Magazine._id_counter
        if id is None:
            Magazine._id_counter += 1
        self.name = name
        self.category = category
        self.articles = []
        Magazine._magazine_db.append(self)

    def __repr__(self):
        return f'<Magazine {self.name}>'

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        self._category = value

    @classmethod
    def get_all(cls):
        return cls._magazine_db

    def add_article(self, article):
        self.articles.append(article)
