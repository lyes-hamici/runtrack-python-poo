class Student:
    def __init__(self,nom,prenom,num_etud):
        self.__nom = nom
        self.__prenom = prenom
        self.__num_etud = num_etud
        self.__num_credit = 0
        self.__level = self.__studentEval()


    def __str__(self):
        return f"Le nombre de credits de {self.__prenom} {self.__nom} est de {self.__num_credit} points."

    def get_name(self):
        return f"Nom = {self.__nom}"

    def get_firstname (self):
        return f"Prenom = {self.__prenom}"

    def get_Id(self):
        return f"Id = {self.__num_etud}"

    def get_level(self):
        return f"Niveau = {self.__nom}"
    



    def set_name(self,nom):
        self.__nom = nom
    
    def set_firstname(self,prenom):
        self.__prenom = prenom
    
    def set_id(self,id):
        self.__num_etud = id


    def add_credits(self,n):
        if n > 0 :
            self.__num_credit += n
            self.__level = self.__studentEval()

        else:
             self.__num_credit = self.__num_credit



    def get_credit(self):
        return self.__num_credit
        
    def __studentEval(self):
        if self.__num_credit >= 90:
            return "Excellent"
        
        elif   80 <= self.__num_credit < 90:
            return "Tres bien"
        
        elif 70 <= self.__num_credit < 80:
            return "Bien"
        
        elif  60 <= self.__num_credit < 70:
            return "Passable"
        
        elif self.__num_credit < 60:
            return "Insuffisant"
        

    def studentinfo(self):
        return f" Nom = {self.__nom} \n Prenom = {self.__prenom} \n Id = {self.__num_etud} \n Niveau = {self.__level} " 


student = Student("John" ,"Doe",145)

print("-----------------------")

print(student)

print("-----------------------")

student.add_credits(15)
student.add_credits(14)
student.add_credits(1)

print(student)

print("-----------------------")

print(student.studentinfo())

print("-----------------------")

student.add_credits(80)

print(student.studentinfo())




