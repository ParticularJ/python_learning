# implicit inheritance

class Parent(object):

    def implicit(self):
        print("PARENT IMPLICIT()")

    def override(self):
        print("PARENT override()")

    def altered(self):
        print("PARENT altered()")


class Child(Parent):
    def override(self):
        print("CHILD override()")

    def altered(self):
        print("CHILD, BEFORE PARENT altered()")
        super(Child, self).altered()
        print("CHILD, AFTER PARENT altered()")

class Other(object):

    def override(self):
        print("OTHER override()")

    def implicit(self):
        print("OTHER implicit()")

    def altered(self):
        print("OTHER altered()")

class Other_Child(object):

    def __init__(self):
        self.other = Other()

    def implicit(self):
        self.other.implicit()

    def override(self):
        print("OTHER CHILD override()")

    def altered(self):
        print("Other_Child, BEFORE Other_Child altered()")
        self.other.altered()
        print("Other_Child, AFTER Other_Child altered()")


#dad = Parent()
#son = Child()
other_son = Other_Child()


#dad.implicit()
#son.implicit()
#dad.override()
#son.override()
#dad.altered()
#son.altered()
other_son.implicit()
other_son.override()
other_son.altered()
