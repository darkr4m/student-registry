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
                    BEFORE: Validate input
                    Only if name is 3 characters or more
                    holds no spaces or special characters
                    Title format
            Age: (required) x
                updates student age x
                    BEFORE: Validate input
                    only if age value is an int type
                    greater than 11
                    less than 18
            Grade: (required) x 
                updates student grade x
                    BEFORE: Validate input
                    If input is an integer:
                        check if >= 9 AND <=12
                        convert to string
                updates student grade if grade falls within 9th - 12th grade
                value is formatted with "th" next to the numbered grade
        Methods:
            __str__ - returns "Student 1: Name: Francisco, Age:15, Grade: 12th"
            advance - (years_advanced) Returns "Francisco has advanced to the 13th grade."
            study - (subject) returns "Francisco is studying Computer Science."
    2. Initialization
        Create a few instances of the student class, initialize then with different names, ages, grades
        Pring out details of each student using the getters
    
    3. Testing - run test suite
    write own tests on class methods to see if they are working properly
    """

    def __init__(self, name, age, grade):
        self._name = name
        self._age = age
        self._grade = grade

    @property
    def name(self):
        return self._name
    
    @name.setter
    def set_name(self, new_name):
        self._name = new_name

    @property
    def age(self):
        return self._age
    
    @age.setter
    def set_age(self, new_age):
        self._age = new_age

    @property
    def grade(self):
        return self._grade
    
    @grade.setter
    def set_grade(self, new_grade):
        self._grade = new_grade



student = Student('Max',33,'9th')

print(student.grade)