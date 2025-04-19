class Employee:
    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.salary = salary
        self.salaries = []

    def __repr__(self):
        return f"Employee({self.first!r}, {last!r}, {salary!r})"

    def __len__(self):
        return len(self.salaries)

    def __iter__(self):
        return iter(self.salaries)

    def give_rise(self):
        self.salary += 5000

    def set_rise_amount(self, rise):
        self.salary += rise

    def store_salaries(self):
        self.salaries.append(self.salary)

    def print_all(self):
        for salary in self.salaries:
            print(self.first.title(), self.last.title(), salary)

print("press 'q' to quit")
while True:
    first = input("Provide first name: ")
    if first == 'q':
        break

    last = input("Provide last name: ")
    if last == 'q':
        break

    salary = input("Input salary: ")
    salary = int(salary)
    if str(salary) == 'q':
        break

    employee = Employee(first, last, salary)
    employee.print_all()

    answer = input("Provide a fix rise (y/n): ")
    if answer == 'y':
        employee.give_rise()
    else:
        amount = input("Provide custom amount: ")
        amount = int(amount)
        employee.set_rise_amount(amount)

    employee.store_salaries()
    employee.print_all()

