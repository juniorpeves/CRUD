import csv
#Directiva de importación para  usar la función sin llamar el modulo
from clients.models import Client

class ClientService:
    
    def __init__(self, table_name): #Recibir el nombre de la tabla donde guardar
        self.table_name = table_name
        
    #Metodo que crea cliente
    def create_client(self, client): 
        #Abrir el archivo en modo de APPEND (adjuntar)
        with open(self.table_name, mode='a') as f:
            # Inicializando el csv con el schema de Client en modo escritura
            writer = csv.DictWriter(f, fieldnames=Client.schema())
            # Agregando al cliente nuevo en una nueva fila como diccionario
            writer.writerow(client.to_dict()) 
    # CLASE 42
    # Metodo que presenta la lista
    def list_clients(self):
        #Abrir el archivo en modo de READ (lectura)
        with open(self.table_name, mode='r') as f:
            # Inicializando el csv con el schema de Client en modo lectura
            reader = csv.DictReader(f, fieldnames=Client.schema())
            # Devuelve en lista las lecturas
            return list(reader)