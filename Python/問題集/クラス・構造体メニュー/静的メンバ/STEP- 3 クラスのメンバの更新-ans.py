class Employee:
    def __init__(self, number, name):
        self.number = number
        self.name = name

    def getnum(self):
        return self.number

    def getname(self):
        return self.name

    def change_num(self, number):
        self.number = number

    def change_name(self, name):
        self.name = name


n = int(input())

roster = []
for _ in range(n):
    values = input().split()

    query = values[0]
    if query == "make":
        number = int(values[1])
        name = values[2]
        roster.append(Employee(number, name))
    else:
        index = int(values[1]) - 1
        if query == "getnum":
            number = roster[index].getnum()
            print(number)
        elif query == "getname":
            name = roster[index].getname()
            print(name)
        elif query == "change_num":
            new_num = int(values[2])
            roster[index].change_num(new_num)
        else:
            new_name = values[2]
            roster[index].change_name(new_name)