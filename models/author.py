class Author:
    def __init__(self, id, name):
        # Validate data types and values
        if not isinstance(id, int):
            raise ValueError("Author ID must be an integer")
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Author name must be a non-empty string")

        self._id = id  # Use private attribute (optional)
        self._name = name

    @property
    def id(self):
        return self._id  # Getter for ID

    @property
    def name(self):
        return self._name  # Getter for name

    def __repr__(self):
        return f'<Author {self.name}>'

