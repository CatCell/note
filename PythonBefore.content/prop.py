class Student:
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value


S = Student()
S.name = "TOm"
print(S.name)
