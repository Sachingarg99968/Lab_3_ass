import pandas as pd

data=[]
class Empl_y:
    def __init__(self,id,name,age,salary):
       self.id=id
       self.name=name
       self.age=age
       self.salary=salary

    def to_dict(self):
        headers = ['Empl_y ID', 'Name', 'Age', 'Salary']
        for i in range(0,len(headers)):
            return[self.id,self.name,self.age,self.salary]
            
    def sort_age(self):
        self.data = self.data.sort_values("Age")
        return data

g1=Empl_y("161E90","Raman",41,56000)
g2=Empl_y("161F91","Himadri",38,67500)
g3=Empl_y("161F99","Jaya",51,82100)
g4=Empl_y("171E20","Tejas",30,55000)
g5=Empl_y("171G30","Ajay",45,44000)

tst_1=g1.to_dict()
tst_2=g2.to_dict()
tst_3=g3.to_dict()
tst_4=g4.to_dict()

data.append(tst_1)
data.append(tst_2)
data.append(tst_3)
data.append(tst_4)

df = pd.DataFrame(data, columns=['Empl_y ID', 'Name', 'Age', 'Salary'])
print(df)
val_u=1
while val_u:
    print("1. age")
    print("2. name")
    print("3. salary")
    print("4. Exit")
    val_u=int(input("Enter your choice: "))
    if val_u==1:
        df=df.sort_values("Age")
        print(df)
    elif val_u==2:
        df=df.sort_values("Name")
        print(df)
    elif val_u==3:
        df=df.sort_values("Salary")
        print(df)
    elif val_u==4:
        exit()
    else:
        exit()