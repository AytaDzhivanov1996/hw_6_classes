class Employee:
    __slots__ = ('first', 'last')

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def fullname(self):
        return f'{self.first} {self.last}'

    @fullname.setter
    def fullname(self, name):
        first_name, last_name = name.split()
        self.first = first_name
        self.last = last_name

    @fullname.deleter
    def fullname(self):
        self.first = None
        self.last = None

    @property
    def email(self):
        return f'{self.first}.{self.last}@gmail.com'
