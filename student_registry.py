class Student:
    """
    1. Class Definition
        Attributes:
            Name - string x
            Age - int x
            grade - string x
        Getters
            Name (required) x
                Returns student name
            Age (required) x
                Returns student Age
            Grade (required) x
                Returns student Grade
        Setters of all attr
            Name: (required) x
                Update students name x
                    BEFORE: Validate input x
                    Only if name is 3 characters or more x
                    holds no spaces or special characters x
                    Title format x
            Age: (required) x
                updates student age x
                    BEFORE: Validate input x
                    only if age value is an int type x
                    greater than 11 x
                    less than 18 x
            Grade: (required) x 
                updates student grade x
                    BEFORE: Validate input x
                    If input is an integer: x
                        check if >= 9 AND <=12 x
                        convert to string x
                updates student grade if grade falls within 9th - 12th grade x
                value is formatted with "th" next to the numbered grade x
        Methods:
            __str__ - returns "Student 1: Name: Francisco, Age:15, Grade: 12th" x
            advance - (years_advanced) Returns "Francisco has advanced to the 13th grade."
            study - (subject) returns "Francisco is studying Computer Science."
    2. Initialization
        Create a few instances of the student class, initialize then with different names, ages, grades
        Pring out details of each student using the getters
    
    3. Testing - run test suite
    write own tests on class methods to see if they are working properly
    """

    def __init__(self, name, age=13, grade='12th'):
        self._name = name
        self._age = age
        self._grade = grade

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str) and (len(new_name) >= 3) and (new_name.isalpha()):
            self._name = new_name.title()
            print(new_name)
        else:
            print('Invalid name input: Name must be a string longer than 3 characters with no spaces or special characters.')

    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, new_age):
        if isinstance(new_age, int) and 11 < new_age < 18:
            self._age = new_age
        else:
            print('Invalid age input.')

    @property
    def grade(self):
        return self._grade
    
    @grade.setter
    def grade(self, new_grade):
        valid_grades = ['9th','10th','11th','12th']
        if new_grade in valid_grades:
            self._grade = new_grade
        else:
            print('Invalid grade input.')

    def __str__(self):
        return f"Student 1: Name: {self.name}, Age: {self.age}, Grade: {self.grade}"

    def advance(self, years_advanced=1):
        print(self.grade[0])
        self.grade = f"{int(self.grade[0]) + years_advanced}th"
        print(f"{self.name} has advanced to the {self.grade} grade.")

    def study(self, subject):
        print(f"{self.name} is studying {subject}")




student = Student('Max',13,'10th')

print(student)
student.age = 12
student.grade = "18th"
print(student)
student.advance(10)
print(student)