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

input_num = int(input())
employee_arr = []
for _ in range(input_num):
    input_line = input().split()
    query = input_line[0]
    if(query == "make"):
        number = int(input_line[1])
        name = input_line[2]
        employee_arr.append(Employee(number,name))

    elif(query == "getnum"):
        index = int(input_line[1])
        print(employee_arr[index-1].getnum())

    elif(query == "getname"):
        index = int(input_line[1])
        print(employee_arr[index-1].getname())

    elif(query == "change_num"):
        index = int(input_line[1])
        newnum = int(input_line[2])
        employee_arr[index-1].change_num(newnum)

    elif(query == "change_name"):
        index = int(input_line[1])
        newname = input_line[2]
        employee_arr[index-1].change_name(newname)