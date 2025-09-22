class Customer:
    def __init__(self, firstName, lastName, age, email):
        self.firstName =  firstName
        self.lastName =  lastName
        self.age =  age
        self.email =  email

customer1 =  Customer("Roger", "Smith", 82, "rsmith82@mail.net")

print(customer1)