clients = 'Pablo, Ricardo' #creamos el string

def create_client(client_name):
	global clients  #Utilizamos global para definir que la variable es la globarl, es decir la que definimos con pablo y ricardo
	_add_coma() #ejecutamos la funcion _add_coma para agregar una coma y un espacio 
	clients += client_name  #adicionamos el nuevo string



def _add_coma():  #el nombre de la función comienza con un guión bajo para establecer que será una funcion privada
	global clients
	clients +=", " #se agrega una coma y un espacio al string para separar los nuevos valores


def list_clients(): #función que muestra la lista de clientes
	global clients
	return clients #imprimimos el string clientes


if __name__ == '__main__': #funcion main
	print("Primer lista: "+ list_clients())
	list_clients() #Listamos los clientes
	print("****************************************************")
	create_client('Fernando') #ejecutamos la funcion crear cliente
	print("Lista despues de ejecutar la función create_client()")
	print(list_clients()) #Volvemos a ejecutar la funcion listar clientes 
	print("****************************************************")
 
	print ('Funcion lambda')
	#Funcion lambda
	"""
	Se trata de crear funciónes de manera rápida, just in time, sobre la marcha, para prototipos 
	ligeros que requieren únicamente de una pequeña operación o comprobación. Por lo tanto, 
	toda funcioón lambda también puede expresarse como una convencional (pero no viceversa)
	f = lambda argumentos: resultado
	"""
	fun_lambda = lambda x,y: x+y
	print (f'Hola, soy una función... lambda : {fun_lambda}')

	
input() #En este caso la usamos para pausar la ejecución del programa hasta presionar la tecla enter
