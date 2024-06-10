class Magazine:
    def __init__(self, id, name, category):
        # Validate data types and potentially name/category length
        if not isinstance(id, int):
            raise ValueError("Magazine ID must be an integer")
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Magazine name must be a non-empty string")
        if not isinstance(category, str) or len(category) == 0:
            raise ValueError("Magazine category must be a non-empty string")

        self._id = id
        self._name = name
        self._category = category

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def category(self):
        return self._category

    def __repr__(self):
        return f'<Magazine {self.name}>'

