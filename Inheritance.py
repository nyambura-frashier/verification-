class Employee():
  def __init__(self,name,position):
    self.name=name
    self.position=position

  def work(self):
    print(f"The name is {self.name}")
    print(f"He is a {self.position}")
    
employee1=Employee("Brian","Manager")
employee2=Employee("Frashier","Supervisor")

employee1.work()
employee2.work()
    
    
  
  