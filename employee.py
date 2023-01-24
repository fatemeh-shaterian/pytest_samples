class Employee:

    raise_amt = 1.08

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    def get_email(self):
        return "{}.{}@gmail.com".format(self.first, self.last)

    def get_ful_name(self):
        return "{} {}".format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)
