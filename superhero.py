class Superhero:
    # __init__ is a built-in method and will always be called when creating a Superhero object.
    # Self refers to the object itself, and serves the same functions as 'this' in Java.
    def __init__(self, first_name, last_name, release_date, hero_name, powers):
        self._first_name = first_name
        self._last_name = last_name
        self._release_date = release_date
        self._hero_name = hero_name
        self._powers = powers

    # Property for first_name
    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        self._first_name = first_name

    # Property for last_name
    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        self._last_name = last_name

    # Property for release_date
    @property
    def release_date(self):
        return self._release_date

    @release_date.setter
    def release_date(self, release_date):
        self._release_date = release_date

    # Property for hero_name
    @property
    def hero_name(self):
        return self._hero_name

    @hero_name.setter
    def hero_name(self, hero_name):
        self._hero_name = hero_name

    # Property for powers
    @property
    def powers(self):
        return self._powers

    @powers.setter
    def powers(self, powers):
        self._powers = powers
