import csv
#Directiva de importación para  usar la función sin llamar el modulo
from clients.models import Client

class ClientService:
    
    def __init__(self, table_name): #Recibir el nombre de la tabla donde guardar
        self.table_name = table_name
    
    def create_client(self, client): 
        #Abriendo el archivo
        with open(self.table_name, mode='a') as f:
            # Inicializando el csv con el schema de Client
            writer = csv.DictWriter(f, fieldnames=Client.schema())
            # Agregando al cliente nuevo en una nueva fila como diccionario
            writer.writerow(client.to_dict()) 