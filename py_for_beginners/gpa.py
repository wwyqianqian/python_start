class Student:
    def __init__(self, name, hours, qpoints):
        self.name = name
        self.hours = float(hours)
        self.qpoints = float(qpoints)

    def getName(self):
        return self.name

    def getHours(self):
        return self.hours

    def getQpoints(self):
        return self.qpoints

    def gpa(self):
        return self.qpoints/self.hours

def makeStudents(infoStr):
    name, hours, qpoints = infoStr.split("\t")
    return Student(name, hours, qpoints)

def main():
    filename = input("enter name the grade file: ")
    infile = open(filename, 'r')
    best = makeStudents(infile.readline())

    for line in infile:
        s = makeStudents(line)
        if s.gpa() > best.gpa():
            best = s
    infile.close()

    print("the best student is:", best.getName())
    print("hours: ", best.getHours())
    print("GPA is :", best.gpa())


if __name__ == "__main":
    main()