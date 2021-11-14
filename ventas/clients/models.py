import uuid

class Client:
    #Inicializando el cliente
    def __init__(self, name, company, email, position, uid=None):
        self.name = name
        self.company = company
        self.email = email
        self.position = position
        self.uid = uid or uuid.uuid4() #Usa uuid para obtener un id unico (Estandarizado)
        
    def to_dict(self):
        return vars(self) #Nos permite acceder a la representación de diccionario
    
    @staticmethod #Representación columnar de los datos
    def schema():
        return ['name', 'company', 'email', 'position', 'uid']
    