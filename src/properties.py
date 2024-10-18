

class Person:
    def __init__(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name

    @property
    def first_name(self):
        """Property that functions as the 'getter' to get the first name value and capitalize it."""
        return self._first_name.title()

    @first_name.setter
    def first_name(self, name):
        """Property that functions as a 'setter', to set a new first name value."""
        self._first_name = name

    @property
    def full_name(self):
        """Property that combines first and last name to create the full name"""
        return f"{self._first_name} {self._last_name}".title()

    @full_name.setter
    def full_name(self, new_full_name):
        """'setter' function to accept a full name, split it into first and last names and assign them to their variables."""
        split_name = new_full_name.split(' ')

        # If user only provided one name, we assume it's first name
        if len(split_name) == 1:
            self._first_name = split_name[0]

        # otherwise we split into first and last name
        else:
            self._first_name = split_name[0]
            self._last_name = split_name[1]


natalia = Person('natalia', 'luna')
print(natalia.full_name)

natalia.full_name = 'petunia ramirez'

print(natalia.full_name)
