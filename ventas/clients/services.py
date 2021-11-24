import csv
import os #CLASE 43
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
    # CLASE 43
    # Metodo que actualiza un cliente, recibe a un cliente actualizado
    
    def update_client(self, updated_client):
        # Obtener la lista de clientes      
        clients = self.list_clients()
        # Crear la lista vacia
        updated_clients = []
        for client in clients:
            # Si el cliente tiene el mismo id se actualiza y se añada el cliente_update
            if client['uid'] == updated_client.uid:
                updated_clients.append(updated_client.to_dict())
            else:
                updated_clients.append(client)
        # Metodo privado para guardar en disco
        self._save_to_disk(updated_clients)
    
    # CLASE 43
    def _save_to_disk(self, clients):
        tmp_table_name = self.table_name + '.tmp'
        with open(tmp_table_name) as f:
            writer = csv.DictWriter(f, fieldnames=Client.schema())
            writer.writerow(clients)
        # Renombra y eliminar con em modulo os
        os.remove(self.table_name)    
        os.rename(tmp_table_name, self.table_name)
        