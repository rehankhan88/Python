class Emp:
    def __init__(self, name):
        self.name = name


    def __str__(self):    
        return f"the name of Employee is {self.name}"
    def __repr__(self):    
        return f"the name of Employee is {self.name}"
    def __call__(self):    
        return "hi i m good"