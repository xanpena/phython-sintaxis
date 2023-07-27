# -+- coding: utf-8 -*-

clients = [
    {
        'nombre': 'Perico',
        'apellido1': 'Perez',
        'apellido2': 'Gonzalez',
        'email': 'pablo.perez@gmail.com'
    },
    {
        'nombre': 'Tome',
        'apellido1': 'Tarrio',
        'apellido2': 'Fuentes',
        'email': 'tome.tarrio@gmail.com'
    }
]

def add_client(client):
    global clients
    if client not in clients:
        clients.append(client)
    else:
        print('Ese cliente ya existe')


def list_clients():
    global clients
    for idx, client in enumerate(clients):
        print('{} | {} {} {} | {}'.format(idx, client['nombre'], client['apellido1'], client['apellido2'], client['email']))


def update_client(client_name, updated_client):
    global clients
    if search_client(client_name) != False:
        index = clients.index(client_name)
        clients[index] = updated_client
    else:
        _get_client_not_found()

def delete_client(client_name):
    global clients
    idx = search_client(client_name)
    if idx != False:
        clients[idx].delete()
    else:
        _get_client_not_found()

def search_client(client_name):
    global clients
    for idx, client in enumerate(clients):
        if(client['nombre'] == client_name):
            return idx
    return False


def _get_client():
    client = {
        'nombre': _get_input('Inserta el nombre del cliente: '),
        'apellido1': _get_input('Inserta su primer apellido: '),
        'apellido2': _get_input('Inserta su segundo apellido: '),
        'email': _get_input('Inserta su email: ')
    }
    return client

def _get_input(label):
    value = None

    while not value:
        value = raw_input(label)

    return value

def _get_client_not_found():
    print('Cliente no encontrado')

def _get_command():
    command = None

    while not command:
        command = input()

    if command not in range(7):
        print('Comando no permitido')
        command = _get_command()
        
    return command


def _print_menu():
    print('-'*50)
    print('Que quieres hacer hoy?:')
    print(u'[1]. Añadir cliente')
    print('[2]. Editar cliente')
    print('[3]. Eliminar cliente')
    print('[4]. Buscar cliente')
    print('[5]. Listar clientes')
    print('[6]. Salir')


if __name__ == '__main__':
    
    print('BIENVENIDOS A PYSHOP')
    print('-'*50)
    while True:
        _print_menu()

        command = _get_command()

        if command == 1:
            client = _get_client()
            add_client(client)
            list_clients()
        elif command == 2:
            client_name = _get_input('Inserta el nombre del cliente: ')
            updated_client = _get_client()
            update_client(client, updated_client)
            list_clients()
        elif command == 3:
            client_name = _get_input('Inserta el nombre del cliente: ')
            delete_client(client_name)
            list_clients()
        elif command == 4:
            client_name = _get_input('Inserta el nombre del cliente: ')

            if search_client(client_name) != False:
                print('Cliente encontrado')
            else:
                print('Cliente no encontrado')
        elif command == 5:
            list_clients()
        elif command == 6:
            print('FIN')
            break
        